from django.urls import path
from . import views

urlpatterns = [
    path('order/confirm_payment/<int:order_id>/', views.confirm_payment, name='confirm_payment'),
]
