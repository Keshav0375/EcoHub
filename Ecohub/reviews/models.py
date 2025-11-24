from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from products.models import Product

User = get_user_model()

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    
    # Rating system
    overall_rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    eco_impact_rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    value_for_money = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    build_quality = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    
    # Review content
    title = models.CharField(max_length=200)
    comment = models.TextField()
    
    # Environmental feedback
    actual_energy_savings = models.FloatField(null=True, blank=True, help_text="kWh saved per month")
    environmental_impact_notes = models.TextField(blank=True)
    would_recommend = models.BooleanField(default=True)
    
    # Verification and moderation
    is_verified_purchase = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    helpful_votes = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'product')  # One review per user per product
        ordering = ['-created_at']

    def __str__(self):
        return f"Review by {self.user.username} for {self.product.name}"

    @property
    def average_rating(self):
        return (self.overall_rating + self.eco_impact_rating + self.value_for_money + self.build_quality) / 4