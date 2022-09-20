from django.shortcuts import render

# Create your views here.

def view_socials(request):
    """
    view to return social media page
    """
    return render(request, 'follow/follow.html')
