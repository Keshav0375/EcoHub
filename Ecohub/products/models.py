from django.db import models
from django.contrib.auth import get_user_model
from vendors.models import Vendor

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    icon = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    CERTIFICATION_CHOICES = [
        ('energy_star', 'Energy Star'),
        ('leed', 'LEED Certified'),
        ('epeat', 'EPEAT Gold'),
        ('carbon_neutral', 'Carbon Neutral'),
        ('renewable', 'Renewable Energy'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='products')
    
    # Pricing
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    # Environmental metrics
    energy_efficiency_rating = models.CharField(max_length=5)  # A++, A+, A, B, C, D, E
    carbon_footprint = models.FloatField(help_text="CO2 emissions in kg/year")
    energy_consumption = models.FloatField(help_text="Energy consumption in kWh/year")
    recyclable_percentage = models.IntegerField(default=0)
    certifications = models.CharField(max_length=50, choices=CERTIFICATION_CHOICES, blank=True)
    
    # Product details
    specifications = models.JSONField(default=dict)
    warranty_years = models.IntegerField(default=1)
    availability = models.IntegerField(default=0)  # Stock quantity
    
    # SEO and management
    slug = models.SlugField(max_length=250, unique=True)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def final_price(self):
        return self.discounted_price if self.discounted_price else self.price

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')
    alt_text = models.CharField(max_length=200)
    is_primary = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.product.name}"