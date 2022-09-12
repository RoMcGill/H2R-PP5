from django.urls import path
from . import views

urlpatterns = [

        path("upload_form/", views.brand_upload, name="upload"),

]
