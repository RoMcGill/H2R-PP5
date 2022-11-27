"""
imports:
"""
from django.db import models


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Mission(models.Model):
    """
    A class for contact us model
    """
    Why = models.TextField(max_length=9999)
    How = models.TextField(max_length=9999)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.Why + self.How
