from django.contrib import admin
from .models import (
    UserProfile, Category, Vendor, Product,
    Review, Cart, CartItem, Order, OrderItem
)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'city', 'state', 'carbon_offset', 'created_at']
    search_fields = ['user__username', 'user__email', 'city']
    list_filter = ['country', 'created_at']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'user', 'is_verified', 'rating', 'created_at']
    list_filter = ['is_verified', 'created_at']
    search_fields = ['company_name', 'user__username', 'email']
    list_editable = ['is_verified']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'vendor', 'category', 'price', 'stock', 'environmental_rating', 'is_active', 'featured']
    list_filter = ['category', 'environmental_rating', 'is_active', 'featured', 'recyclable', 'biodegradable']
    search_fields = ['name', 'description', 'vendor__company_name']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['is_active', 'featured', 'price', 'stock']
    readonly_fields = ['views', 'created_at', 'updated_at']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'rating', 'title', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['product__name', 'user__username', 'title', 'comment']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'updated_at']
    search_fields = ['user__username']


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'product', 'quantity', 'added_at']
    list_filter = ['added_at']
    search_fields = ['cart__user__username', 'product__name']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'user', 'status', 'total', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['order_number', 'user__username', 'shipping_city']
    list_editable = ['status']
    readonly_fields = ['order_number', 'created_at', 'updated_at']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price']
    search_fields = ['order__order_number', 'product__name']
