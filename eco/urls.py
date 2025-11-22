from django.urls import path
from . import views

urlpatterns = [
    # Home and general pages
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # Authentication
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # User profile
    path('profile/', views.profile, name='profile'),
    path('profile/setup/', views.profile_setup, name='profile_setup'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),

    # Products
    path('products/', views.product_list, name='product_list'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('product/<slug:slug>/review/', views.add_review, name='add_review'),

    # Shopping cart
    path('cart/', views.cart_view, name='cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:item_id>/', views.update_cart, name='update_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),

    # Checkout and orders
    path('checkout/', views.checkout, name='checkout'),
    path('order/<str:order_number>/', views.order_detail, name='order_detail'),
    path('orders/', views.order_history, name='order_history'),

    # Vendor
    path('vendor/register/', views.vendor_register, name='vendor_register'),
    path('vendor/dashboard/', views.vendor_dashboard, name='vendor_dashboard'),
    path('vendor/product/add/', views.vendor_add_product, name='vendor_add_product'),
    path('vendor/product/<int:product_id>/edit/', views.vendor_edit_product, name='vendor_edit_product'),
]
