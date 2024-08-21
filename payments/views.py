from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Order


# Функция для проверки прав пользователя (например, на основе группы или роли)
def is_staff_user(user):
    return user.is_staff


@login_required
@user_passes_test(is_staff_user)  # Только для администраторов или курьеров
def confirm_payment(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.paid = True
    order.save()
    return redirect('order_history')
