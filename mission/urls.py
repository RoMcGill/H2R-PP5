from django.urls import path
from . import views

urlpatterns = [

       path('mission/', views.MissionList.as_view(), name='mission')
]