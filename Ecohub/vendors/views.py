from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Vendor
from .serializers import (
    VendorSerializer,
    VendorListSerializer,
    VendorApplicationSerializer
)


class IsVendorOwner(permissions.BasePermission):
    """
    Custom permission to only allow vendor owners to edit their profile.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class VendorViewSet(viewsets.ModelViewSet):
    """
    ViewSet for vendor CRUD operations.
    """
    queryset = Vendor.objects.filter(is_active=True)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsVendorOwner]

    def get_serializer_class(self):
        if self.action == 'list':
            return VendorListSerializer
        return VendorSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filter by verification status
        status_filter = self.request.query_params.get('status')
        if status_filter:
            queryset = queryset.filter(verification_status=status_filter)

        # Filter by featured
        is_featured = self.request.query_params.get('featured')
        if is_featured:
            queryset = queryset.filter(is_featured=True)

        # Filter verified vendors only
        verified_only = self.request.query_params.get('verified')
        if verified_only:
            queryset = queryset.filter(verification_status='verified')

        # Order by rating or eco impact
        ordering = self.request.query_params.get('order_by', '-created_at')
        if ordering in ['rating', '-rating', 'eco_impact_score', '-eco_impact_score', '-created_at']:
            queryset = queryset.order_by(ordering)

        return queryset

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def my_profile(self, request):
        """Get the vendor profile for the current user."""
        try:
            vendor = Vendor.objects.get(user=request.user)
            serializer = self.get_serializer(vendor)
            return Response(serializer.data)
        except Vendor.DoesNotExist:
            return Response(
                {"detail": "You don't have a vendor profile."},
                status=status.HTTP_404_NOT_FOUND
            )

    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        """Get all products for a specific vendor."""
        vendor = self.get_object()
        products = vendor.products.all()
        # Import here to avoid circular dependency
        from products.serializers import ProductSerializer
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(serializer.data)


class VendorApplicationView(generics.CreateAPIView):
    """
    View for submitting vendor application.
    """
    serializer_class = VendorApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            vendor = serializer.save()
            return Response({
                'message': 'Vendor application submitted successfully. Awaiting verification.',
                'vendor': VendorSerializer(vendor).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Template views (for web frontend if needed)
def vendor_list_view(request):
    """List all verified vendors."""
    vendors = Vendor.objects.filter(is_active=True, verification_status='verified')
    return render(request, 'vendors/list.html', {'vendors': vendors})


def vendor_detail_view(request, pk):
    """Show vendor detail page."""
    vendor = get_object_or_404(Vendor, pk=pk, is_active=True)
    return render(request, 'vendors/detail.html', {'vendor': vendor})


def vendor_dashboard_view(request):
    """Vendor dashboard for managing their profile and products."""
    if not request.user.is_authenticated:
        from django.shortcuts import redirect
        return redirect('login')

    try:
        vendor = Vendor.objects.get(user=request.user)
        return render(request, 'vendors/dashboard.html', {'vendor': vendor})
    except Vendor.DoesNotExist:
        return render(request, 'vendors/no_profile.html')


def become_vendor_view(request):
    """Page for users to apply to become a vendor."""
    return render(request, 'vendors/become_vendor.html')
