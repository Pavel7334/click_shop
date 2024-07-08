from django.shortcuts import render, get_object_or_404
from .models import Product


def home_view(request):
    return render(request, 'products/home.html')


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'products/product_detail.html', {'product': product})