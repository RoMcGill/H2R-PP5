from django.shortcuts import render
from django.views import generic
from .models import Mission

# Create your views here.
class Mission(generic.ListView):
    queryset = Mission.objects.all
    template_name = 'mission/mission.html'





def mission(request):

    return render(request, 'mission/mission.html')
