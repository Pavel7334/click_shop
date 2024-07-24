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
        # Ищем продукт с именем, содержащим запрос
        product = Product.objects.filter(name__icontains=query).first()
        if product:
            # Если найден продукт, перенаправляем на страницу деталей продукта
            return render(request, 'products/product_detail.html', {'product': product})
        else:
            # Если продукта не найдено, выводим страницу результатов поиска
            return render(request, 'products/search_results.html', {'query': query})

    # Если запрос пуст, выводим страницу результатов поиска
    return render(request, 'products/search_results.html', {'query': query})
