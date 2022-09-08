from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

       path('brands/', views.brands, name='brands')
]
