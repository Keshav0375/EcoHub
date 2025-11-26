from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from products import views as product_views
from vendors import views as vendor_views
from accounts import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # API endpoints
    path('api/auth/', include('accounts.urls')),
    path('api/products/', include('products.urls')),
    path('api/vendors/', include('vendors.urls')),
    path('api/reviews/', include('reviews.urls')),

    # Web views - Products
    path('', product_views.home_view, name='home'),
    path('products/', product_views.product_list_view, name='product-list'),
    path('products/<slug:slug>/', product_views.product_detail_view, name='product-detail'),
    path('impact-calculator/', product_views.impact_calculator_view, name='impact-calculator'),

    # Web views - Vendors
    path('vendors/', vendor_views.vendor_list_view, name='vendor-list'),
    path('vendors/<int:pk>/', vendor_views.vendor_detail_view, name='vendor-detail'),
    path('vendor-dashboard/', vendor_views.vendor_dashboard_view, name='vendor-dashboard'),
    path('become-vendor/', vendor_views.become_vendor_view, name='become-vendor'),

    # Web views - Authentication
    path('login/', account_views.login_view, name='login'),
    path('register/', account_views.register_view, name='register'),
    path('logout/', account_views.logout_view, name='logout'),
    path('profile/', account_views.profile_view, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)