from django.shortcuts import render
from django.views import generic
from .models import Mission


class MissionList(generic.ListView):
    queryset = Mission.objects.all()
    template_name = 'mission/mission.html'
