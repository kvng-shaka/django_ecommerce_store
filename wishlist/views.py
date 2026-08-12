from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from products.models import Product

from .models import Wishlist

# Create your views here.


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id, is_available=True)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.products.add(product)

    return redirect(request.META.get('HTTP_REFERER', 'product_list'))



@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist = get_object_or_404(Wishlist, user=request.user)
    wishlist.products.remove(product)

    return redirect(request.META.get('HTTP_REFERER', 'product_list'))




@login_required
def wishlist(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    products = wishlist.products.filter(is_available=True)
    return render(request, 'wishlist/wishlist.html', {'wishlist': wishlist, 'products': products,})