# 🛒 E-Commerce Store

A Django-based e-commerce web application built as a practical project for developing and strengthening Python and Django skills.

The project provides a foundation for managing products, categories, inventory, and eventually customer carts and orders. It will later be extended with a REST API using Django REST Framework.

## 🚀 Current Features

* Product management
* Product categories
* Product descriptions
* Product pricing
* Product stock management
* Product availability
* Product images
* Product listing page
* Product detail page
* Django admin interface
* SQLite database for development

## 🛠️ Technologies

* Python
* Django
* SQLite
* HTML
* CSS
* Pillow
* Git & GitHub

## 📁 Project Structure

```text
ecommerce_store/
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── products/
│   ├── migrations/
│   ├── templates/
│   │   └── products/
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── media/
├── manage.py
├── README.md
├── .gitignore
└── requirements.txt
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/kvng-shaka/ecommerce_store.git
cd ecommerce_store
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

### macOS/Linux

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Create an admin account:

```bash
python manage.py createsuperuser
```

Start the development server:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/products/
```

## 🔐 Admin

The Django admin dashboard is available at:

```text
http://127.0.0.1:8000/admin/
```

From there, administrators can manage categories and products.

## 🗺️ Project Roadmap

The project will be developed in stages.

* [x] Django project setup
* [x] Product and category models
* [x] Product listing
* [x] Product detail page
* [ ] Shopping cart
* [ ] User authentication
* [ ] Customer profiles
* [ ] Checkout
* [ ] Orders
* [ ] Inventory improvements
* [ ] Search and filtering
* [ ] Django REST Framework API
* [ ] API authentication and permissions
* [ ] API documentation
* [ ] PostgreSQL
* [ ] Production deployment

## 🎯 Learning Goals

This project is being developed to strengthen practical skills in:

* Django
* Database relationships
* Django ORM
* Authentication and permissions
* CRUD operations
* Forms
* Templates
* Media files
* Git and GitHub
* REST API development
* Django REST Framework
* Backend architecture

## 👨‍💻 Author

**Kvng Funsho**

Built as part of my journey toward becoming a stronger Python/Django developer.
