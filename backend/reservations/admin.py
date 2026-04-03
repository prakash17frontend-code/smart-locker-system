from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "locker",
        "reserved_until",
        "status",
        "created_at",
        "released_at",
    )
    list_filter = ("status",)
    search_fields = ("user__username", "locker__locker_number")