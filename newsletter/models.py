"""
imports:
"""
from django.db import models


class Subscribers(models.Model):
    """
    subscriber model for newletter submission
    """
    email = models.EmailField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class SendNews(models.Model):
    """
    send news model for sending a newsletter
    """
    title = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.title
