from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'', views.ProductViewSet, basename='product')
router.register(r'categories', views.CategoryViewSet, basename='category')

app_name = 'products'

urlpatterns = [
    # API endpoints only
    path('', include(router.urls)),
    path('search/', views.ProductSearchView.as_view(), name='search'),
    path('featured/', views.FeaturedProductsView.as_view(), name='featured'),
]