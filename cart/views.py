from django.shortcuts import redirect, render, get_object_or_404

from products.models import Product

# Create your views here.

def cart_detail(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        sub_total = product.price * quantity
        total += sub_total
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'sub_total': sub_total,
        })
    return render(request, 'cart/cart_detail.html', {'cart_items': cart_items, 'total': total})


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id, is_available=True)
    cart = request.session.get('cart', {})
    product_id = str(product.id)
    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    request.session['cart'] = cart
    request.session.modified = True
    return redirect('cart_detail')




def update_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id, is_available=True)
    cart = request.session.get('cart', {})
    product_id = str(product.id)
    if product_id not in cart:
        return redirect('cart_detail')

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            cart[product_id] = quantity
        else:
            del cart[product_id]

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart_detail')



def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id = str(product_id)
    if product_id in cart:
        del cart[product_id]
    request.session['cart'] = cart
    request.session.modified = True
    return redirect('cart_detail')



