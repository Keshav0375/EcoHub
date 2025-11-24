from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Avg
from rest_framework import viewsets, filters, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product, Category, ProductImage
from .serializers import ProductSerializer, CategorySerializer, ProductImageSerializer
from .filters import ProductFilter
from .permissions import IsVendorOrReadOnly

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsVendorOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'description', 'category__name']
    ordering_fields = ['price', 'created_at', 'energy_efficiency_rating', 'carbon_footprint']
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True).select_related('category', 'vendor')
        
        # Filter by vendor for vendor users
        if self.request.user.is_authenticated and self.request.user.user_type == 'vendor':
            if self.action in ['list'] and self.request.query_params.get('my_products'):
                queryset = queryset.filter(vendor__user=self.request.user)
        
        return queryset

    def perform_create(self, serializer):
        if self.request.user.user_type != 'vendor':
            raise PermissionError("Only vendors can create products")
        serializer.save(vendor=self.request.user.vendor_profile)

    @action(detail=False, methods=['get'])
    def my_products(self, request):
        """Vendor's own products"""
        if request.user.user_type != 'vendor':
            return Response({"error": "Only vendors can access this endpoint"}, 
                          status=status.HTTP_403_FORBIDDEN)
        
        products = self.get_queryset().filter(vendor__user=request.user)
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def toggle_featured(self, request, pk=None):
        """Toggle featured status - Admin only"""
        if not request.user.is_staff:
            return Response({"error": "Admin access required"}, 
                          status=status.HTTP_403_FORBIDDEN)
        
        product = self.get_object()
        product.is_featured = not product.is_featured
        product.save()
        return Response({"is_featured": product.is_featured})

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        """Get products in this category"""
        category = self.get_object()
        products = Product.objects.filter(category=category, is_active=True)
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(serializer.data)

class ProductSearchView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        category = self.request.query_params.get('category')
        certification = self.request.query_params.get('certification')
        
        queryset = Product.objects.filter(is_active=True)
        
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | 
                Q(description__icontains=query) |
                Q(category__name__icontains=query)
            )
        
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        if category:
            queryset = queryset.filter(category_id=category)
        if certification:
            queryset = queryset.filter(certifications=certification)
            
        return queryset

class FeaturedProductsView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        return Product.objects.filter(is_featured=True, is_active=True)[:8]

# Web Views for traditional Django templates
def home_view(request):
    featured_products = Product.objects.filter(is_featured=True, is_active=True)[:6]
    categories = Category.objects.all()[:8]
    return render(request, 'products/home.html', {
        'featured_products': featured_products,
        'categories': categories,
    })

def product_list_view(request):
    products = Product.objects.filter(is_active=True)
    categories = Category.objects.all()
    return render(request, 'products/product_list.html', {
        'products': products,
        'categories': categories,
    })

def product_detail_view(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    related_products = Product.objects.filter(
        category=product.category, 
        is_active=True
    ).exclude(id=product.id)[:4]
    
    return render(request, 'products/product_detail.html', {
        'product': product,
        'related_products': related_products,
    })

def impact_calculator_view(request):
    return render(request, 'products/impact_calculator.html')