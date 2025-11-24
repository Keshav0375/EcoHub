from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'', views.ReviewViewSet, basename='review')

app_name = 'reviews'

urlpatterns = [
    # API endpoints
    path('api/', include(router.urls)),
    path('api/product/<int:product_id>/', views.ProductReviewsView.as_view(), name='product_reviews'),
]