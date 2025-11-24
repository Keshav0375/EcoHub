from rest_framework import serializers
from .models import Review
from accounts.serializers import UserProfileSerializer


class ReviewSerializer(serializers.ModelSerializer):
    """Serializer for review with full details"""
    user = UserProfileSerializer(read_only=True)
    average_rating = serializers.FloatField(read_only=True)
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = Review
        fields = [
            'id', 'user', 'product', 'product_name',
            'overall_rating', 'eco_impact_rating', 'value_for_money', 'build_quality',
            'average_rating', 'title', 'comment',
            'actual_energy_savings', 'environmental_impact_notes', 'would_recommend',
            'is_verified_purchase', 'is_approved', 'helpful_votes',
            'created_at', 'updated_at'
        ]
        read_only_fields = [
            'id', 'user', 'is_verified_purchase', 'is_approved',
            'helpful_votes', 'created_at', 'updated_at'
        ]

    def validate(self, attrs):
        """Validate that ratings are within range"""
        ratings = [
            attrs.get('overall_rating'),
            attrs.get('eco_impact_rating'),
            attrs.get('value_for_money'),
            attrs.get('build_quality')
        ]

        for rating in ratings:
            if rating and (rating < 1 or rating > 5):
                raise serializers.ValidationError(
                    "All ratings must be between 1 and 5"
                )

        return attrs

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class ReviewListSerializer(serializers.ModelSerializer):
    """Lighter serializer for review lists"""
    user_username = serializers.CharField(source='user.username', read_only=True)
    average_rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Review
        fields = [
            'id', 'user_username', 'product',
            'overall_rating', 'eco_impact_rating', 'average_rating',
            'title', 'would_recommend', 'is_verified_purchase',
            'helpful_votes', 'created_at'
        ]


class ReviewCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating a review"""

    class Meta:
        model = Review
        fields = [
            'product', 'overall_rating', 'eco_impact_rating',
            'value_for_money', 'build_quality', 'title', 'comment',
            'actual_energy_savings', 'environmental_impact_notes',
            'would_recommend'
        ]

    def validate(self, attrs):
        """Check if user has already reviewed this product"""
        user = self.context['request'].user
        product = attrs.get('product')

        if Review.objects.filter(user=user, product=product).exists():
            raise serializers.ValidationError(
                "You have already reviewed this product."
            )

        return attrs

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
