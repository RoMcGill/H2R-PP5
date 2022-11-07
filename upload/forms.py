from django import forms
from brands.models import Brands, Brand_products
brands = Brands.objects.all()


class Brand_form(forms.ModelForm):
    brand_email = forms.EmailField(max_length=254, required=True)
    brand_name = forms.CharField(max_length=254, required=False)
    description = forms.CharField(required=False)
    image = forms.ImageField(required=False)


    class Meta:
        model = Brands
        fields = ['brand_name', 'brand_email', 'description', 'image']



class Product_form(forms.ModelForm):
    brand_name = forms.CharField(max_length=254, required=False)
    brand = forms.ModelChoiceField(queryset=Brands.objects.all(),
                                    to_field_name = 'brand_name',
                                    empty_label="Select your brand")
    sku = forms.CharField(max_length=254, required=False)
    product_name = forms.CharField(max_length=254, required=False)
    description = forms.CharField(required=False)
    max_quant = forms.IntegerField(required=True)
    price = forms.DecimalField(max_digits=6, decimal_places=2)
    image = forms.ImageField(required=False)


    class Meta:
        model = Brand_products
        fields = ['brand_name', 'brand', 'sku', 'product_name', 'description', 'max_quant', 'price', 'image']






