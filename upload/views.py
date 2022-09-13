from django.shortcuts import render, redirect
from .forms import Brand_form, Product_form
from django.contrib import messages


# Create your views here.

def brand_upload(request):
    if request.method == 'POST':  # this means the form has data
        form = Brand_form(request.POST, request.FILES)  # get the form and it data
        if form.is_valid():  # check if it is valid
            brand_name = form.cleaned_data.get('brand_name')  # clean the data
            description = form.cleaned_data.get('description')  # clean the data
            image = form.cleaned_data.get('image')  # clean the data
            form.save()  # save the data to the model
            messages.success(request, 'Your product has been added!')
            return redirect('upload/brand-upload.html')
        else:  # form not valid so display message and retain the data entered
            form = Brand_form(request.POST)
            messages.success(request, 'Error in creating your product, the form is not valid!')
            return render(request, 'upload/brand-upload.html', {'form': form})
    else:  # the form has no data
        form = Brand_form()  #produce a blank form
        return render(request, 'upload/brand-upload.html', {'form': form})


def product_upload(request):
    if request.method == 'POST':  # this means the form has data
        form = Product_form(request.POST, request.FILES)  # get the form and it data
        if form.is_valid():  # check if it is valid
            brand = form.cleaned_data.get_or_create('brand')  # clean the data
            brand_name = form.cleaned_data.get('brand_name')  # clean the data
            image = form.cleaned_data.get('image')  # clean the data
            sku = form.cleaned_data.get('sku')
            Product_name = form.cleaned_data.get('Product_name')
            description = form.cleaned_data.get('description')  # clean the data
            has_sizes = form.cleaned_data.get('has_sizes')  # clean the data
            price = form.cleaned_data.get('price')  # clean the data
            form.save()  # save the data to the model
            messages.success(request, 'Your product has been added!')
            return redirect('upload/product-upload.html')
        else:  # form not valid so display message and retain the data entered
            form = Product_form(request.POST)
            messages.success(request, 'Error in creating your product, the form is not valid!')
            return render(request, 'upload/product-upload.html', {'form': form})
    else:  # the form has no data
        form = Product_form()  #produce a blank form
        return render(request, 'upload/product-upload.html', {'form': form})

