from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from products.models import Category, Product, ProductImage
from vendors.models import Vendor
from reviews.models import Review
from django.utils.text import slugify
import random
from decimal import Decimal

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate database with sample sustainable tech products'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')
        
        # Create admin user if doesn't exist
        if not User.objects.filter(username='admin').exists():
            admin = User.objects.create_superuser(
                username='admin',
                email='admin@ecohub.com',
                password='admin123',
                user_type='admin'
            )
            self.stdout.write('Created admin user: admin/admin123')
        
        # Create sample vendors
        vendors_data = [
            {
                'username': 'greenenergy_co',
                'email': 'contact@greenenergy.com',
                'company_name': 'GreenEnergy Solutions',
                'description': 'Leading provider of solar and renewable energy solutions.',
                'verification_status': 'verified'
            },
            {
                'username': 'ecotech_innovations',
                'email': 'info@ecotech.com',
                'company_name': 'EcoTech Innovations',
                'description': 'Smart home and energy efficiency experts.',
                'verification_status': 'verified'
            },
            {
                'username': 'sustainable_living',
                'email': 'hello@sustainableliving.com',
                'company_name': 'Sustainable Living Co',
                'description': 'Eco-friendly products for modern homes.',
                'verification_status': 'verified'
            }
        ]

        vendors = []
        for vendor_data in vendors_data:
            if not User.objects.filter(username=vendor_data['username']).exists():
                user = User.objects.create_user(
                    username=vendor_data['username'],
                    email=vendor_data['email'],
                    password='vendor123',
                    user_type='vendor',
                    first_name=vendor_data['company_name'].split()[0],
                    last_name='Team'
                )
                
                vendor = Vendor.objects.create(
                    user=user,
                    company_name=vendor_data['company_name'],
                    business_license=f"BL{random.randint(100000, 999999)}",
                    tax_id=f"TX{random.randint(100000, 999999)}",
                    business_address="123 Green Street, Eco City, EC 12345",
                    contact_phone=f"555-{random.randint(1000, 9999)}",
                    website=f"https://{vendor_data['username']}.com",
                    verification_status=vendor_data['verification_status'],
                    description=vendor_data['description'],
                    rating=round(random.uniform(4.0, 5.0), 1),
                    eco_impact_score=round(random.uniform(85, 98), 1)
                )
                vendors.append(vendor)
                self.stdout.write(f'Created vendor: {vendor.company_name}')

        # Get all vendors (including any existing ones)
        all_vendors = list(Vendor.objects.all())
        
        # Create categories
        categories_data = [
            {'name': 'Solar Energy', 'description': 'Solar panels, inverters, and solar accessories', 'icon': 'fas fa-sun'},
            {'name': 'Smart Home', 'description': 'Smart thermostats, lighting, and home automation', 'icon': 'fas fa-home'},
            {'name': 'Energy Storage', 'description': 'Batteries and energy storage solutions', 'icon': 'fas fa-battery-full'},
            {'name': 'Electric Vehicles', 'description': 'EV chargers and electric mobility solutions', 'icon': 'fas fa-car'},
            {'name': 'LED Lighting', 'description': 'Energy-efficient LED lighting solutions', 'icon': 'fas fa-lightbulb'},
            {'name': 'Water Conservation', 'description': 'Water-saving devices and filtration systems', 'icon': 'fas fa-tint'},
            {'name': 'Heating & Cooling', 'description': 'Energy-efficient HVAC systems', 'icon': 'fas fa-thermometer-half'},
            {'name': 'Wind Energy', 'description': 'Small wind turbines and wind accessories', 'icon': 'fas fa-wind'},
        ]

        categories = []
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={
                    'description': cat_data['description'],
                    'icon': cat_data['icon']
                }
            )
            categories.append(category)
            if created:
                self.stdout.write(f'Created category: {category.name}')

        # Create products
        products_data = [
            # Solar Energy Products
            {
                'name': 'EcoSolar Premium 400W Monocrystalline Panel',
                'category': 'Solar Energy',
                'price': 299.99,
                'energy_efficiency_rating': 'A++',
                'carbon_footprint': 45.2,
                'energy_consumption': 0,
                'recyclable_percentage': 95,
                'certifications': 'energy_star',
                'warranty_years': 25,
                'description': 'High-efficiency monocrystalline solar panel with 400W output. Perfect for residential installations with excellent performance in low-light conditions.'
            },
            {
                'name': 'SolarMax 300W Polycrystalline Panel',
                'category': 'Solar Energy',
                'price': 199.99,
                'energy_efficiency_rating': 'A+',
                'carbon_footprint': 52.1,
                'energy_consumption': 0,
                'recyclable_percentage': 90,
                'certifications': 'leed',
                'warranty_years': 20,
                'description': 'Reliable polycrystalline solar panel offering excellent value for money. Ideal for budget-conscious solar installations.'
            },
            
            # Smart Home Products
            {
                'name': 'EcoTherm Smart Wi-Fi Thermostat',
                'category': 'Smart Home',
                'price': 249.99,
                'energy_efficiency_rating': 'A++',
                'carbon_footprint': 12.5,
                'energy_consumption': 240,
                'recyclable_percentage': 80,
                'certifications': 'energy_star',
                'warranty_years': 5,
                'description': 'Smart thermostat with learning capabilities, geofencing, and energy usage reports. Can save up to 23% on heating and cooling costs.'
            },
            {
                'name': 'SmartHome Energy Monitor Pro',
                'category': 'Smart Home',
                'price': 199.99,
                'energy_efficiency_rating': 'A+',
                'carbon_footprint': 8.3,
                'energy_consumption': 12,
                'recyclable_percentage': 85,
                'certifications': 'epeat',
                'warranty_years': 3,
                'description': 'Real-time whole-home energy monitoring system with mobile app. Track your energy usage by device and optimize consumption.'
            },
            
            # Energy Storage
            {
                'name': 'PowerVault 10kWh Home Battery System',
                'category': 'Energy Storage',
                'price': 8999.99,
                'energy_efficiency_rating': 'A++',
                'carbon_footprint': 125.7,
                'energy_consumption': 0,
                'recyclable_percentage': 95,
                'certifications': 'leed',
                'warranty_years': 10,
                'description': 'Lithium-ion home battery storage system with 10kWh capacity. Store solar energy for use during peak hours or power outages.'
            },
            
            # Electric Vehicles
            {
                'name': 'ChargePro Level 2 EV Charger 32A',
                'category': 'Electric Vehicles',
                'price': 599.99,
                'energy_efficiency_rating': 'A+',
                'carbon_footprint': 18.9,
                'energy_consumption': 7680,
                'recyclable_percentage': 88,
                'certifications': 'energy_star',
                'warranty_years': 3,
                'description': 'High-speed Level 2 EV charger with 32A output. Charges most electric vehicles 6x faster than standard outlets.'
            },
            
            # LED Lighting
            {
                'name': 'EcoGlow Smart LED Bulb Set (4-pack)',
                'category': 'LED Lighting',
                'price': 79.99,
                'energy_efficiency_rating': 'A++',
                'carbon_footprint': 2.1,
                'energy_consumption': 36,
                'recyclable_percentage': 75,
                'certifications': 'energy_star',
                'warranty_years': 15,
                'description': 'Smart LED bulbs with color changing, dimming, and scheduling features. Each bulb uses only 9W while producing 800 lumens.'
            },
            {
                'name': 'Industrial LED High Bay Light 150W',
                'category': 'LED Lighting',
                'price': 189.99,
                'energy_efficiency_rating': 'A+',
                'carbon_footprint': 15.4,
                'energy_consumption': 150,
                'recyclable_percentage': 90,
                'certifications': 'epeat',
                'warranty_years': 10,
                'description': 'Commercial-grade LED high bay light perfect for warehouses and industrial spaces. 150W replaces 400W traditional lighting.'
            },
            
            # Water Conservation
            {
                'name': 'AquaSave Low-Flow Showerhead',
                'category': 'Water Conservation',
                'price': 49.99,
                'energy_efficiency_rating': 'A',
                'carbon_footprint': 3.2,
                'energy_consumption': 0,
                'recyclable_percentage': 70,
                'certifications': 'renewable',
                'warranty_years': 5,
                'description': 'High-pressure, low-flow showerhead that reduces water usage by 40% while maintaining excellent shower experience.'
            },
            
            # Heating & Cooling
            {
                'name': 'EcoHeat Mini-Split Heat Pump 12k BTU',
                'category': 'Heating & Cooling',
                'price': 1299.99,
                'energy_efficiency_rating': 'A++',
                'carbon_footprint': 85.6,
                'energy_consumption': 1200,
                'recyclable_percentage': 85,
                'certifications': 'energy_star',
                'warranty_years': 7,
                'description': 'Ductless mini-split heat pump system with inverter technology. Provides efficient heating and cooling year-round.'
            },
            
            # Wind Energy
            {
                'name': 'WindTech Residential 1kW Wind Turbine',
                'category': 'Wind Energy',
                'price': 2499.99,
                'energy_efficiency_rating': 'A',
                'carbon_footprint': 95.3,
                'energy_consumption': 0,
                'recyclable_percentage': 92,
                'certifications': 'renewable',
                'warranty_years': 15,
                'description': 'Compact residential wind turbine designed for low-wind areas. Generates clean energy with minimal noise and vibration.'
            }
        ]

        for product_data in products_data:
            if not all_vendors:
                self.stdout.write('No vendors available. Creating products without vendors.')
                continue
                
            category = Category.objects.get(name=product_data['category'])
            vendor = random.choice(all_vendors)
            
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults={
                    'description': product_data['description'],
                    'category': category,
                    'vendor': vendor,
                    'price': Decimal(str(product_data['price'])),
                    'discounted_price': Decimal(str(product_data['price'] * 0.9)) if random.choice([True, False]) else None,
                    'energy_efficiency_rating': product_data['energy_efficiency_rating'],
                    'carbon_footprint': product_data['carbon_footprint'],
                    'energy_consumption': product_data['energy_consumption'],
                    'recyclable_percentage': product_data['recyclable_percentage'],
                    'certifications': product_data['certifications'],
                    'warranty_years': product_data['warranty_years'],
                    'availability': random.randint(5, 50),
                    'slug': slugify(product_data['name']),
                    'is_featured': random.choice([True, False]),
                    'specifications': {
                        'weight': f"{random.randint(1, 50)} lbs",
                        'dimensions': f"{random.randint(10, 50)}x{random.randint(10, 50)}x{random.randint(5, 20)} inches",
                        'color': random.choice(['Black', 'White', 'Silver', 'Blue']),
                        'installation': random.choice(['Professional Required', 'DIY Friendly', 'Plug and Play'])
                    }
                }
            )
            
            if created:
                self.stdout.write(f'Created product: {product.name}')

        # Create some sample users for reviews
        consumer_users = []
        for i in range(5):
            username = f'consumer_{i+1}'
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(
                    username=username,
                    email=f'consumer{i+1}@example.com',
                    password='consumer123',
                    user_type='consumer',
                    first_name=f'Consumer{i+1}',
                    last_name='User'
                )
                consumer_users.append(user)

        # Create some sample reviews
        all_products = list(Product.objects.all())
        all_consumers = list(User.objects.filter(user_type='consumer'))
        
        review_templates = [
            {
                'title': 'Excellent product quality!',
                'comment': 'Really impressed with the build quality and energy savings. Installation was straightforward and customer service was helpful.',
                'environmental_impact_notes': 'Noticed a 20% reduction in energy bills within the first month.'
            },
            {
                'title': 'Good value for money',
                'comment': 'Does exactly what it promises. The environmental benefits are clear and the payback period is reasonable.',
                'environmental_impact_notes': 'Carbon footprint reduced significantly as expected.'
            },
            {
                'title': 'Highly recommend',
                'comment': 'Amazing product that exceeded expectations. The smart features work flawlessly and the app is user-friendly.',
                'environmental_impact_notes': 'Energy consumption dropped by 30% since installation.'
            }
        ]

        if all_products and all_consumers:
            for _ in range(min(20, len(all_products) * 2)):  # Create up to 20 reviews
                product = random.choice(all_products)
                user = random.choice(all_consumers)
                
                # Check if review already exists
                if not Review.objects.filter(user=user, product=product).exists():
                    review_template = random.choice(review_templates)
                    
                    Review.objects.create(
                        user=user,
                        product=product,
                        overall_rating=random.randint(4, 5),
                        eco_impact_rating=random.randint(4, 5),
                        value_for_money=random.randint(3, 5),
                        build_quality=random.randint(4, 5),
                        title=review_template['title'],
                        comment=review_template['comment'],
                        environmental_impact_notes=review_template['environmental_impact_notes'],
                        actual_energy_savings=random.uniform(50, 200),
                        would_recommend=True,
                        is_verified_purchase=random.choice([True, False]),
                        is_approved=True,
                        helpful_votes=random.randint(0, 15)
                    )

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created sample data!\n'
                f'- Categories: {Category.objects.count()}\n'
                f'- Vendors: {Vendor.objects.count()}\n'
                f'- Products: {Product.objects.count()}\n'
                f'- Reviews: {Review.objects.count()}\n'
                f'- Users: {User.objects.count()}\n\n'
                f'Login credentials:\n'
                f'Admin: admin / admin123\n'
                f'Vendors: greenenergy_co / vendor123 (and others)\n'
                f'Consumers: consumer_1 / consumer123 (and others)'
            )
        )