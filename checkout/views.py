from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart',{})
    if not cart:
        messages.error(request, "Your Cart Is Empty!")
        return redirect(reverse('home'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {

        "order_form": order_form,
        "stripe_public_key": 'pk_test_51LuKPJHTzR2Hy8K4jGXOg03Qr19Rhk4FEaxqGiEBQ4ZyfyudW59oaS9dN0PN9mgYre2yLPVKGODRYx1Nj0pJUbzU004EhgtTM9',
        "client_secret": 'test client secret',

    }

    return render(request, template, context)
