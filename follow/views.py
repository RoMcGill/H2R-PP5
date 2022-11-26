from django.shortcuts import render


def view_socials(request):
    """
    view to return social media page
    """
    return render(request, 'follow/follow.html')
