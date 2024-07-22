from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product


def home_view(request):
    products = Product.objects.all().prefetch_related('images')
    return render(request, 'products/home.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)


def search_view(request):
    query = request.GET.get('q', '')
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    else:
        products = Product.objects.none()

    context = {
        'products': products,
        'query': query,
    }
    return render(request, 'products/search_results.html', context)
