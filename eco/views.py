from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Avg
from decimal import Decimal
from .models import (
    Product, Category, UserProfile, Cart, CartItem,
    Order, OrderItem, Review, Vendor
)
from .forms import (
    UserRegistrationForm, UserLoginForm, UserProfileForm,
    ProductForm, ReviewForm, CheckoutForm, VendorRegistrationForm
)


def home(request):
    """Homepage view"""
    featured_products = Product.objects.filter(is_active=True, featured=True)[:6]
    categories = Category.objects.all()[:8]
    latest_products = Product.objects.filter(is_active=True).order_by('-created_at')[:8]

    context = {
        'featured_products': featured_products,
        'categories': categories,
        'latest_products': latest_products,
    }
    return render(request, 'eco/home.html', context)


def product_list(request):
    """Product listing with filters"""
    products = Product.objects.filter(is_active=True)

    # Category filter
    category_slug = request.GET.get('category')
    if category_slug:
        products = products.filter(category__slug=category_slug)

    # Search
    search_query = request.GET.get('search')
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    # Environmental rating filter
    rating = request.GET.get('rating')
    if rating:
        products = products.filter(environmental_rating=rating)

    # Sustainability filters
    if request.GET.get('recyclable') == 'on':
        products = products.filter(recyclable=True)
    if request.GET.get('biodegradable') == 'on':
        products = products.filter(biodegradable=True)

    # Sorting
    sort_by = request.GET.get('sort', '-created_at')
    products = products.order_by(sort_by)

    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories,
        'current_category': category_slug,
    }
    return render(request, 'eco/product_list.html', context)


def product_detail(request, slug):
    """Product detail view"""
    product = get_object_or_404(Product, slug=slug, is_active=True)

    # Increment views
    product.views += 1
    product.save(update_fields=['views'])

    reviews = product.reviews.all().order_by('-created_at')
    related_products = Product.objects.filter(
        category=product.category,
        is_active=True
    ).exclude(id=product.id)[:4]

    # Check if user already reviewed
    user_review = None
    if request.user.is_authenticated:
        user_review = reviews.filter(user=request.user).first()

    context = {
        'product': product,
        'reviews': reviews,
        'related_products': related_products,
        'user_review': user_review,
    }
    return render(request, 'eco/product_detail.html', context)


@login_required
def add_review(request, slug):
    """Add product review"""
    product = get_object_or_404(Product, slug=slug)

    # Check if user already reviewed
    if Review.objects.filter(product=product, user=request.user).exists():
        messages.warning(request, 'You have already reviewed this product.')
        return redirect('product_detail', slug=slug)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, 'Review added successfully!')
            return redirect('product_detail', slug=slug)
    else:
        form = ReviewForm()

    context = {
        'form': form,
        'product': product,
    }
    return render(request, 'eco/add_review.html', context)


def register(request):
    """User registration"""
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create user profile
            UserProfile.objects.create(user=user)
            # Create cart
            Cart.objects.create(user=user)
            login(request, user)
            messages.success(request, 'Registration successful! Welcome to EcoTech Hub!')
            return redirect('profile_setup')
    else:
        form = UserRegistrationForm()

    return render(request, 'eco/register.html', {'form': form})


def user_login(request):
    """User login"""
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.username}!')
                next_url = request.GET.get('next', 'home')
                return redirect(next_url)
    else:
        form = UserLoginForm()

    return render(request, 'eco/login.html', {'form': form})


