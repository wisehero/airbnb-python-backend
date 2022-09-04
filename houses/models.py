from django.db import models


# Create your models here.

class House(models.Model):
    """ Model Definition for houses"""

    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField()
    description = models.TextField()  # this is for long text
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(default=True)
