from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPES = [
        ('consumer', 'Consumer'),
        ('vendor', 'Vendor'),
        ('admin', 'Admin'),
    ]
    
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='consumer')
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    sustainability_goals = models.TextField(blank=True)
    carbon_footprint_target = models.FloatField(null=True, blank=True)
    email_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username} ({self.user_type})"