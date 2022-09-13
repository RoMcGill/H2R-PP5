from django import forms
from brands.models import Brands


class Brand_form(forms.ModelForm):
    brand_name = forms.CharField(max_length=254, required=False)
    description = forms.CharField(required=False)
    image = forms.ImageField(required=False)


    class Meta:
        model = Brands
        fields = ['brand_name', 'description', 'image']




