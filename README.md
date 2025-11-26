# EcoHub 🌱

**A Sustainable Technology Marketplace Connecting Eco-Conscious Consumers with Verified Green Vendors**

![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)
![Django](https://img.shields.io/badge/Django-4.2-green.svg)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)

---

## Table of Contents

- [Overview](#overview)
- [The Idea Behind EcoHub](#the-idea-behind-ecohub)
- [Key Features](#key-features)
- [Architecture](#architecture)
- [Technology Stack](#technology-stack)
- [Project Workflow](#project-workflow)
- [Database Schema](#database-schema)
- [API Documentation](#api-documentation)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

**EcoHub** is a comprehensive web platform designed to bridge the gap between environmentally-conscious consumers and vendors selling sustainable technology products. The platform provides detailed environmental metrics for every product, enabling users to make informed purchasing decisions based on energy efficiency, carbon footprint, recyclability, and sustainability certifications.

Unlike traditional e-commerce platforms, EcoHub places environmental impact at the forefront of the shopping experience, helping consumers track their carbon footprint and achieve sustainability goals while supporting verified eco-friendly businesses.

---

## The Idea Behind EcoHub

### Problem Statement

In today's market, consumers who want to make environmentally responsible purchases face several challenges:

1. **Lack of Transparency**: Product listings rarely include comprehensive environmental impact data
2. **Greenwashing**: Unverified sustainability claims make it difficult to trust eco-friendly marketing
3. **Scattered Information**: Environmental certifications and energy ratings are inconsistent across platforms
4. **No Impact Tracking**: Consumers cannot easily measure the environmental benefits of their purchasing decisions

### Our Solution

EcoHub addresses these challenges by:

- **Standardizing Environmental Metrics**: Every product includes energy efficiency ratings, carbon footprint data, energy consumption metrics, and recyclability percentages
- **Vendor Verification**: Rigorous verification process requiring sustainability certificates and business licenses
- **Transparent Reviews**: Multi-dimensional review system that includes actual energy savings and environmental impact feedback
- **Personal Impact Tracking**: Users can set sustainability goals and track their carbon footprint reduction over time
- **Curated Marketplace**: Only eco-friendly products from verified vendors are listed

### Vision

To create the world's most trusted marketplace for sustainable technology, where every purchase contributes to a greener future and consumers have complete transparency about the environmental impact of their choices.

---

## Key Features

### For Consumers

#### 🔍 **Smart Product Discovery**
- Browse products with detailed environmental metrics
- Filter by energy efficiency ratings (A++ to E)
- Search by certifications (Energy Star, LEED, EPEAT, Carbon Neutral, Renewable Energy)
- View carbon footprint (kg CO2/year) and energy consumption (kWh/year)
- Check recyclable percentage for each product

#### 📊 **Impact Tracking**
- Set personal sustainability goals
- Track carbon footprint targets
- Calculate potential energy savings before purchasing
- Monitor cumulative environmental impact

#### ⭐ **Comprehensive Reviews**
- Multi-dimensional ratings:
  - Overall product quality (1-5 stars)
  - Environmental impact (1-5 stars)
  - Value for money (1-5 stars)
  - Build quality (1-5 stars)
- Read actual energy savings from verified purchasers
- Environmental impact notes from real users
- Verified purchase badges

#### 🛡️ **Trust & Transparency**
- All vendors are verified with sustainability certificates
- Product certifications are validated
- Detailed product specifications in JSON format
- Warranty information clearly displayed

### For Vendors

#### 🏢 **Vendor Portal**
- Apply for verification with sustainability certificates
- Upload business licenses and tax documentation
- Manage verification documents

#### 📦 **Product Management**
- Create and manage product listings
- Upload multiple product images (file upload or URL)
- Set pricing, discounts, and stock availability
- Specify environmental metrics and certifications
- Add detailed specifications in JSON format

#### 📈 **Performance Tracking**
- Monitor eco-impact scores
- Track total sales
- View vendor ratings
- Analyze product performance

#### 🎨 **Branding**
- Upload company logo and banner images
- Customize vendor profile
- Showcase sustainability achievements

### For Administrators

#### ✅ **Vendor Management**
- Review and approve vendor applications
- Verify sustainability certificates
- Suspend or reject non-compliant vendors
- Monitor vendor performance

#### 🛠️ **Product Moderation**
- Feature products on homepage
- Verify product certifications
- Manage product categories
- Ensure data quality

#### 💬 **Review Moderation**
- Approve or flag reviews
- Verify purchase status
- Monitor review quality
- Prevent spam and abuse

---

## Architecture

### System Architecture

EcoHub follows a **monolithic Django architecture** with a clear separation of concerns:

```
┌─────────────────────────────────────────────────────────────┐
│                    Client Layer                             │
│  ┌──────────────────┐          ┌──────────────────┐        │
│  │  Web Browser     │          │  Mobile/SPA      │        │
│  │  (Django Tmpl)   │          │  (REST API)      │        │
│  └────────┬─────────┘          └────────┬─────────┘        │
└───────────┼──────────────────────────────┼──────────────────┘
            │                              │
            ▼                              ▼
┌─────────────────────────────────────────────────────────────┐
│                Application Layer (Django)                    │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │   accounts   │  │   products   │  │   vendors    │     │
│  │   (Auth &    │  │  (Catalog &  │  │ (Vendor Mgmt)│     │
│  │   Profile)   │  │   Search)    │  │              │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│  ┌──────────────┐  ┌──────────────┐                        │
│  │   reviews    │  │     api      │                        │
│  │ (Ratings &   │  │  (REST API)  │                        │
│  │  Feedback)   │  │              │                        │
│  └──────────────┘  └──────────────┘                        │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│              Data Layer (MySQL/PostgreSQL)                   │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │  Users   │  │ Products │  │ Vendors  │  │ Reviews  │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### Application Structure

```
EcoHub/
├── Ecohub/                    # Main Django project directory
│   ├── manage.py              # Django management script
│   ├── requirements.txt       # Python dependencies
│   │
│   ├── Ecohub/               # Project configuration
│   │   ├── settings.py       # Django settings
│   │   ├── urls.py           # Root URL configuration
│   │   ├── wsgi.py           # WSGI application
│   │   └── asgi.py           # ASGI application
│   │
│   ├── accounts/             # User Authentication & Profiles
│   │   ├── models.py         # Custom User model
│   │   ├── views.py          # Auth views (JWT + Template)
│   │   ├── serializers.py    # User serializers
│   │   └── urls.py           # Auth routes
│   │
│   ├── products/             # Product Catalog
│   │   ├── models.py         # Product, Category, ProductImage
│   │   ├── views.py          # Product ViewSets
│   │   ├── serializers.py    # Product serializers
│   │   ├── filters.py        # Product filtering
│   │   ├── urls.py           # Product routes
│   │   └── management/
│   │       └── commands/
│   │           └── populate_products.py  # Seed data
│   │
│   ├── vendors/              # Vendor Management
│   │   ├── models.py         # Vendor model
│   │   ├── views.py          # Vendor ViewSets
│   │   ├── serializers.py    # Vendor serializers
│   │   └── urls.py           # Vendor routes
│   │
│   ├── reviews/              # Product Reviews
│   │   ├── models.py         # Review model
│   │   ├── views.py          # Review ViewSets
│   │   ├── serializers.py    # Review serializers
│   │   └── urls.py           # Review routes
│   │
│   ├── api/                  # API Configuration (minimal)
│   │   └── urls.py           # API root routes
│   │
│   ├── templates/            # Django templates
│   │   ├── base/             # Base templates, home page
│   │   ├── accounts/         # Auth templates
│   │   └── vendors/          # Vendor templates
│   │
│   └── static/               # Static files
│       ├── css/              # Custom CSS
│       ├── js/               # JavaScript
│       └── images/           # Images
│
├── .git/                     # Git version control
├── .gitignore                # Git ignore rules
├── LICENSE                   # Apache 2.0 License
└── README.md                 # This file
```

### Design Patterns

1. **MVT (Model-View-Template)**: Standard Django pattern for web interface
2. **REST API**: Django REST Framework for API endpoints
3. **Custom User Model**: Extended Django User for application-specific fields
4. **ViewSets**: DRF ViewSets for standardized CRUD operations
5. **Serializers**: Data validation and transformation layer
6. **Permissions**: Custom permission classes (e.g., `IsVendorOrReadOnly`)
7. **Filters**: django-filter for advanced querying
8. **Signals**: (Potential) Post-save hooks for notifications

---

## Technology Stack

### Backend

| Technology | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.x | Core programming language |
| **Django** | 4.2 | Web framework |
| **Django REST Framework** | Latest | RESTful API |
| **MySQL** | - | Primary database (active) |
| **PostgreSQL** | - | Database (configured, alternative) |

### Authentication & Security

| Package | Purpose |
|---------|---------|
| **django-allauth** | User registration and authentication |
| **djangorestframework-simplejwt** | JWT token authentication |
| **Token Blacklisting** | Secure logout mechanism |

### Frontend

| Technology | Purpose |
|-----------|---------|
| **Django Templates** | Server-side rendering |
| **Bootstrap 5** | CSS framework |
| **Font Awesome 6.0** | Icon library |
| **django-crispy-forms** | Form rendering |
| **crispy-bootstrap5** | Bootstrap 5 template pack |

### Additional Libraries

| Package | Purpose |
|---------|---------|
| **Pillow** | Image processing |
| **django-filter** | Advanced filtering |
| **django-cors-headers** | CORS support for SPA |
| **WhiteNoise** | Static file serving |
| **Gunicorn** | Production WSGI server |
| **python-decouple** | Environment variable management |
| **django-extensions** | Development utilities |

### Future Integrations (Configured)

- **Stripe**: Payment processing
- **Celery**: Asynchronous tasks
- **Redis**: Caching and task queue

---

## Project Workflow

### User Registration & Authentication Flow

```
1. User Registration
   ├─→ User selects type (Consumer/Vendor)
   ├─→ Fills registration form
   ├─→ Email verification sent
   ├─→ User confirms email
   └─→ Account activated

2. JWT Authentication
   ├─→ User submits credentials
   ├─→ Server validates and issues JWT tokens
   │   ├─→ Access Token (short-lived)
   │   └─→ Refresh Token (long-lived)
   ├─→ Client stores tokens
   └─→ Access token included in API requests
```

### Vendor Onboarding Flow

```
1. Application Submission
   ├─→ User registers as Vendor type
   ├─→ Fills vendor application form
   │   ├─→ Company information
   │   ├─→ Business license upload
   │   ├─→ Tax ID
   │   ├─→ Sustainability certificate
   │   └─→ Contact details
   └─→ Status: PENDING

2. Admin Review
   ├─→ Admin reviews application
   ├─→ Verifies documents
   ├─→ Checks sustainability credentials
   └─→ Decision:
       ├─→ VERIFIED: Vendor can list products
       ├─→ REJECTED: Application denied
       └─→ SUSPENDED: Temporarily disabled

3. Vendor Activation
   ├─→ Vendor receives approval notification
   ├─→ Access to vendor dashboard unlocked
   └─→ Can create product listings
```

### Product Listing Flow

```
1. Product Creation (Vendor)
   ├─→ Navigate to vendor dashboard
   ├─→ Click "Add Product"
   ├─→ Fill product details:
   │   ├─→ Basic info (name, description, price)
   │   ├─→ Category selection
   │   ├─→ Environmental metrics:
   │   │   ├─→ Energy efficiency rating (A++ to E)
   │   │   ├─→ Carbon footprint (kg CO2/year)
   │   │   ├─→ Energy consumption (kWh/year)
   │   │   ├─→ Recyclable percentage (0-100%)
   │   │   └─→ Certifications (Energy Star, LEED, etc.)
   │   ├─→ Product images (upload or URL)
   │   ├─→ Specifications (JSON format)
   │   └─→ Stock & warranty info
   └─→ Product published

2. Product Discovery (Consumer)
   ├─→ Browse categories
   ├─→ Apply filters:
   │   ├─→ Price range
   │   ├─→ Energy efficiency
   │   ├─→ Carbon footprint
   │   ├─→ Certifications
   │   └─→ Vendor rating
   ├─→ Search by keywords
   └─→ View product details

3. Product Moderation (Admin)
   ├─→ Review new products
   ├─→ Verify certifications
   ├─→ Feature quality products
   └─→ Remove non-compliant listings
```

### Shopping & Review Flow

```
1. Product Purchase
   ├─→ Consumer selects product
   ├─→ Views environmental impact
   ├─→ Checks sustainability metrics
   ├─→ (Future: Adds to cart & checkout)
   └─→ Purchase marked as verified

2. Post-Purchase Review
   ├─→ Consumer receives review prompt
   ├─→ Fills multi-dimensional review:
   │   ├─→ Overall rating (1-5)
   │   ├─→ Eco-impact rating (1-5)
   │   ├─→ Value for money (1-5)
   │   ├─→ Build quality (1-5)
   │   ├─→ Review text
   │   ├─→ Actual energy savings
   │   └─→ Environmental impact notes
   ├─→ Review submitted
   └─→ Status: Pending approval

3. Review Moderation
   ├─→ Admin reviews submission
   ├─→ Verifies purchase (if claimed)
   ├─→ Checks for spam/abuse
   └─→ Approves or rejects

4. Review Display
   ├─→ Approved reviews shown on product page
   ├─→ Aggregated statistics calculated:
   │   ├─→ Average ratings (overall, eco, value, quality)
   │   ├─→ Total review count
   │   ├─→ Rating distribution
   │   └─→ Recommendation percentage
   └─→ Users can mark reviews helpful
```

### Impact Tracking Flow

```
1. Goal Setting
   ├─→ Consumer sets sustainability goals
   ├─→ Defines carbon footprint target
   └─→ Saved in user profile

2. Purchase Impact
   ├─→ Product carbon footprint recorded
   ├─→ Energy savings calculated
   └─→ Added to user's impact score

3. Progress Tracking
   ├─→ Dashboard shows cumulative savings
   ├─→ Displays progress toward goals
   └─→ Provides recommendations
```

---

## Database Schema

### Core Models

#### **User Model** (`accounts.User`)
Extends Django's AbstractUser with custom fields.

| Field | Type | Description |
|-------|------|-------------|
| `username` | CharField | Unique username |
| `email` | EmailField | Email address |
| `user_type` | CharField | consumer / vendor / admin |
| `phone` | CharField | Contact phone number |
| `address` | TextField | Physical address |
| `sustainability_goals` | TextField | Personal eco goals |
| `carbon_footprint_target` | FloatField | Target CO2 reduction |
| `email_verified` | BooleanField | Email verification status |
| `created_at` | DateTimeField | Account creation date |
| `updated_at` | DateTimeField | Last update |

#### **Vendor Model** (`vendors.Vendor`)
One-to-one relationship with User.

| Field | Type | Description |
|-------|------|-------------|
| `user` | OneToOneField | Links to User |
| `company_name` | CharField | Business name |
| `business_license` | CharField | License number |
| `tax_id` | CharField | Tax identification |
| `business_address` | TextField | Business location |
| `contact_phone` | CharField | Business phone |
| `website` | URLField | Company website |
| `verification_status` | CharField | pending/verified/rejected/suspended |
| `sustainability_certificate` | FileField | Certificate upload |
| `verification_documents` | FileField | Supporting documents |
| `rating` | DecimalField | Vendor rating (0-5) |
| `total_sales` | IntegerField | Number of sales |
| `eco_impact_score` | DecimalField | Environmental score |
| `logo` | ImageField | Company logo |
| `banner_image` | ImageField | Profile banner |

#### **Category Model** (`products.Category`)
Hierarchical product categories.

| Field | Type | Description |
|-------|------|-------------|
| `name` | CharField | Category name |
| `slug` | SlugField | URL-friendly name |
| `description` | TextField | Category description |
| `icon` | CharField | Icon class/name |
| `parent` | ForeignKey | Parent category (nullable) |

#### **Product Model** (`products.Product`)
Core product information with environmental metrics.

| Field | Type | Description |
|-------|------|-------------|
| `name` | CharField | Product name |
| `description` | TextField | Product description |
| `slug` | SlugField | URL-friendly name |
| `category` | ForeignKey | Product category |
| `vendor` | ForeignKey | Selling vendor |
| `price` | DecimalField | Base price |
| `discounted_price` | DecimalField | Sale price (optional) |
| **Environmental Metrics** | | |
| `energy_efficiency_rating` | CharField | A++, A+, A, B, C, D, E |
| `carbon_footprint` | DecimalField | kg CO2/year |
| `energy_consumption` | DecimalField | kWh/year |
| `recyclable_percentage` | IntegerField | 0-100% |
| `certifications` | JSONField | List of certifications |
| **Other Details** | | |
| `specifications` | JSONField | Technical specs |
| `warranty_years` | IntegerField | Warranty period |
| `stock_quantity` | IntegerField | Available stock |
| `is_featured` | BooleanField | Featured product |
| `is_active` | BooleanField | Listing active |
| `created_at` | DateTimeField | Creation date |
| `updated_at` | DateTimeField | Last update |

#### **ProductImage Model** (`products.ProductImage`)
Multiple images per product.

| Field | Type | Description |
|-------|------|-------------|
| `product` | ForeignKey | Associated product |
| `image` | ImageField | Image file upload |
| `image_url` | URLField | Alternative image URL |
| `alt_text` | CharField | Image description |
| `is_primary` | BooleanField | Main product image |
| `display_order` | IntegerField | Sort order |

#### **Review Model** (`reviews.Review`)
Multi-dimensional product reviews.

| Field | Type | Description |
|-------|------|-------------|
| `user` | ForeignKey | Reviewer |
| `product` | ForeignKey | Reviewed product |
| **Ratings (1-5)** | | |
| `overall_rating` | IntegerField | Overall score |
| `eco_impact_rating` | IntegerField | Environmental impact |
| `value_for_money` | IntegerField | Value rating |
| `build_quality` | IntegerField | Quality rating |
| **Review Content** | | |
| `title` | CharField | Review title |
| `comment` | TextField | Review text |
| `actual_energy_savings` | DecimalField | Real savings (kWh/year) |
| `environmental_impact_notes` | TextField | Eco impact feedback |
| **Metadata** | | |
| `would_recommend` | BooleanField | Recommendation |
| `is_verified_purchase` | BooleanField | Verified buyer |
| `is_approved` | BooleanField | Admin approval |
| `helpful_votes` | IntegerField | Helpful count |
| `created_at` | DateTimeField | Review date |

**Unique Constraint**: (user, product) - One review per user per product

### Relationships

```
User (1) ──────── (1) Vendor
User (1) ──────── (N) Review
User (1) ──────── (N) Product (as vendor)

Vendor (1) ─────── (N) Product

Category (1) ───── (N) Category (parent-child)
Category (1) ───── (N) Product

Product (1) ────── (N) ProductImage
Product (1) ────── (N) Review
```

---

## API Documentation

### Base URL
```
Production: https://ecohub.com/api/
Development: http://localhost:8000/api/
```

### Authentication

All protected endpoints require JWT authentication:

```http
Authorization: Bearer <access_token>
```

### Authentication Endpoints

#### Register User
```http
POST /api/auth/register/
Content-Type: application/json

{
  "username": "string",
  "email": "string",
  "password": "string",
  "user_type": "consumer|vendor|admin",
  "phone": "string",
  "address": "string"
}

Response: 201 Created
{
  "id": 1,
  "username": "string",
  "email": "string",
  "user_type": "consumer",
  "token": {
    "access": "string",
    "refresh": "string"
  }
}
```

#### Login
```http
POST /api/auth/login/
Content-Type: application/json

{
  "username": "string",
  "password": "string"
}

Response: 200 OK
{
  "access": "string",
  "refresh": "string",
  "user": {
    "id": 1,
    "username": "string",
    "email": "string",
    "user_type": "consumer"
  }
}
```

#### Refresh Token
```http
POST /api/auth/refresh/
Content-Type: application/json

{
  "refresh": "string"
}

Response: 200 OK
{
  "access": "string"
}
```

#### Logout
```http
POST /api/auth/logout/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "refresh": "string"
}

Response: 205 Reset Content
```

#### Get/Update Profile
```http
GET /api/auth/profile/
PUT /api/auth/profile/
Authorization: Bearer <access_token>

Response: 200 OK
{
  "id": 1,
  "username": "string",
  "email": "string",
  "user_type": "consumer",
  "phone": "string",
  "address": "string",
  "sustainability_goals": "string",
  "carbon_footprint_target": 100.0,
  "email_verified": true
}
```

### Product Endpoints

#### List Products
```http
GET /api/products/?page=1&category=1&min_price=0&max_price=1000&energy_efficiency=A++

Query Parameters:
- page: Page number (default: 1)
- category: Category ID
- min_price: Minimum price
- max_price: Maximum price
- energy_efficiency: A++, A+, A, B, C, D, E
- certifications: Comma-separated list
- search: Keyword search

Response: 200 OK
{
  "count": 100,
  "next": "url",
  "previous": null,
  "results": [
    {
      "id": 1,
      "name": "Eco Solar Panel 300W",
      "slug": "eco-solar-panel-300w",
      "description": "High-efficiency solar panel",
      "category": {
        "id": 1,
        "name": "Solar Panels"
      },
      "vendor": {
        "id": 1,
        "company_name": "Green Energy Co",
        "rating": 4.5
      },
      "price": "599.99",
      "discounted_price": "499.99",
      "energy_efficiency_rating": "A++",
      "carbon_footprint": "50.00",
      "energy_consumption": "0.00",
      "recyclable_percentage": 95,
      "certifications": ["Energy Star", "LEED"],
      "primary_image": {
        "id": 1,
        "image_url": "url",
        "alt_text": "Solar panel"
      },
      "stock_quantity": 50,
      "is_featured": true,
      "created_at": "2024-01-01T00:00:00Z"
    }
  ]
}
```

#### Create Product (Vendor Only)
```http
POST /api/products/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "name": "Eco Solar Panel 300W",
  "description": "High-efficiency solar panel",
  "category": 1,
  "price": "599.99",
  "discounted_price": "499.99",
  "energy_efficiency_rating": "A++",
  "carbon_footprint": "50.00",
  "energy_consumption": "0.00",
  "recyclable_percentage": 95,
  "certifications": ["Energy Star", "LEED"],
  "specifications": {
    "wattage": "300W",
    "dimensions": "65x39x1.4 inches",
    "weight": "40 lbs"
  },
  "warranty_years": 25,
  "stock_quantity": 50
}

Response: 201 Created
```

#### Get Product Detail
```http
GET /api/products/{id}/

Response: 200 OK
{
  "id": 1,
  "name": "Eco Solar Panel 300W",
  "description": "High-efficiency solar panel",
  "category": {...},
  "vendor": {...},
  "price": "599.99",
  "images": [
    {
      "id": 1,
      "image_url": "url",
      "is_primary": true
    }
  ],
  "average_rating": 4.5,
  "total_reviews": 42,
  "energy_efficiency_rating": "A++",
  "carbon_footprint": "50.00",
  "certifications": ["Energy Star", "LEED"],
  "specifications": {...}
}
```

#### Featured Products
```http
GET /api/products/featured/

Response: 200 OK
[
  {...product...},
  {...product...}
]
```

#### My Products (Vendor)
```http
GET /api/products/my_products/
Authorization: Bearer <access_token>

Response: 200 OK
[
  {...product...}
]
```

### Vendor Endpoints

#### List Vendors
```http
GET /api/vendors/api/

Response: 200 OK
{
  "count": 50,
  "results": [
    {
      "id": 1,
      "company_name": "Green Energy Co",
      "business_address": "123 Eco St",
      "website": "https://greenenergyco.com",
      "verification_status": "verified",
      "rating": 4.5,
      "total_sales": 1500,
      "eco_impact_score": 92.5,
      "logo": "url",
      "created_at": "2024-01-01T00:00:00Z"
    }
  ]
}
```

#### Apply for Vendor Status
```http
POST /api/vendors/api/apply/
Authorization: Bearer <access_token>
Content-Type: multipart/form-data

{
  "company_name": "Green Energy Co",
  "business_license": "file",
  "tax_id": "123456789",
  "business_address": "123 Eco St",
  "contact_phone": "+1234567890",
  "website": "https://greenenergyco.com",
  "sustainability_certificate": "file"
}

Response: 201 Created
```

#### Get Vendor's Products
```http
GET /api/vendors/api/{id}/products/

Response: 200 OK
[
  {...product...}
]
```

### Review Endpoints

#### Create Review
```http
POST /api/reviews/api/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "product": 1,
  "overall_rating": 5,
  "eco_impact_rating": 5,
  "value_for_money": 4,
  "build_quality": 5,
  "title": "Excellent solar panel!",
  "comment": "Exceeded my expectations...",
  "actual_energy_savings": "350.00",
  "environmental_impact_notes": "Reduced my carbon footprint significantly",
  "would_recommend": true
}

Response: 201 Created
```

#### Get Product Reviews with Statistics
```http
GET /api/reviews/api/product/{product_id}/

Response: 200 OK
{
  "reviews": [
    {
      "id": 1,
      "user": {
        "username": "john_doe"
      },
      "overall_rating": 5,
      "eco_impact_rating": 5,
      "title": "Excellent!",
      "comment": "Great product",
      "is_verified_purchase": true,
      "helpful_votes": 12,
      "created_at": "2024-01-15T00:00:00Z"
    }
  ],
  "statistics": {
    "average_overall_rating": 4.5,
    "average_eco_impact_rating": 4.7,
    "average_value_rating": 4.3,
    "average_build_quality": 4.6,
    "total_reviews": 42,
    "rating_distribution": {
      "5": 25,
      "4": 12,
      "3": 3,
      "2": 1,
      "1": 1
    }
  }
}
```

#### Mark Review Helpful
```http
POST /api/reviews/api/{id}/mark_helpful/
Authorization: Bearer <access_token>

Response: 200 OK
{
  "helpful_votes": 13
}
```

### Pagination

All list endpoints support pagination:
- Default page size: 20 items
- Use `?page=N` to navigate pages
- Response includes `count`, `next`, and `previous` fields

### Filtering

Products support advanced filtering:
```http
GET /api/products/?category=1&min_price=100&max_price=500&energy_efficiency=A++&certifications=Energy Star,LEED
```

### Rate Limiting

- Anonymous users: 100 requests/hour
- Authenticated users: 1000 requests/hour
- Vendors: 2000 requests/hour

---

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- MySQL or PostgreSQL
- pip (Python package manager)
- Virtual environment (recommended)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/EcoHub.git
cd EcoHub/Ecohub
```

### Step 2: Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Database

**Option A: MySQL (Default)**

1. Create MySQL database:
```sql
CREATE DATABASE ecohub_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'ecohub_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON ecohub_db.* TO 'ecohub_user'@'localhost';
FLUSH PRIVILEGES;
```

2. Update `Ecohub/settings.py` (already configured):
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ecohub_db',
        'USER': 'ecohub_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

**Option B: PostgreSQL**

1. Create PostgreSQL database:
```sql
CREATE DATABASE ecohub_db;
CREATE USER ecohub_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE ecohub_db TO ecohub_user;
```

2. Update `Ecohub/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ecohub_db',
        'USER': 'ecohub_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Step 5: Environment Variables (Optional)

Create a `.env` file in the `Ecohub/` directory:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_NAME=ecohub_db
DATABASE_USER=ecohub_user
DATABASE_PASSWORD=your_password
DATABASE_HOST=localhost
DATABASE_PORT=3306
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Step 6: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 7: Create Superuser

```bash
python manage.py createsuperuser
```

### Step 8: Load Sample Data (Optional)

```bash
python manage.py populate_products
```

### Step 9: Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### Step 10: Run Development Server

```bash
python manage.py runserver
```

Visit `http://localhost:8000` to access the application.

### Production Deployment

For production, use Gunicorn:

```bash
gunicorn Ecohub.wsgi:application --bind 0.0.0.0:8000
```

Configure with Nginx as a reverse proxy and use environment variables for sensitive settings.

---

## Usage

### For Consumers

1. **Register an Account**
   - Navigate to `/accounts/register/`
   - Select "Consumer" as user type
   - Fill in required information
   - Verify email

2. **Browse Products**
   - Visit homepage
   - Browse categories or search
   - Apply filters (price, efficiency, certifications)
   - View detailed product information

3. **Set Sustainability Goals**
   - Go to profile settings
   - Define carbon footprint targets
   - Set sustainability goals

4. **Leave Reviews**
   - Purchase products
   - Navigate to product page
   - Click "Write Review"
   - Fill multi-dimensional rating form

### For Vendors

1. **Apply for Vendor Status**
   - Register with "Vendor" user type
   - Navigate to `/vendors/apply/`
   - Upload required documents:
     - Business license
     - Sustainability certificate
     - Tax ID
   - Wait for admin approval

2. **Manage Products**
   - Access vendor dashboard
   - Click "Add Product"
   - Fill environmental metrics
   - Upload product images
   - Set pricing and stock

3. **Track Performance**
   - View eco-impact score
   - Monitor sales statistics
   - Check vendor rating
   - Analyze product performance

### For Administrators

1. **Access Admin Panel**
   - Navigate to `/admin/`
   - Login with superuser credentials

2. **Manage Vendors**
   - Review applications under "Vendors"
   - Verify documents
   - Approve/reject/suspend vendors

3. **Moderate Content**
   - Review product listings
   - Feature quality products
   - Moderate reviews
   - Verify purchases

---

## API Usage Examples

### Using cURL

```bash
# Register
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "ecouser",
    "email": "user@ecohub.com",
    "password": "SecurePass123",
    "user_type": "consumer"
  }'

# Login
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "ecouser",
    "password": "SecurePass123"
  }'

# Get products (with auth)
curl -X GET http://localhost:8000/api/products/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"

# Create review
curl -X POST http://localhost:8000/api/reviews/api/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "product": 1,
    "overall_rating": 5,
    "eco_impact_rating": 5,
    "title": "Excellent product",
    "comment": "Highly recommended!"
  }'
```

### Using Python Requests

```python
import requests

BASE_URL = "http://localhost:8000/api"

# Register
response = requests.post(f"{BASE_URL}/auth/register/", json={
    "username": "ecouser",
    "email": "user@ecohub.com",
    "password": "SecurePass123",
    "user_type": "consumer"
})
print(response.json())

# Login
response = requests.post(f"{BASE_URL}/auth/login/", json={
    "username": "ecouser",
    "password": "SecurePass123"
})
tokens = response.json()
access_token = tokens['access']

# Get products
headers = {"Authorization": f"Bearer {access_token}"}
response = requests.get(f"{BASE_URL}/products/", headers=headers)
products = response.json()

# Filter products
response = requests.get(
    f"{BASE_URL}/products/",
    headers=headers,
    params={
        "energy_efficiency": "A++",
        "min_price": 100,
        "max_price": 1000,
        "certifications": "Energy Star"
    }
)
filtered_products = response.json()
```

### Using JavaScript (Fetch API)

```javascript
const BASE_URL = 'http://localhost:8000/api';

// Register
async function register() {
  const response = await fetch(`${BASE_URL}/auth/register/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      username: 'ecouser',
      email: 'user@ecohub.com',
      password: 'SecurePass123',
      user_type: 'consumer'
    })
  });
  return await response.json();
}

// Login
async function login() {
  const response = await fetch(`${BASE_URL}/auth/login/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      username: 'ecouser',
      password: 'SecurePass123'
    })
  });
  const data = await response.json();
  localStorage.setItem('access_token', data.access);
  return data;
}

// Get products
async function getProducts() {
  const token = localStorage.getItem('access_token');
  const response = await fetch(`${BASE_URL}/products/`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  return await response.json();
}

// Create review
async function createReview(productId, reviewData) {
  const token = localStorage.getItem('access_token');
  const response = await fetch(`${BASE_URL}/reviews/api/`, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      product: productId,
      ...reviewData
    })
  });
  return await response.json();
}
```

---

## Contributing

We welcome contributions to EcoHub! Here's how you can help:

### Getting Started

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Write/update tests
5. Commit your changes: `git commit -m "Add your feature"`
6. Push to your branch: `git push origin feature/your-feature-name`
7. Create a Pull Request

### Contribution Guidelines

- Follow PEP 8 style guidelines for Python code
- Write descriptive commit messages
- Add tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR
- Keep PRs focused on a single feature/fix

### Code Style

```python
# Good
def calculate_carbon_savings(product, usage_hours):
    """
    Calculate carbon savings based on product efficiency.

    Args:
        product: Product instance
        usage_hours: Hours of usage per year

    Returns:
        float: Carbon savings in kg CO2/year
    """
    baseline_consumption = 100  # kWh/year
    actual_consumption = product.energy_consumption
    return (baseline_consumption - actual_consumption) * 0.92
```

### Testing

Run tests before submitting:

```bash
python manage.py test
```

### Reporting Issues

- Use GitHub Issues
- Provide detailed description
- Include steps to reproduce
- Specify environment details

---

## Roadmap

### Phase 1 (Current)
- [x] User authentication and profiles
- [x] Vendor verification system
- [x] Product catalog with environmental metrics
- [x] Review system
- [x] REST API

### Phase 2 (In Progress)
- [ ] Shopping cart functionality
- [ ] Payment integration (Stripe)
- [ ] Order management
- [ ] Email notifications

### Phase 3 (Planned)
- [ ] Advanced impact calculator
- [ ] Personalized product recommendations
- [ ] Vendor analytics dashboard
- [ ] Mobile app (React Native)
- [ ] Social features (share goals, achievements)

### Phase 4 (Future)
- [ ] Carbon offset marketplace
- [ ] Sustainability challenges and rewards
- [ ] API for third-party integrations
- [ ] Machine learning for product categorization
- [ ] Blockchain for supply chain transparency

---

## License

This project is licensed under the **Apache License 2.0**.

```
Copyright 2024 EcoHub

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

See the [LICENSE](LICENSE) file for full details.

---

## Support

- **Documentation**: This README and inline code comments
- **Issues**: [GitHub Issues](https://github.com/yourusername/EcoHub/issues)
- **Email**: support@ecohub.com
- **Community**: [Join our Discord](#)

---

## Acknowledgments

- Django community for the excellent framework
- Django REST Framework for API tools
- Bootstrap team for the UI framework
- All contributors and supporters of sustainable technology

---

## Contact

**EcoHub Team**
- Website: [ecohub.com](#)
- Email: info@ecohub.com
- Twitter: [@EcoHub](#)
- LinkedIn: [EcoHub](#)

---

**Made with 💚 for a sustainable future**
