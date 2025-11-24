from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/products/', include(('products.urls', 'products'), namespace='products-api')),
    path('api/vendors/', include(('vendors.urls', 'vendors'), namespace='vendors-api')),
    path('api/reviews/', include(('reviews.urls', 'reviews'), namespace='reviews-api')),
    path('', include(('products.urls', 'products'), namespace='products')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)