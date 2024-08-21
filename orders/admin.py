from django.contrib import admin
from .models import Order, OrderItem, Cart, CartItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created', 'updated', 'paid')
    list_filter = ('paid', 'created', 'updated', 'user')
    search_fields = ('id', 'user__username')  # Позволяет искать по ID заказа и имени пользователя
    readonly_fields = ('created', 'updated')  # Сделать поля 'created' и 'updated' только для чтения


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(CartItem)
