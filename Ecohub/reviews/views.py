from django.shortcuts import get_object_or_404
from django.db import models
from rest_framework import viewsets, permissions, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Review
from products.models import Product
from .serializers import (
    ReviewSerializer,
    ReviewListSerializer,
    ReviewCreateSerializer
)


class IsReviewOwner(permissions.BasePermission):
    """
    Custom permission to only allow review owners to edit/delete their reviews.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class ReviewViewSet(viewsets.ModelViewSet):
    """
    ViewSet for review CRUD operations.
    """
    queryset = Review.objects.filter(is_approved=True)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsReviewOwner]

    def get_serializer_class(self):
        if self.action == 'create':
            return ReviewCreateSerializer
        elif self.action == 'list':
            return ReviewListSerializer
        return ReviewSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filter by product
        product_id = self.request.query_params.get('product')
        if product_id:
            queryset = queryset.filter(product_id=product_id)

        # Filter by user
        user_id = self.request.query_params.get('user')
        if user_id:
            queryset = queryset.filter(user_id=user_id)

        # Filter verified purchases only
        verified_only = self.request.query_params.get('verified')
        if verified_only:
            queryset = queryset.filter(is_verified_purchase=True)

        # Order by rating, helpful votes, or date
        ordering = self.request.query_params.get('order_by', '-created_at')
        if ordering in ['overall_rating', '-overall_rating', 'helpful_votes', '-helpful_votes', '-created_at']:
            queryset = queryset.order_by(ordering)

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def my_reviews(self, request):
        """Get all reviews by the current user."""
        reviews = Review.objects.filter(user=request.user)
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def mark_helpful(self, request, pk=None):
        """Mark a review as helpful."""
        review = self.get_object()
        review.helpful_votes += 1
        review.save()
        return Response({
            'message': 'Review marked as helpful',
            'helpful_votes': review.helpful_votes
        })

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAdminUser])
    def approve(self, request, pk=None):
        """Approve a review (admin only)."""
        review = self.get_object()
        review.is_approved = True
        review.save()
        return Response({'message': 'Review approved successfully'})

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAdminUser])
    def verify_purchase(self, request, pk=None):
        """Verify a review as from a genuine purchase (admin only)."""
        review = self.get_object()
        review.is_verified_purchase = True
        review.save()
        return Response({'message': 'Review marked as verified purchase'})


class ProductReviewsView(generics.ListAPIView):
    """
    View to get all reviews for a specific product.
    """
    serializer_class = ReviewListSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        product_id = self.kwargs.get('product_id')
        return Review.objects.filter(
            product_id=product_id,
            is_approved=True
        ).order_by('-created_at')

    def get(self, request, *args, **kwargs):
        product_id = self.kwargs.get('product_id')
        product = get_object_or_404(Product, pk=product_id)

        reviews = self.get_queryset()
        serializer = self.get_serializer(reviews, many=True)

        # Calculate aggregate statistics
        if reviews.exists():
            avg_overall = reviews.aggregate(models.Avg('overall_rating'))['overall_rating__avg']
            avg_eco = reviews.aggregate(models.Avg('eco_impact_rating'))['eco_impact_rating__avg']
            avg_value = reviews.aggregate(models.Avg('value_for_money'))['value_for_money__avg']
            avg_quality = reviews.aggregate(models.Avg('build_quality'))['build_quality__avg']
        else:
            avg_overall = avg_eco = avg_value = avg_quality = 0

        return Response({
            'product_id': product.id,
            'product_name': product.name,
            'total_reviews': reviews.count(),
            'average_ratings': {
                'overall': round(avg_overall, 2) if avg_overall else 0,
                'eco_impact': round(avg_eco, 2) if avg_eco else 0,
                'value_for_money': round(avg_value, 2) if avg_value else 0,
                'build_quality': round(avg_quality, 2) if avg_quality else 0,
            },
            'reviews': serializer.data
        })
