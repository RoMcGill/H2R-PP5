from django.db import models

# Create your models here.
class Mission(models.Model):
    """
    A class for contact us model
    """
    Why = models.CharField(max_length=9999)
    How = models.CharField(max_length=9999)

    def __str__(self):
        return self.Why + self.How