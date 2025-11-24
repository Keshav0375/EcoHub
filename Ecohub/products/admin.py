from django.contrib import admin
from .models import Product, Category, ProductImage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', 'created_at']
    list_filter = ['parent', 'created_at']
    search_fields = ['name', 'description']

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'vendor', 'price', 'energy_efficiency_rating', 'is_featured', 'is_active']
    list_filter = ['category', 'is_featured', 'is_active', 'energy_efficiency_rating', 'certifications']
    search_fields = ['name', 'description']
    inlines = [ProductImageInline]
    readonly_fields = ['slug', 'created_at', 'updated_at']
    prepopulated_fields = {"slug": ("name",)}