from django.db import models
from common.models import CommonModel


# Create your models here.

class Experience(CommonModel):
    """ Experience Model Definition """

    country = models.CharField(
        max_length=50,
        default="한국"
    )
    city = models.CharField(
        max_length=80,
        default="서울"
    )
    name = models.CharField(
        max_length=250,
    )
    host = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE
    )
    price = models.PositiveIntegerField()
    address = models.CharField(
        max_length=250
    )
    start = models.TimeField()
    end = models.TimeField()
    description = models.TextField()
    perks = models.ManyToManyField(
        "experiences.Perk",
    )

    def __str__(self):
        return self.name


class Perk(CommonModel):
    name = models.CharField(
        max_length=100,
    )
    details = models.CharField(
        max_length=250,
        blank=True,
        default=""
    )
    explanation = models.TextField(
        blank=True,
        default=""
    )

    def __str__(self):
        return self.name
