from django.contrib import admin
from .models import House


# Register your models here.
@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    pass
