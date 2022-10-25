from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    class LanguageChoices(models.TextChoices):
        KR = ("kr", "Korean")
        EN = ("en", "English")

    class CurrencyChoices(models.TextChoices):
        WON = ("won", "Korean won")
        USD = ("usd", "Dollar")

    first_name = models.CharField(max_length=150,
                                  editable=False)
    last_name = models.CharField(max_length=150,
                                 editable=False)
    # Own field
    avatar = models.URLField(blank=True)  # poetry install Pillow
    name = models.CharField(
        max_length=150,
        default="")
    is_host = models.BooleanField(default=False)
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices)
    language = models.CharField(
        max_length=2,
        choices=LanguageChoices.choices)
    currency = models.CharField(
        max_length=5,
        choices=CurrencyChoices.choices
    )
