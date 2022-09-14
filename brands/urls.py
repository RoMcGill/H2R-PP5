from django.urls import path
from . import views

urlpatterns = [

       path('', views.brands, name='brands'),
       path('<brand_id>', views.brand_detail, name='brand_detail'),
       path('<brand_product_id>', views.brand_detail, name='brand_product'),
       # path('product_detail', views.product_detail, name='product_detail'),
]
