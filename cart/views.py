from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from brands.models import Brand_products



# Create your views here.


def view_cart(request):
    """
    view to return cart contents page
    """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    product = Brand_products.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'Updated {product.product_name} quantity to {cart[item_id]}')
    else:

        cart[item_id] = quantity
        messages.success(request, f'Added {product.product_name} to your cart')
    request.session['cart'] = cart


    return redirect(redirect_url)


def adjust_cart(request, item_id):
    product = get_object_or_404(Brand_products, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    print(quantity)
    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request, f'Updated {product.product_name} quantity to {cart[item_id]}')
    else:
        cart.pop(item_id)
        messages.success(request, f'Removed {product.product_name} from cart')
        print("item pop")

    request.session['cart'] = cart
    print("redirected")
    return redirect(reverse('view_cart'))


def remove_cart(request, item_id):

    cart = request.session.get('cart', {})
    cart.pop(item_id)
    messages.success(request, f'Removed {product.product_name} from cart')
    print("item pop")

    request.session['cart'] = cart
    print("redirected")
    return HttpResponse(status=200)






