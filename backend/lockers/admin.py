from django.contrib import admin
from .models import Locker

@admin.register(Locker)
class LockerAdmin(admin.ModelAdmin):
    list_display = ("id", "locker_number", "location", "status", "created_at")
    search_fields = ("locker_number", "location")
    list_filter = ("status",)