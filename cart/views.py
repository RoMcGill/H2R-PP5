from django.shortcuts import render

# Create your views here.


def view_cart(request):
    """
    view to return index page
    """
    return render(request, 'cart/cart.html')
