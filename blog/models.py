from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    """
    models for blog post
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=9999)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        """
        display most recent createed first
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        return title of blog in admin
        """
        return self.title
