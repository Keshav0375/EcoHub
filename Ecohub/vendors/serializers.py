from rest_framework import serializers
from .models import Vendor
from accounts.serializers import UserProfileSerializer


class VendorSerializer(serializers.ModelSerializer):
    """Serializer for vendor profile"""
    user = UserProfileSerializer(read_only=True)
    is_verified = serializers.BooleanField(read_only=True)

    class Meta:
        model = Vendor
        fields = [
            'id', 'user', 'company_name', 'business_license', 'tax_id',
            'business_address', 'contact_phone', 'website',
            'verification_status', 'sustainability_certificate',
            'verification_documents', 'rating', 'total_sales',
            'eco_impact_score', 'description', 'logo', 'banner_image',
            'is_featured', 'is_active', 'is_verified',
            'created_at', 'updated_at'
        ]
        read_only_fields = [
            'id', 'user', 'verification_status', 'rating',
            'total_sales', 'eco_impact_score', 'is_featured',
            'is_verified', 'created_at', 'updated_at'
        ]


class VendorListSerializer(serializers.ModelSerializer):
    """Lighter serializer for vendor list views"""
    user_email = serializers.EmailField(source='user.email', read_only=True)
    user_username = serializers.CharField(source='user.username', read_only=True)
    is_verified = serializers.BooleanField(read_only=True)

    class Meta:
        model = Vendor
        fields = [
            'id', 'user_email', 'user_username', 'company_name',
            'business_address', 'contact_phone', 'website',
            'verification_status', 'rating', 'eco_impact_score',
            'description', 'logo', 'banner_image', 'is_featured',
            'is_verified', 'created_at'
        ]


class VendorApplicationSerializer(serializers.ModelSerializer):
    """Serializer for vendor application"""

    class Meta:
        model = Vendor
        fields = [
            'company_name', 'business_license', 'tax_id',
            'business_address', 'contact_phone', 'website',
            'description', 'logo', 'banner_image',
            'sustainability_certificate', 'verification_documents'
        ]

    def create(self, validated_data):
        user = self.context['request'].user
        vendor = Vendor.objects.create(user=user, **validated_data)
        # Update user type to vendor
        user.user_type = 'vendor'
        user.save()
        return vendor

    def validate(self, attrs):
        user = self.context['request'].user
        if hasattr(user, 'vendor_profile'):
            raise serializers.ValidationError(
                "You already have a vendor profile."
            )
        return attrs
