from django.shortcuts import render
from .forms import Brand_form
# Create your views here.

def brand_upload(request):
    form = Brand_form()
    return render(request, "brand_upload.html", {"form": form})
