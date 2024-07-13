from django.shortcuts import render, get_object_or_404
from .models import Product, ProductImage


def home_view(request):
    return render(request, 'products/home.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    product_image = product.images.first()
    context = {
        'product': product,
        'product_image': product_image,
    }
    return render(request, 'products/product_detail.html', context)
