from django.contrib import admin
from bookings.models import Booking


# Register your models here.


@admin.register(Booking)
class Booking(admin.ModelAdmin):
    list_display = (
        "kind",
        "user",
        "room",
        "experience",
        "check_in",
        "check_out",
        "experience_time",
        "guests",
    )
    list_filter = ("kind",)
