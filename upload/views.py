from django.shortcuts import render, redirect
from .forms import Brand_form
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
