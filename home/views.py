"""
imports:
"""
from django.shortcuts import render


def index(request):
    """
    view to return index page
    """
    return render(request, 'home/index.html')
