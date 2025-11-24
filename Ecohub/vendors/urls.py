from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'', views.VendorViewSet, basename='vendor')

app_name = 'vendors'

urlpatterns = [
    # Web views
    path('vendors/', views.vendor_list_view, name='list'),
    path('vendors/<int:pk>/', views.vendor_detail_view, name='detail'),
    path('dashboard/', views.vendor_dashboard_view, name='dashboard'),
    path('become-vendor/', views.become_vendor_view, name='become_vendor'),
    
    # API endpoints
    path('api/', include(router.urls)),
    path('api/apply/', views.VendorApplicationView.as_view(), name='apply'),
]