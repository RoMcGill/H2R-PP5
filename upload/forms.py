from django import forms
from brands.models import Brands


class Brand_form(forms.ModelForm):
    brand_name = forms.CharField(max_length=254, required=True)
    description = forms.CharField(required=True)
    image_url = forms.URLField(max_length=1024, required=True)
    image = forms.ImageField(required=True)

    class Meta:
        model = Brands
        fields = ['brand_name', 'description', 'image_url', 'image']




