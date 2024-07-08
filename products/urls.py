from django.urls import path

from . import views
from .views import home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('product/<str:slug>/', views.product_detail, name='product_detail'),
]
