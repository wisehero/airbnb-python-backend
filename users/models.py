from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)
    # Own field
    name = models.CharField(max_length=150, default="")
    is_host = models.BooleanField(default=False)
