from django import template

register = template.Library()


@register.filter
def cart_total(cart):
    return sum(item.product.price * item.quantity for item in cart.items.all())
