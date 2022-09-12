from django.urls import path
from . import views

urlpatterns = [

        path("brand_upload/", views.brand_upload, name="brand_upload"),

]
