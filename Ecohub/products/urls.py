from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'', views.ProductViewSet, basename='product')
router.register(r'categories', views.CategoryViewSet, basename='category')

app_name = 'products'

urlpatterns = [
    # Web views
    path('', views.home_view, name='home'),
    path('products/', views.product_list_view, name='list'),
    path('products/<slug:slug>/', views.product_detail_view, name='detail'),
    path('impact-calculator/', views.impact_calculator_view, name='impact_calculator'),
    
    # API endpoints
    path('api/', include(router.urls)),
    path('api/search/', views.ProductSearchView.as_view(), name='search'),
    path('api/featured/', views.FeaturedProductsView.as_view(), name='featured'),
]