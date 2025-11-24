from rest_framework import serializers
from .models import Product, Category, ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'alt_text', 'is_primary']

class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'parent', 'icon', 'product_count']

    def get_product_count(self, obj):
        return obj.products.filter(is_active=True).count()

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    vendor_name = serializers.CharField(source='vendor.company_name', read_only=True)
    average_rating = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'slug', 'category', 'category_name',
            'vendor', 'vendor_name', 'price', 'discounted_price', 'final_price',
            'energy_efficiency_rating', 'carbon_footprint', 'energy_consumption',
            'recyclable_percentage', 'certifications', 'specifications',
            'warranty_years', 'availability', 'is_featured', 'is_active',
            'images', 'average_rating', 'review_count', 'created_at'
        ]
        read_only_fields = ['slug', 'vendor', 'final_price', 'average_rating', 'review_count']

    def get_average_rating(self, obj):
        reviews = obj.reviews.filter(is_approved=True)
        if reviews.exists():
            return round(reviews.aggregate(avg=models.Avg('overall_rating'))['avg'], 1)
        return 0.0

    def get_review_count(self, obj):
        return obj.reviews.filter(is_approved=True).count()