@login_required
def user_logout(request):
    """User logout"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')


@login_required
def profile(request):
    """User profile view"""
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    orders = Order.objects.filter(user=request.user).order_by('-created_at')[:5]

    context = {
        'profile': profile,
        'orders': orders,
    }
    return render(request, 'eco/profile.html', context)


@login_required
def profile_setup(request):
    """Profile setup after registration"""
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('home')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'eco/profile_setup.html', {'form': form})


@login_required
def edit_profile(request):
    """Edit user profile"""
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'eco/edit_profile.html', {'form': form})


@login_required
def cart_view(request):
    """Shopping cart view"""
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.all()

    context = {
        'cart': cart,
        'cart_items': cart_items,
    }
    return render(request, 'eco/cart.html', context)


@login_required
def add_to_cart(request, product_id):
    """Add product to cart"""
    product = get_object_or_404(Product, id=product_id, is_active=True)
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Check stock
    if product.stock < 1:
        messages.error(request, 'Product is out of stock.')
        return redirect('product_detail', slug=product.slug)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        if cart_item.quantity < product.stock:
            cart_item.quantity += 1
            cart_item.save()
            messages.success(request, f'Updated {product.name} quantity in cart.')
        else:
            messages.warning(request, 'Cannot add more items. Stock limit reached.')
    else:
        messages.success(request, f'{product.name} added to cart!')

    return redirect(request.META.get('HTTP_REFERER', 'cart'))


@login_required
def update_cart(request, item_id):
    """Update cart item quantity"""
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0 and quantity <= cart_item.product.stock:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, 'Cart updated successfully.')
        elif quantity > cart_item.product.stock:
            messages.warning(request, 'Quantity exceeds available stock.')
        else:
            messages.error(request, 'Invalid quantity.')

    return redirect('cart')


@login_required
def remove_from_cart(request, item_id):
    """Remove item from cart"""
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    product_name = cart_item.product.name
    cart_item.delete()
    messages.success(request, f'{product_name} removed from cart.')
    return redirect('cart')


@login_required
def checkout(request):
    """Checkout view"""
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = cart.items.all()

    if not cart_items:
        messages.warning(request, 'Your cart is empty.')
        return redirect('cart')

    # Get user profile for default shipping info
    profile = getattr(request.user, 'profile', None)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Create order
            order = form.save(commit=False)
            order.user = request.user
            order.subtotal = cart.total_price
            order.shipping_cost = Decimal('10.00')  # Fixed shipping cost
            order.tax = cart.total_price * Decimal('0.08')  # 8% tax
            order.total = order.subtotal + order.shipping_cost + order.tax

            # Calculate carbon offset
            order.total_carbon_offset = sum(
                item.product.carbon_footprint * item.quantity
                for item in cart_items
            )
            order.save()

            # Create order items
            for cart_item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                    price=cart_item.product.price
                )
                # Update product stock
                cart_item.product.stock -= cart_item.quantity
                cart_item.product.save()

            # Clear cart
            cart_items.delete()

            # Update user's carbon offset
            if profile:
                profile.carbon_offset += order.total_carbon_offset
                profile.save()

            messages.success(request, f'Order {order.order_number} placed successfully!')
            return redirect('order_detail', order_number=order.order_number)
    else:
        initial_data = {}
        if profile:
            initial_data = {
                'shipping_address': profile.address,
                'shipping_city': profile.city,
                'shipping_state': profile.state,
                'shipping_zip': profile.zip_code,
                'shipping_country': profile.country,
            }
        form = CheckoutForm(initial=initial_data)

    context = {
        'form': form,
        'cart': cart,
        'cart_items': cart_items,
    }
    return render(request, 'eco/checkout.html', context)


@login_required
def order_detail(request, order_number):
    """Order detail view"""
    order = get_object_or_404(Order, order_number=order_number, user=request.user)
    context = {
        'order': order,
    }
    return render(request, 'eco/order_detail.html', context)


@login_required
def order_history(request):
    """Order history view"""
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'orders': orders,
    }
    return render(request, 'eco/order_history.html', context)


@login_required
def vendor_register(request):
    """Vendor registration"""
    if hasattr(request.user, 'vendor'):
        messages.warning(request, 'You are already registered as a vendor.')
        return redirect('vendor_dashboard')

    if request.method == 'POST':
        form = VendorRegistrationForm(request.POST)
        if form.is_valid():
            vendor = form.save(commit=False)
            vendor.user = request.user
            vendor.save()
            messages.success(request, 'Vendor registration successful! Awaiting verification.')
            return redirect('vendor_dashboard')
    else:
        form = VendorRegistrationForm()

    return render(request, 'eco/vendor_register.html', {'form': form})


@login_required
def vendor_dashboard(request):
    """Vendor dashboard"""
    try:
        vendor = request.user.vendor
    except Vendor.DoesNotExist:
        messages.warning(request, 'Please register as a vendor first.')
        return redirect('vendor_register')

    products = vendor.products.all()
    recent_orders = OrderItem.objects.filter(product__vendor=vendor).order_by('-order__created_at')[:10]

    context = {
        'vendor': vendor,
        'products': products,
        'recent_orders': recent_orders,
    }
    return render(request, 'eco/vendor_dashboard.html', context)


@login_required
def vendor_add_product(request):
    """Add product (vendor)"""
    try:
        vendor = request.user.vendor
    except Vendor.DoesNotExist:
        messages.warning(request, 'Please register as a vendor first.')
        return redirect('vendor_register')

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = vendor
            product.save()
            messages.success(request, 'Product added successfully!')
            return redirect('vendor_dashboard')
    else:
        form = ProductForm()

    return render(request, 'eco/vendor_add_product.html', {'form': form})


@login_required
def vendor_edit_product(request, product_id):
    """Edit product (vendor)"""
    try:
        vendor = request.user.vendor
    except Vendor.DoesNotExist:
        messages.warning(request, 'Access denied.')
        return redirect('home')

    product = get_object_or_404(Product, id=product_id, vendor=vendor)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('vendor_dashboard')
    else:
        form = ProductForm(instance=product)

    context = {
        'form': form,
        'product': product,
    }
    return render(request, 'eco/vendor_edit_product.html', context)


def about(request):
    """About page"""
    return render(request, 'eco/about.html')


def contact(request):
    """Contact page"""
    return render(request, 'eco/contact.html')
