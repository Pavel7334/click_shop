from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from .views import home_view, search_view

urlpatterns = [
    path('', home_view, name='home'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/', views.search_view, name='search_results'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

