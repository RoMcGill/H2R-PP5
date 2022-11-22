from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import Brand_form, Product_form
from brands.models import Brand_products
from django.contrib import messages


# Create your views here.
@login_required
def brand_upload(request):
    if request.method == 'POST':  # this means the form has data
        form = Brand_form(request.POST, request.FILES)  # get the form and it data
        if form.is_valid():  # check if it is valid
            brand_name = form.cleaned_data.get('brand_name')  # clean the data
            brand_email = form.cleaned_data.get('brand_email')
            description = form.cleaned_data.get('description')  # clean the data
            image = form.cleaned_data.get('image')  # clean the data

            form.save()  # save the data to the model
            messages.success(request, 'Your brand has been added! Please wait to be approved to Upload A product Usual wait Time: 24 hours.')
            return redirect(reverse('brands'))
        else:  # form not valid so display message and retain the data entered
            form = Brand_form(request.POST)
            messages.success(request, 'Error in creating your product, the form is not valid!')
            return render(request, 'upload/brand-upload.html', {'form': form})
    else:  # the form has no data
        form = Brand_form()  #produce a blank form
        return render(request, 'upload/brand-upload.html', {'form': form})

@login_required
def product_upload(request):
    if not request.user.is_staff:
        messages.error(request, 'Only Store owners can add products, Please wait to be Accepted by our Team, usual wait time: 24hrs')
        return redirect(reverse('home'))
    if request.method == 'POST':  # this means the form has data
        form = Product_form(request.POST, request.FILES)  # get the form and it data
        if form.is_valid():  # check if it is valid
            brand = form.cleaned_data.get('brand')  # clean the data
            brand_name = form.cleaned_data.get('brand_name')  # clean the data
            image = form.cleaned_data.get('image')  # clean the data
            sku = form.cleaned_data.get('sku')
            product_name = form.cleaned_data.get('product_name')
            description = form.cleaned_data.get('description')  # clean the data
            max_quant = form.cleaned_data.get('max_quant')  # clean the data
            price = form.cleaned_data.get('price')  # clean the data
            form.save()  # save the data to the model
            messages.success(request, 'Your product has been added!')
            return redirect(reverse('brands'))
        else:  # form not valid so display message and retain the data entered
            form = Product_form(request.POST)
            messages.success(request, 'Error in creating your product, the form is not valid!')
            return render(request, 'upload/product-upload.html', {'form': form})
    else:  # the form has no data
        form = Product_form()  #produce a blank form
        return render(request, 'upload/product-upload.html', {'form': form})

@login_required
def edit_product(request, product_id):
    if not request.user.is_staff:
        messages.error(request, 'Only Store owners can edit products')
        return redirect(reverse('home'))
    product = get_object_or_404(Brand_products, pk=product_id)
    if request.method == 'POST':
        form = Product_form(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('brands'))
        else:
            messages.error(request, 'Failed to upload product, please ensure form is valid')
    else:
        form = Product_form(instance=product)
        messages.info(request, f'youare editing {product.product_name}')

    template = 'upload/edit_product.html'
    context ={
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    if not request.user.is_staff:
        messages.error(request, 'Only Store owners can delete products')
        return redirect(reverse('home'))
    product = get_object_or_404(Brand_products, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('brands'))


