from django.urls import path
from . import views

urlpatterns = [
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('increase-quantity/<int:item_id>/', views.increase_quantity, name='increase_quantity'),
    path('decrease-quantity/<int:item_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('remove-item/<int:item_id>/', views.remove_item, name='remove_item'),
    path('checkout/', views.checkout, name='checkout'),
]
