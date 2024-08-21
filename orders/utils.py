from django.db.models import Sum
from .models import OrderItem
from django.core.mail import send_mail
from django.template.loader import render_to_string


def send_order_confirmation_email(order, recipient_email):
    subject = f'Подтверждение заказа #{order.id}'
    message = render_to_string('orders/order_confirmation.html', {
        'order': order,
        'order_items': OrderItem.objects.filter(order=order),
        'total_cost': OrderItem.objects.filter(order=order).aggregate(total=Sum('price'))['total'] or 0,
    })
    send_mail(
        subject,
        message,
        'your-email@gmail.com',  # Адрес отправителя
        [recipient_email],  # Адрес получателя
        fail_silently=False,
    )