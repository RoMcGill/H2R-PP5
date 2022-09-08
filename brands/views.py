from django.shortcuts import render

# Create your views here.


def brands(request):
    """
    view to return index page
    """
    return render(request, 'brands.html')
