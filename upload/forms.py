from django.forms import ModelForm
from brands.models import Brands


class Brand_form(ModelForm):
    class Meta:
        model = Brands
        fields = ['brand_name', 'description', 'image_url', 'image']


form = Brand_form()

# Create a form instance from POST data.


# Save a new Article object from the form's data.
new_brand = Brand_form()




