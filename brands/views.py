from django.shortcuts import render, get_object_or_404
from .models import Brands

# Create your views here.


def brands(request):
    """
    view to return brands page
    """
    brands = Brands.objects.all()

    context = {
        'brands': brands

    }
    return render(request, 'brands.html', context)


    def brand_detail(request, brand_id):
    """
    view to return brand details page
    """
    brand = get_object_or_404(brand, pk=brand_id)

    context = {
        'brand': brand,

    }
    return render(request, 'brands-detail.html', context)
