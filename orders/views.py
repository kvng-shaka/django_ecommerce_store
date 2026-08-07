from decimal import Decimal

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from orders.forms import OrderCreateForm
from orders.models import OrderItem, Order
from products.models import Product

# Create your views here.


@login_required
def checkout(request):
    cart = request.session.get("cart", {})
    if not cart:
        return redirect("cart_detail")

    profile = request.user.profile
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            total = Decimal("0.00")
            products = Product.objects.filter(id__in=cart.keys())
            for product in products:
                quantity = int(cart[str(product.id)])
                total += product.price * quantity
            order.total = total
            order.save()

            for product in products:
                quantity = int(cart[str(product.id)])
                OrderItem.objects.create(
                    order=order, product=product, quantity=quantity, price=product.price
                )
            request.session["cart"] = {}

            return redirect("order_confirmation", order_id=order.id)

    else:
        form = OrderCreateForm(
            initial={
                "email": request.user.email,
                "address": profile.address,
                "phone": profile.phone,
                "city": profile.city,
                "country": profile.country,
            }
        )

    return render(request, "orders/checkout.html", {"form": form, "cart": cart})



@login_required
def order_confirmation(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    return render(request, 'orders/order_confirmation.html', {'order':order})



@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_list.html', {'orders':orders})


@login_required
def order_detail(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    return render(request, 'orders/order_detail.html', {'order':order})