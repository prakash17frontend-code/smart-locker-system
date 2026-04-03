from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Extra Fields", {"fields": ("name", "role", "created_at", "updated_at")}),
    )
    readonly_fields = ("created_at", "updated_at")