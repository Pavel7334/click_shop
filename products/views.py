from django.shortcuts import render, get_object_or_404
from .models import Product


def home_view(request):
    products = Product.objects.all().prefetch_related('images')
    return render(request, 'products/home.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    product_image = product.images.first()
    context = {
        'product': product,
        'product_image': product_image,
    }
    return render(request, 'products/product_detail.html', context)
