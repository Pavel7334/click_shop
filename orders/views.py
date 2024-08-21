from django.db.models import Sum, F
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import Product, Cart, CartItem, OrderItem, Order
from .forms import OrderForm
from django.urls import reverse


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


# def checkout(request):
#     return render(request, 'orders/checkout.html')


# @login_required
# def checkout_view(request):
#     try:
#         cart = Cart.objects.get(user=request.user)
#     except Cart.DoesNotExist:
#         print("Корзина не найдена для пользователя.")
#         return redirect('cart')  # Перенаправление на страницу корзины, если корзина не найдена
#
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             # Создание заказа
#             order = Order.objects.create(
#                 user=request.user,
#                 paid=False,
#             )
#
#             # Сохранение товаров в заказе
#             for item in cart.items.all():
#                 OrderItem.objects.create(
#                     order=order,
#                     product=item.product,
#                     price=item.product.price,
#                     quantity=item.quantity
#                 )
#
#             # Очистка корзины
#             cart.items.all().delete()
#
#             # Отправка email
#             send_order_confirmation_email(order, request.user.email)
#
#             print(f"Заказ {order.id} создан успешно.")
#             return redirect('order_confirmation')  # Перенаправление на страницу подтверждения заказа
#         else:
#             print("Форма заказа невалидна:", form.errors)
#     else:
#         form = OrderForm()
#
#     # Вычисление общей стоимости корзины
#     total_cost = cart.items.aggregate(total=Sum('product__price'))['total'] or 0
#
#     return render(request, 'orders/checkout.html', {'form': form, 'total_cost': total_cost})


@login_required
def checkout_view(request):
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        print("Корзина не найдена для пользователя.")
        return redirect('cart')

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(user=request.user, paid=False)

            order_items = []
            for item in cart.items.all():
                order_item = OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    price=item.product.price,
                    quantity=item.quantity
                )
                order_items.append(order_item)

            cart.items.all().delete()

            print(f"Заказ {order.id} создан успешно.")
            return redirect(reverse('order_confirmation', args=[order.id]))
        else:
            print("Форма заказа невалидна:", form.errors)
    else:
        form = OrderForm()

    total_cost = cart.items.aggregate(
        total=Sum(F('product__price') * F('quantity'))
    )['total'] or 0

    return render(request, 'orders/checkout.html', {'form': form, 'total_cost': total_cost})


def order_confirmation_view(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order_items = OrderItem.objects.filter(order=order)
    total_cost = sum(item.price * item.quantity for item in order_items)

    return render(request, 'orders/order_confirmation.html', {
        'order': order,
        'order_items': order_items,
        'total_cost': total_cost,
    })


@login_required
def order_history(request):
    # Получаем все заказы пользователя
    orders = Order.objects.filter(user=request.user)

    # Создаем список с данными о каждом заказе, включая общую стоимость
    order_data = []
    for order in orders:
        total_cost = sum(item.price * item.quantity for item in order.items.all())
        order_data.append({
            'id': order.id,
            'created': order.created,
            'updated': order.updated,
            'paid': order.paid,
            'total_cost': total_cost
        })

    return render(request, 'orders/order_history.html', {'orders': order_data})


def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order_items = order.items.all()
    total_cost = sum(item.price * item.quantity for item in order_items)  # Вычислить общую сумму
    return render(request, 'orders/order_detail.html', {
        'order': order,
        'order_items': order_items,
        'total_cost': total_cost
    })