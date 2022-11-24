"""
imports
"""
from django.shortcuts import render, get_object_or_404
from .models import Brands, Brand_products

# Create your views here.


def brands(request):
    """
    view to return brands page
    """
    brands = Brands.objects.all()

    context = {
        'brands': brands

    }
    return render(request, 'brands/brands.html', context)


def brand_detail(request, brand_id):
    """
    view to return brand details page
    """
    brand = get_object_or_404(Brands, pk=brand_id)
    brand_products = Brand_products.objects.filter(brand=brand_id)

    context = {
        'brand': brand,
        'brand_products': brand_products,

    }
    return render(request, 'brands/brands-detail.html', context)
