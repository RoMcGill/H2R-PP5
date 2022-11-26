"""
imports
"""
from django.db import models


class Contact(models.Model):
    """
    A class for contact us model
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.subject + " - " + self.email
