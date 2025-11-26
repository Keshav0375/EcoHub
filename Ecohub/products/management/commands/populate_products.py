from django.core.management.base import BaseCommand
from django.utils.text import slugify
from products.models import Product, Category, ProductImage
from vendors.models import Vendor
from accounts.models import User


class Command(BaseCommand):
    help = 'Populate database with sample eco-friendly products with Unsplash images'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting to populate database...')

        # Create or get admin user
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@ecohub.com',
                'user_type': 'vendor',
                'is_staff': True,
                'is_superuser': True
            }
        )
        if created:
            admin_user.set_password('admin123')
            admin_user.save()
            self.stdout.write(self.style.SUCCESS('Created admin user'))

        # Create sample vendor
        vendor, created = Vendor.objects.get_or_create(
            user=admin_user,
            defaults={
                'company_name': 'EcoTech Solutions',
                'business_license': 'ECO-12345',
                'tax_id': 'TAX-67890',
                'business_address': '123 Green Street, Eco City, EC 12345',
                'contact_phone': '+1-555-ECO-TECH',
                'website': 'https://ecotech-solutions.example.com',
                'description': 'Leading provider of sustainable technology solutions for homes and businesses.',
                'verification_status': 'verified',
                'rating': 4.8,
                'eco_impact_score': 95.5
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created vendor: {vendor.company_name}'))

        # Create categories
        categories_data = [
            {
                'name': 'Solar Panels',
                'description': 'High-efficiency solar energy solutions',
                'icon': 'solar-panel'
            },
            {
                'name': 'Smart Home',
                'description': 'Energy-efficient smart home devices',
                'icon': 'home'
            },
            {
                'name': 'LED Lighting',
                'description': 'Energy-saving LED light solutions',
                'icon': 'lightbulb'
            },
            {
                'name': 'Appliances',
                'description': 'Eco-friendly home appliances',
                'icon': 'blender'
            },
            {
                'name': 'Electric Vehicles',
                'description': 'Sustainable transportation solutions',
                'icon': 'car-battery'
            }
        ]

        categories = {}
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults=cat_data
            )
            categories[cat_data['name']] = category
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created category: {category.name}'))

        # Sample products with Unsplash images
        products_data = [
            {
                'name': 'Premium Solar Panel 400W',
                'category': categories['Solar Panels'],
                'description': 'High-efficiency monocrystalline solar panel with 22% efficiency rating. Perfect for residential installations.',
                'price': 299.99,
                'discounted_price': 249.99,
                'energy_efficiency_rating': 'A++',
                'carbon_footprint': 15.5,
                'energy_consumption': 0,
                'recyclable_percentage': 95,
                'certifications': 'energy_star',
                'warranty_years': 25,
                'availability': 50,
                'is_featured': True,
                'images': [
                    {
                        'url': 'https://images.unsplash.com/photo-1509391366360-2e959784a276?w=800',
                        'alt_text': 'Solar panels on roof'
                    }
                ]
            },
            {
                'name': 'Smart Thermostat Pro',
                'category': categories['Smart Home'],
                'description': 'AI-powered smart thermostat that learns your schedule and reduces energy consumption by up to 30%.',
                'price': 199.99,
                'discounted_price': 159.99,
                'energy_efficiency_rating': 'A+',
                'carbon_footprint': 8.2,
                'energy_consumption': 50,
                'recyclable_percentage': 85,
                'certifications': 'energy_star',
                'warranty_years': 3,
                'availability': 100,
                'is_featured': True,
                'images': [
                    {
                        'url': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800',
                        'alt_text': 'Smart thermostat on wall'
                    }
                ]
            },
            {
                'name': 'LED Smart Bulb 4-Pack',
                'category': categories['LED Lighting'],
                'description': 'Color-changing smart LED bulbs with app control. 90% more efficient than traditional bulbs.',
                'price': 49.99,
                'energy_efficiency_rating': 'A++',
                'carbon_footprint': 2.1,
                'energy_consumption': 40,
                'recyclable_percentage': 75,
                'certifications': 'energy_star',
                'warranty_years': 2,
                'availability': 200,
                'is_featured': True,
                'images': [
                    {
                        'url': 'https://images.unsplash.com/photo-1563013544-824ae1b704d3?w=800',
                        'alt_text': 'LED smart bulbs'
                    }
                ]
            },
            {
                'name': 'Energy Star Refrigerator',
                'category': categories['Appliances'],
                'description': 'A++ rated smart refrigerator with advanced cooling technology. Reduces energy consumption by 40%.',
                'price': 1299.99,
                'discounted_price': 1099.99,
                'energy_efficiency_rating': 'A++',
                'carbon_footprint': 120.5,
                'energy_consumption': 320,
                'recyclable_percentage': 90,
                'certifications': 'energy_star',
                'warranty_years': 5,
                'availability': 25,
                'is_featured': True,
                'images': [
                    {
                        'url': 'https://images.unsplash.com/photo-1571175443880-49e1d25b2bc5?w=800',
                        'alt_text': 'Modern refrigerator'
                    }
                ]
            },
            {
                'name': 'Electric Bike Urban Commuter',
                'category': categories['Electric Vehicles'],
                'description': 'Eco-friendly electric bicycle with 50-mile range. Zero emissions commuting solution.',
                'price': 1899.99,
                'discounted_price': 1699.99,
                'energy_efficiency_rating': 'A++',
                'carbon_footprint': 0,
                'energy_consumption': 150,
                'recyclable_percentage': 80,
                'certifications': 'carbon_neutral',
                'warranty_years': 2,
                'availability': 30,
                'is_featured': True,
                'images': [
                    {
                        'url': 'https://images.unsplash.com/photo-1571333250630-f0230c320b6d?w=800',
                        'alt_text': 'Electric bicycle'
                    }
                ]
            },
            {
                'name': 'Portable Solar Charger 50W',
                'category': categories['Solar Panels'],
                'description': 'Foldable solar charger for phones, tablets, and laptops. Perfect for outdoor adventures.',
                'price': 129.99,
                'energy_efficiency_rating': 'A+',
                'carbon_footprint': 3.5,
                'energy_consumption': 0,
                'recyclable_percentage': 85,
                'certifications': 'energy_star',
                'warranty_years': 2,
                'availability': 75,
                'images': [
                    {
                        'url': 'https://images.unsplash.com/photo-1603899122634-f086ca5f5ddd?w=800',
                        'alt_text': 'Portable solar charger'
                    }
                ]
            },
            {
                'name': 'Smart Power Strip',
                'category': categories['Smart Home'],
                'description': 'Intelligent power strip that eliminates vampire power. Saves up to $100 per year on electricity.',
                'price': 39.99,
                'energy_efficiency_rating': 'A',
                'carbon_footprint': 1.8,
                'energy_consumption': 5,
                'recyclable_percentage': 80,
                'certifications': 'energy_star',
                'warranty_years': 1,
                'availability': 150,
                'images': [
                    {
                        'url': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800',
                        'alt_text': 'Smart power strip'
                    }
                ]
            },
            {
                'name': 'LED Desk Lamp with USB',
                'category': categories['LED Lighting'],
                'description': 'Adjustable LED desk lamp with USB charging port. Eye-care technology and energy-saving design.',
                'price': 79.99,
                'discounted_price': 59.99,
                'energy_efficiency_rating': 'A++',
                'carbon_footprint': 1.2,
                'energy_consumption': 12,
                'recyclable_percentage': 75,
                'certifications': 'energy_star',
                'warranty_years': 2,
                'availability': 120,
                'images': [
                    {
                        'url': 'https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=800',
                        'alt_text': 'Modern LED desk lamp'
                    }
                ]
            },
            {
                'name': 'Eco Washing Machine',
                'category': categories['Appliances'],
                'description': 'Front-load washing machine with steam cleaning. Uses 50% less water and energy.',
                'price': 899.99,
                'discounted_price': 799.99,
                'energy_efficiency_rating': 'A++',
                'carbon_footprint': 85.0,
                'energy_consumption': 180,
                'recyclable_percentage': 88,
                'certifications': 'energy_star',
                'warranty_years': 3,
                'availability': 40,
                'images': [
                    {
                        'url': 'https://images.unsplash.com/photo-1626806787461-102c1bfaaea1?w=800',
                        'alt_text': 'Modern washing machine'
                    }
                ]
            },
            {
                'name': 'Solar Garden Lights Set',
                'category': categories['LED Lighting'],
                'description': 'Set of 12 solar-powered garden lights. No wiring needed, automatic on/off.',
                'price': 89.99,
                'energy_efficiency_rating': 'A++',
                'carbon_footprint': 0,
                'energy_consumption': 0,
                'recyclable_percentage': 70,
                'certifications': 'renewable',
                'warranty_years': 1,
                'availability': 200,
                'images': [
                    {
                        'url': 'https://images.unsplash.com/photo-1513506003901-1e6a229e2d15?w=800',
                        'alt_text': 'Solar garden lights'
                    }
                ]
            }
        ]

        # Create products
        for product_data in products_data:
            images_data = product_data.pop('images')
            slug = slugify(product_data['name'])

            product, created = Product.objects.get_or_create(
                slug=slug,
                defaults={
                    **product_data,
                    'vendor': vendor
                }
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Created product: {product.name}'))

                # Add images
                for idx, img_data in enumerate(images_data):
                    ProductImage.objects.create(
                        product=product,
                        image_url=img_data['url'],
                        alt_text=img_data['alt_text'],
                        is_primary=(idx == 0)
                    )
                    self.stdout.write(f'  Added image for {product.name}')

        self.stdout.write(self.style.SUCCESS('\n✅ Database populated successfully!'))
        self.stdout.write(self.style.SUCCESS(f'Created {Product.objects.count()} products'))
        self.stdout.write(self.style.SUCCESS(f'Created {Category.objects.count()} categories'))
        self.stdout.write(self.style.SUCCESS('\n📝 Admin credentials:'))
        self.stdout.write(self.style.WARNING('   Username: admin'))
        self.stdout.write(self.style.WARNING('   Password: admin123'))
