from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    """
    view to show list of blog posts
    """
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/blog.html'
