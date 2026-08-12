from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from products.models import Product, Category
from django.core.paginator import Paginator

# Create your views here.


def product_list(request):
    search = request.GET.get('search', '').strip()
    category = request.GET.get('category', '').strip()
    min_price = request.GET.get('min_price', '').strip()
    max_price = request.GET.get('max_price', '').strip()

    products = Product.objects.filter(is_available=True)
    categories = Category.objects.all()

    # Search filter
    if search:
        products = products.filter(Q(name__icontains=search) | Q(description__icontains=search))

    # Category filter
    if category:
        products = products.filter(category__name=category)

    # Minimum price
    if min_price:
        products = products.filter(price__gte=min_price)

    # Maximum price
    if max_price:
        products = products.filter(price__lte=max_price)

    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'products/product_list.html', {'products': page_obj, 'page_obj': page_obj, 'search':search, 'category': category, 'categories': categories, 'min_price': min_price, 'max_price': max_price,})


def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk, is_available=True)
    reviews = product.reviews.all()
    return render(request, 'products/product_detail.html', {'product': product, 'reviews': reviews,})