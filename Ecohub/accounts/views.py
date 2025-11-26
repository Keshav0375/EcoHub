from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from .serializers import (
    CustomTokenObtainPairSerializer,
    RegisterSerializer,
    UserProfileSerializer,
    ChangePasswordSerializer
)

User = get_user_model()

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': UserProfileSerializer(user).data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'message': 'User created successfully'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            if user.check_password(serializer.validated_data['old_password']):
                user.set_password(serializer.validated_data['new_password'])
                user.save()
                return Response({"message": "Password changed successfully"}, status=status.HTTP_200_OK)
            return Response({"error": "Invalid old password"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyEmailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user
        user.email_verified = True
        user.save()
        return Response({"message": "Email verified successfully"}, status=status.HTTP_200_OK)


# Web Views for Template-based Authentication
def login_view(request):
    """Web view for login page"""
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')

        # Try to authenticate
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)

            # Set session expiry
            if not remember:
                request.session.set_expiry(0)  # Session expires on browser close

            messages.success(request, f'Welcome back, {user.get_full_name() or user.username}!')

            # Redirect to next page or home
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
        else:
            # Check if user exists with this email
            try:
                user_by_email = User.objects.get(email=username)
                user = authenticate(request, username=user_by_email.username, password=password)
                if user:
                    auth_login(request, user)
                    if not remember:
                        request.session.set_expiry(0)
                    messages.success(request, f'Welcome back, {user.get_full_name() or user.username}!')
                    next_url = request.GET.get('next', 'home')
                    return redirect(next_url)
            except User.DoesNotExist:
                pass

            return render(request, 'accounts/login.html', {
                'error': 'Invalid username/email or password. Please try again.'
            })

    return render(request, 'accounts/login.html')


def register_view(request):
    """Web view for registration page"""
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        # Get form data
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user_type = request.POST.get('user_type', 'consumer')
        phone = request.POST.get('phone', '')

        errors = []

        # Validate passwords match
        if password != password2:
            errors.append('Passwords do not match')

        # Validate password strength
        if len(password) < 8:
            errors.append('Password must be at least 8 characters long')

        # Check if username exists
        if User.objects.filter(username=username).exists():
            errors.append('Username already exists')

        # Check if email exists
        if User.objects.filter(email=email).exists():
            errors.append('Email already registered')

        # Validate password using Django validators
        try:
            validate_password(password)
        except DjangoValidationError as e:
            errors.extend(e.messages)

        if errors:
            return render(request, 'accounts/register.html', {
                'errors': errors
            })

        # Create user
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                user_type=user_type,
                phone=phone
            )

            # Auto login after registration
            # Specify the backend to avoid multiple backend error
            auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')

            messages.success(request, 'Account created successfully! Welcome to EcoTech Hub!')
            return redirect('home')

        except Exception as e:
            return render(request, 'accounts/register.html', {
                'errors': [f'Error creating account: {str(e)}']
            })

    return render(request, 'accounts/register.html')


def logout_view(request):
    """Web view for logout"""
    auth_logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('home')


@login_required
def profile_view(request):
    """Web view for user profile"""
    return render(request, 'accounts/profile.html', {
        'user': request.user
    })