from django.shortcuts import get_object_or_404, render

from products.models import Product

# Create your views here.


def product_list(request):
    products = Product.objects.filter(is_available=True)
    return render(request, 'products/product_list.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk, is_available=True)
    return render(request, 'products/product_detail.html', {'product': product})