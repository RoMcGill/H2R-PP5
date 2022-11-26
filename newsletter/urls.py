from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

         path('newsletter/', views.Newsletter, name='newsletter'),
         path(
            'send_newsletter/',
            views.send_newsletter,
            name='send-newsletter'),

]
