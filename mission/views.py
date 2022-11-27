"""
imports:
"""
from django.shortcuts import render
from django.views import generic
from .models import Mission


class MissionList(generic.ListView):
    """
    view to show how and why content created in the backend
    """
    queryset = Mission.objects.all()
    template_name = 'mission/mission.html'
