from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from products import views as product_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # API endpoints
    path('api/auth/', include('accounts.urls')),
    path('api/products/', include('products.urls')),
    path('api/vendors/', include('vendors.urls')),
    path('api/reviews/', include('reviews.urls')),

    # Web views (optional - only if you need template views)
    path('', product_views.home_view, name='home'),
    path('products/', product_views.product_list_view, name='product-list'),
    path('products/<slug:slug>/', product_views.product_detail_view, name='product-detail'),
    path('impact-calculator/', product_views.impact_calculator_view, name='impact-calculator'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)