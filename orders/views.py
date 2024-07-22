from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .models import Product, Cart, CartItem
from django.http import JsonResponse


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')


@login_required
def cart(request):
    cart = Cart.objects.filter(user=request.user).first()
    total_cost = sum(item.product.price * item.quantity for item in cart.items.all()) if cart else 0
    return render(request, 'orders/cart.html', {'cart': cart, 'total_cost': total_cost})


def increase_quantity(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.quantity += 1
    cart_item.save()
    return JsonResponse({
        'quantity': cart_item.quantity,
        'total': sum(item.product.price * item.quantity for item in cart_item.cart.items.all())
    })


def decrease_quantity(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    if cart_item.quantity > 0:
        cart_item.quantity -= 1
        cart_item.save()
    return JsonResponse({
        'quantity': cart_item.quantity,
        'total': sum(item.product.price * item.quantity for item in cart_item.cart.items.all())
    })


def remove_item(request, item_id):
    try:
        cart_item = CartItem.objects.get(id=item_id)
        cart = cart_item.cart
        cart_item.delete()
        return JsonResponse({
            'total': sum(item.product.price * item.quantity for item in cart.items.all()),
            'count': cart.items.count()
        })
    except CartItem.DoesNotExist:
        return JsonResponse({'error': 'Item not found'}, status=404)


def checkout(request):
    return render(request, 'orders/checkout.html')
