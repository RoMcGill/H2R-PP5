from django.urls import path
from . import views

urlpatterns = [

        path('upload/', views.brand_upload, name='brand-upload'),
        path('upload-product/', views.product_upload, name='product-upload'),
        path('edit/<int:product_id>/', views.edit_product, name='edit_product'),

]
