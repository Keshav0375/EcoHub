from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Vendor(models.Model):
    VERIFICATION_STATUS = [
        ('pending', 'Pending'),
        ('verified', 'Verified'),
        ('rejected', 'Rejected'),
        ('suspended', 'Suspended'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='vendor_profile')
    company_name = models.CharField(max_length=200)
    business_license = models.CharField(max_length=100)
    tax_id = models.CharField(max_length=50)
    
    # Contact details
    business_address = models.TextField()
    contact_phone = models.CharField(max_length=15)
    website = models.URLField(blank=True)
    
    # Verification and compliance
    verification_status = models.CharField(max_length=20, choices=VERIFICATION_STATUS, default='pending')
    sustainability_certificate = models.FileField(upload_to='vendor_certificates/', blank=True)
    verification_documents = models.FileField(upload_to='vendor_docs/', blank=True)
    
    # Business metrics
    rating = models.FloatField(default=0.0)
    total_sales = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    eco_impact_score = models.FloatField(default=0.0)  # Calculated based on products sold
    
    # Profile details
    description = models.TextField()
    logo = models.ImageField(upload_to='vendor_logos/', blank=True)
    banner_image = models.ImageField(upload_to='vendor_banners/', blank=True)
    
    # Settings
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name

    @property
    def is_verified(self):
        return self.verification_status == 'verified'