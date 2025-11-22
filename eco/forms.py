from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile, Product, Review, Vendor, Order


class UserRegistrationForm(UserCreationForm):
    """User registration form with additional fields"""
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email address'
        })
    )
    first_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'First name'
        })
    )
    last_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Last name'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm password'
        })


class UserLoginForm(AuthenticationForm):
    """Custom login form"""
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )


class UserProfileForm(forms.ModelForm):
    """User profile form"""
    class Meta:
        model = UserProfile
        fields = ['phone', 'address', 'city', 'state', 'zip_code', 'country', 'sustainability_goal']
        widgets = {
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone number'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Street address',
                'rows': 3
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'City'
            }),
            'state': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'State/Province'
            }),
            'zip_code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ZIP/Postal code'
            }),
            'country': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Country'
            }),
            'sustainability_goal': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Share your sustainability goals and commitments',
                'rows': 4
            }),
        }


class VendorRegistrationForm(forms.ModelForm):
    """Vendor registration form"""
    class Meta:
        model = Vendor
        fields = ['company_name', 'description', 'phone', 'email', 'address', 'website', 'sustainability_certification']
        widgets = {
            'company_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Company name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe your company and sustainability practices',
                'rows': 4
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Business phone'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Business email'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Business address',
                'rows': 3
            }),
            'website': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Website URL (optional)'
            }),
            'sustainability_certification': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Certifications (e.g., B-Corp, Fair Trade)'
            }),
        }


class ProductForm(forms.ModelForm):
    """Product creation/update form"""
    class Meta:
        model = Product
        fields = [
            'category', 'name', 'description', 'price', 'stock', 'image',
            'environmental_rating', 'carbon_footprint', 'energy_efficiency',
            'recyclable', 'biodegradable', 'sustainable_materials', 'featured'
        ]
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Product name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Product description',
                'rows': 5
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Price',
                'step': '0.01'
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Available stock'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
            'environmental_rating': forms.Select(attrs={'class': 'form-control'}),
            'carbon_footprint': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Carbon footprint (kg CO2)',
                'step': '0.01'
            }),
            'energy_efficiency': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Energy rating (e.g., A+++)'
            }),
            'recyclable': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'biodegradable': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'sustainable_materials': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'List sustainable materials used',
                'rows': 3
            }),
            'featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class ReviewForm(forms.ModelForm):
    """Product review form"""
    class Meta:
        model = Review
        fields = ['rating', 'title', 'comment']
        widgets = {
            'rating': forms.Select(
                choices=[(i, f'{i} Star{"s" if i != 1 else ""}') for i in range(1, 6)],
                attrs={'class': 'form-control'}
            ),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Review title'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Share your experience with this product',
                'rows': 4
            }),
        }


class CheckoutForm(forms.ModelForm):
    """Checkout form for order"""
    class Meta:
        model = Order
        fields = ['shipping_address', 'shipping_city', 'shipping_state', 'shipping_zip', 'shipping_country', 'notes']
        widgets = {
            'shipping_address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Street address',
                'rows': 3
            }),
            'shipping_city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'City'
            }),
            'shipping_state': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'State/Province'
            }),
            'shipping_zip': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ZIP/Postal code'
            }),
            'shipping_country': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Country'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Order notes (optional)',
                'rows': 3
            }),
        }
