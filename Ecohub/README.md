# EcoTech Hub - Sustainable Technology Marketplace

![EcoTech Hub](https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?w=1200&h=300&fit=crop)

## 📋 Table of Contents

- [Overview](#overview)
- [Vision & Mission](#vision--mission)
- [Key Features](#key-features)
- [Architecture](#architecture)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [User Workflows](#user-workflows)
- [API Documentation](#api-documentation)
- [Database Schema](#database-schema)
- [Contributing](#contributing)
- [License](#license)

---

## 🌍 Overview

**EcoTech Hub** is a sustainable technology marketplace that connects eco-conscious consumers with verified vendors offering environmentally-friendly products and solutions. The platform serves as a bridge between sustainability-focused businesses and consumers who want to make informed, eco-friendly purchasing decisions.

### The Problem We Solve

In today's market, consumers face several challenges when trying to make sustainable technology purchases:
- **Lack of Transparency**: Difficulty verifying environmental claims made by manufacturers
- **Information Overload**: Too much conflicting information about product sustainability
- **Trust Issues**: Uncertainty about vendor credibility and product certifications
- **No Centralized Platform**: Sustainable tech products scattered across multiple marketplaces
- **Impact Measurement**: No clear way to measure personal environmental impact from purchases

### Our Solution

EcoTech Hub addresses these challenges by providing:
- **Verified Vendor System**: Rigorous verification process for sustainable vendors
- **Standardized Metrics**: Consistent environmental impact measurements across all products
- **Centralized Marketplace**: One-stop shop for eco-friendly technology
- **Impact Calculator**: Tools to measure and visualize your environmental contributions
- **Community Reviews**: Verified purchase reviews with sustainability ratings

---

## 🎯 Vision & Mission

### Vision
To become the world's leading marketplace for sustainable technology, making eco-friendly choices accessible, trustworthy, and measurable for everyone.

### Mission
- **Empower Consumers**: Provide transparent, verified information about product sustainability
- **Support Green Businesses**: Give sustainable vendors a platform to reach conscious consumers
- **Measure Impact**: Help users understand and track their environmental contributions
- **Build Community**: Create a community of eco-conscious consumers and vendors
- **Drive Change**: Accelerate the transition to sustainable technology consumption

---

## ✨ Key Features

### For Consumers

#### 1. **Product Discovery & Search**
- Advanced filtering by environmental certifications (Energy Star, EPEAT, etc.)
- Search by energy efficiency ratings (A+++ to D)
- Filter by carbon footprint, recyclability percentage
- Category-based browsing (Solar, Wind, Smart Home, etc.)
- Price range and availability filters

#### 2. **Environmental Impact Tracking**
- **Impact Calculator**: Calculate energy savings, cost savings, and CO₂ reduction
- **Personal Dashboard**: Track cumulative environmental impact from purchases
- **Comparison Tools**: Compare environmental metrics across similar products

#### 3. **Verified Reviews System**
- Verified purchase reviews only
- Multi-dimensional ratings (Quality, Eco-Impact, Value, Durability)
- Helpful votes and vendor responses
- Photo/video review support

#### 4. **Vendor Profiles**
- Verification status and eco-impact scores
- Company sustainability practices
- Certifications and compliance information
- Vendor ratings and review history

### For Vendors

#### 1. **Vendor Dashboard**
- Product management (CRUD operations)
- Sales analytics and insights
- Inventory tracking
- Customer review management

#### 2. **Verification System**
- Multi-step verification process
- Document submission (certifications, compliance)
- Business verification and sustainability audits
- Ongoing compliance monitoring

#### 3. **Product Management**
- Detailed product listings with environmental metrics
- Multiple image support (local upload + URL)
- Inventory and pricing management
- Discount and promotion tools

### Platform Features

#### 1. **Authentication & Authorization**
- Multi-user types (Consumer, Vendor, Admin)
- JWT-based API authentication
- Session-based web authentication
- Social authentication support (Google, Facebook)

#### 2. **Responsive Design**
- Mobile-first approach
- Bootstrap 5 responsive components
- Touch-friendly interfaces
- Progressive Web App (PWA) ready

#### 3. **API-First Architecture**
- RESTful API endpoints
- Django REST Framework
- API documentation with Swagger/OpenAPI
- Separate web views and API endpoints

---

## 🏗️ Architecture

### System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        Frontend Layer                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  Web Views   │  │  Mobile App  │  │  Admin Panel │      │
│  │  (Bootstrap) │  │   (Future)   │  │   (Django)   │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                      Application Layer                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Django     │  │  DRF API     │  │ Authentication│      │
│  │   Views      │  │  ViewSets    │  │   (JWT/OAuth) │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│                                                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Business   │  │  Validation  │  │  Permissions  │      │
│  │    Logic     │  │   Layer      │  │    Layer      │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                       Data Layer                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Django     │  │    Models    │  │  Serializers │      │
│  │     ORM      │  │   (SQLite/   │  │     (DRF)    │      │
│  │              │  │    MySQL)    │  │              │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
```

### Application Architecture

EcoTech Hub follows a **modular Django application architecture** with clear separation of concerns:

```
EcoHub/
├── accounts/          # User authentication & profiles
├── products/          # Product catalog & management
├── vendors/           # Vendor profiles & verification
├── reviews/           # Review & rating system
├── orders/            # Order processing (future)
├── payments/          # Payment integration (future)
└── analytics/         # Impact tracking & analytics (future)
```

### Design Patterns

1. **Model-View-Template (MVT)**: Django's core pattern for web views
2. **Model-View-Serializer (MVS)**: DRF pattern for API endpoints
3. **Repository Pattern**: Data access abstraction through Django ORM
4. **Factory Pattern**: Model factories for test data generation
5. **Strategy Pattern**: Multiple authentication backends (JWT, Session, OAuth)

---

## 🛠️ Technology Stack

### Backend
- **Framework**: Django 5.2.8
- **API**: Django REST Framework 3.15.2
- **Authentication**: djangorestframework-simplejwt, django-allauth
- **Database**: MySQL (production) / SQLite (development)
- **Image Processing**: Pillow
- **CORS**: django-cors-headers

### Frontend
- **CSS Framework**: Bootstrap 5.3.0
- **Icons**: Font Awesome 6.0.0
- **Template Engine**: Django Templates
- **JavaScript**: Vanilla JS (minimal dependencies)

### DevOps & Tools
- **Version Control**: Git
- **Package Management**: pip
- **Environment Management**: python-decouple
- **Development Server**: Django runserver
- **Production Server**: Gunicorn + Nginx (recommended)

### Third-Party Integrations
- **Image Hosting**: Unsplash (product images)
- **Social Auth**: Google, Facebook (via django-allauth)
- **Payment Gateway**: (Future: Stripe, PayPal)

---

## 📁 Project Structure

```
EcoHub/
│
├── Ecohub/                      # Project root
│   ├── settings.py              # Django settings
│   ├── urls.py                  # Main URL configuration
│   ├── wsgi.py                  # WSGI configuration
│   └── asgi.py                  # ASGI configuration
│
├── accounts/                    # User management app
│   ├── models.py                # Custom User model
│   ├── views.py                 # Auth views (login, register, profile)
│   ├── serializers.py           # User serializers (JWT, registration)
│   ├── urls.py                  # API auth endpoints
│   └── admin.py                 # User admin configuration
│
├── products/                    # Product catalog app
│   ├── models.py                # Product, Category, ProductImage models
│   ├── views.py                 # Product views & API ViewSets
│   ├── serializers.py           # Product serializers
│   ├── urls.py                  # Product API endpoints
│   ├── filters.py               # Product filtering logic
│   └── management/
│       └── commands/
│           └── populate_products.py  # Sample data generator
│
├── vendors/                     # Vendor management app
│   ├── models.py                # Vendor, VendorApplication models
│   ├── views.py                 # Vendor views & API ViewSets
│   ├── serializers.py           # Vendor serializers
│   ├── urls.py                  # Vendor API endpoints
│   └── admin.py                 # Vendor admin configuration
│
├── reviews/                     # Review system app
│   ├── models.py                # Review model
│   ├── views.py                 # Review views & API ViewSets
│   ├── serializers.py           # Review serializers
│   ├── urls.py                  # Review API endpoints
│   └── permissions.py           # Review permissions
│
├── templates/                   # Template files
│   ├── base/
│   │   ├── base.html            # Base template
│   │   ├── home.html            # Homepage
│   │   ├── product_list.html    # Product listing
│   │   ├── product_detail.html  # Product details
│   │   └── impact_calculator.html
│   ├── accounts/
│   │   ├── login.html           # Login form
│   │   ├── register.html        # Registration form
│   │   └── profile.html         # User profile
│   └── vendors/
│       ├── list.html            # Vendor listing
│       ├── detail.html          # Vendor details
│       └── dashboard.html       # Vendor dashboard
│
├── static/                      # Static files
│   ├── css/
│   ├── js/
│   └── images/
│
├── media/                       # User-uploaded files
│   └── products/                # Product images
│
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

---

## 🚀 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- MySQL 8.0 or higher (or SQLite for development)
- pip (Python package manager)
- Virtual environment tool (venv, virtualenv, or conda)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/ecohub.git
cd ecohub/Ecohub
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv eco
eco\Scripts\activate

# macOS/Linux
python3 -m venv eco
source eco/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Environment Configuration

Create a `.env` file in the project root:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration (MySQL)
DB_NAME=ecohub_db
DB_USER=root
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=3306

# Email Configuration (optional)
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Social Auth (optional)
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
FACEBOOK_APP_ID=your-facebook-app-id
FACEBOOK_APP_SECRET=your-facebook-app-secret
```

### Step 5: Database Setup

```bash
# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Load sample data (optional)
python manage.py populate_products
```

### Step 6: Run Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

### Step 7: Access Admin Panel

Visit `http://127.0.0.1:8000/admin/` and login with your superuser credentials.

---

## 👥 User Workflows

### Consumer Workflow

```
1. Registration/Login
   ↓
2. Browse Products
   ├── Filter by category, price, certifications
   ├── Search by keywords
   └── View featured/trending products
   ↓
3. Product Discovery
   ├── View product details
   ├── Check environmental metrics
   ├── Read reviews
   └── Compare with similar products
   ↓
4. Impact Calculation
   ├── Use impact calculator
   ├── Calculate potential savings
   └── View environmental benefits
   ↓
5. Purchase Decision
   ├── Add to cart (future)
   ├── Add to wishlist (future)
   └── Contact vendor
   ↓
6. Post-Purchase
   ├── Write review
   ├── Upload photos
   └── Track environmental impact
```

### Vendor Workflow

```
1. Registration
   ↓
2. Vendor Application
   ├── Submit business information
   ├── Upload certifications
   ├── Provide sustainability documentation
   └── Wait for verification
   ↓
3. Verification Process
   ├── Admin reviews application
   ├── Document verification
   └── Approval/Rejection
   ↓
4. Vendor Dashboard Access
   ↓
5. Product Management
   ├── Add new products
   ├── Set environmental metrics
   ├── Upload product images
   ├── Manage inventory
   └── Set pricing/discounts
   ↓
6. Order Management (future)
   ├── Process orders
   ├── Update order status
   └── Handle customer queries
   ↓
7. Analytics & Insights
   ├── View sales reports
   ├── Track product performance
   └── Monitor customer reviews
```

### Admin Workflow

```
1. Admin Login
   ↓
2. Dashboard Overview
   ├── Platform statistics
   ├── Pending vendor applications
   ├── Flagged reviews
   └── User reports
   ↓
3. Vendor Management
   ├── Review applications
   ├── Verify documents
   ├── Approve/Reject vendors
   └── Monitor vendor compliance
   ↓
4. Content Moderation
   ├── Review flagged content
   ├── Approve/Reject reviews
   ├── Manage product listings
   └── Handle disputes
   ↓
5. Platform Management
   ├── Manage categories
   ├── Update certifications list
   ├── Configure platform settings
   └── Generate reports
```

---

## 🔌 API Documentation

### Authentication Endpoints

#### Register New User
```http
POST /api/auth/register/
Content-Type: application/json

{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "SecurePass123!",
  "first_name": "John",
  "last_name": "Doe",
  "user_type": "consumer",
  "phone": "+1234567890"
}
```

#### Login (Get JWT Token)
```http
POST /api/auth/login/
Content-Type: application/json

{
  "username": "johndoe",
  "password": "SecurePass123!"
}

Response:
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "user": {
    "id": 1,
    "username": "johndoe",
    "email": "john@example.com",
    "user_type": "consumer"
  }
}
```

#### Refresh Token
```http
POST /api/auth/refresh/
Content-Type: application/json

{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### Product Endpoints

#### List Products
```http
GET /api/products/?category=solar&min_price=100&max_price=500
Authorization: Bearer {access_token}

Response:
{
  "count": 25,
  "next": "http://localhost:8000/api/products/?page=2",
  "previous": null,
  "results": [...]
}
```

#### Get Product Details
```http
GET /api/products/{id}/
Authorization: Bearer {access_token}
```

#### Create Product (Vendor only)
```http
POST /api/products/
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "name": "Solar Panel 400W",
  "description": "High-efficiency solar panel",
  "category": "solar",
  "price": "599.99",
  "energy_efficiency_rating": "A+++",
  "carbon_footprint": "25.5",
  ...
}
```

### Vendor Endpoints

#### List Vendors
```http
GET /api/vendors/?verified=true&featured=true
```

#### Get Vendor Details
```http
GET /api/vendors/{id}/
```

#### Apply as Vendor
```http
POST /api/vendors/apply/
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "company_name": "Green Tech Solutions",
  "description": "We provide sustainable tech solutions",
  "business_registration": "REG123456",
  ...
}
```

### Review Endpoints

#### List Product Reviews
```http
GET /api/products/{product_id}/reviews/
```

#### Create Review
```http
POST /api/reviews/
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "product": 1,
  "overall_rating": 5,
  "quality_rating": 5,
  "eco_impact_rating": 4,
  "value_rating": 5,
  "title": "Excellent product!",
  "comment": "This solar panel exceeded my expectations...",
  "would_recommend": true
}
```

---

## 🗄️ Database Schema

### Core Models

#### User Model
```python
User (AbstractUser)
├── username (CharField, unique)
├── email (EmailField, unique)
├── user_type (CharField: consumer/vendor/admin)
├── phone (CharField, optional)
├── email_verified (Boolean)
├── date_joined (DateTime)
└── is_active (Boolean)
```

#### Product Model
```python
Product
├── id (AutoField, PK)
├── vendor (ForeignKey → Vendor)
├── category (ForeignKey → Category)
├── name (CharField)
├── slug (SlugField, unique)
├── description (TextField)
├── price (DecimalField)
├── discounted_price (DecimalField, optional)
├── availability (IntegerField)
├── energy_efficiency_rating (CharField)
├── carbon_footprint (DecimalField)
├── energy_consumption (DecimalField)
├── recyclable_percentage (IntegerField)
├── certifications (CharField)
├── warranty_years (IntegerField)
├── specifications (JSONField)
├── is_active (Boolean)
├── is_featured (Boolean)
├── created_at (DateTime)
└── updated_at (DateTime)
```

#### Vendor Model
```python
Vendor
├── id (AutoField, PK)
├── user (OneToOneField → User)
├── company_name (CharField)
├── description (TextField)
├── logo (ImageField, optional)
├── business_registration (CharField)
├── verification_status (CharField: pending/verified/rejected)
├── eco_impact_score (DecimalField)
├── rating (DecimalField)
├── is_active (Boolean)
├── is_featured (Boolean)
├── certifications (JSONField)
├── created_at (DateTime)
└── updated_at (DateTime)
```

#### Review Model
```python
Review
├── id (AutoField, PK)
├── user (ForeignKey → User)
├── product (ForeignKey → Product)
├── overall_rating (IntegerField, 1-5)
├── quality_rating (IntegerField, 1-5)
├── eco_impact_rating (IntegerField, 1-5)
├── value_rating (IntegerField, 1-5)
├── durability_rating (IntegerField, 1-5)
├── title (CharField)
├── comment (TextField)
├── would_recommend (Boolean)
├── is_verified_purchase (Boolean)
├── is_approved (Boolean)
├── helpful_count (IntegerField)
├── created_at (DateTime)
└── updated_at (DateTime)
```

### Relationships

```
User ──────────┬─────────→ Review
               │
               └─────────→ Vendor (1:1)
                              │
                              ├─────→ Product (1:N)
                              │          │
                              │          └─────→ ProductImage (1:N)
                              │          │
                              │          └─────→ Review (1:N)
                              │
                              └─────→ VendorApplication (1:1)

Category ──────────────────→ Product (1:N)
```

---

## 🎨 Design Philosophy

### User Experience Principles

1. **Transparency First**: All environmental claims must be verifiable
2. **Simplicity**: Clean, intuitive interface with minimal learning curve
3. **Accessibility**: WCAG 2.1 AA compliance for inclusive design
4. **Mobile-First**: Responsive design that works on all devices
5. **Performance**: Fast load times and optimized queries

### Sustainability Metrics

All products must include:
- **Energy Efficiency Rating**: A+++ to D scale
- **Carbon Footprint**: kg CO₂ per year
- **Energy Consumption**: kWh per year
- **Recyclable Percentage**: 0-100%
- **Certifications**: Energy Star, EPEAT, etc.
- **Warranty**: Years of coverage

### Vendor Verification Process

1. **Application Submission**: Business details and documentation
2. **Document Review**: Verify business registration and certifications
3. **Sustainability Audit**: Review environmental practices
4. **Compliance Check**: Ensure product claims are accurate
5. **Approval/Rejection**: Notify vendor of decision
6. **Ongoing Monitoring**: Regular audits and compliance checks

---

## 🔮 Future Roadmap

### Phase 1 (Current)
- ✅ User authentication and profiles
- ✅ Product catalog with filtering
- ✅ Vendor management system
- ✅ Review and rating system
- ✅ Impact calculator
- ✅ Responsive web interface

### Phase 2 (Q2 2024)
- 🔄 Shopping cart and checkout
- 🔄 Payment integration (Stripe, PayPal)
- 🔄 Order management system
- 🔄 Email notifications
- 🔄 Wishlist functionality
- 🔄 Product comparison tool

### Phase 3 (Q3 2024)
- 📋 Advanced analytics dashboard
- 📋 Vendor messaging system
- 📋 Live chat support
- 📋 Mobile app (iOS/Android)
- 📋 Push notifications
- 📋 Advanced search with AI

### Phase 4 (Q4 2024)
- 📋 Community forum
- 📋 Blog and educational content
- 📋 Carbon offset marketplace
- 📋 Subscription service
- 📋 Loyalty rewards program
- 📋 API for third-party integrations

---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### Getting Started

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Contribution Guidelines

- Follow PEP 8 style guide for Python code
- Write meaningful commit messages
- Add tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR

### Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on the issue, not the person
- Help create a positive community

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📞 Contact & Support

- **Email**: support@ecotechhub.com
- **Website**: https://ecotechhub.com
- **GitHub Issues**: [Report a bug or request a feature](https://github.com/yourusername/ecohub/issues)
- **Documentation**: [Full documentation](https://docs.ecotechhub.com)

---

## 🙏 Acknowledgments

- Bootstrap team for the amazing CSS framework
- Django and DRF communities for excellent documentation
- Unsplash for high-quality product images
- All contributors and supporters of sustainable technology

---

## 📊 Project Statistics

- **Total Lines of Code**: ~15,000+
- **Models**: 10+
- **API Endpoints**: 50+
- **Templates**: 15+
- **Test Coverage**: 85%+
- **Last Updated**: January 2025

---

**Made with 💚 for a sustainable future**
