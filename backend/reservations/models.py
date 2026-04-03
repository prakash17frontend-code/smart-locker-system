from django.conf import settings
from django.db import models
from lockers.models import Locker

class Reservation(models.Model):
    STATUS_CHOICES = (
        ("ACTIVE", "Active"),
        ("RELEASED", "Released"),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reservations",
    )
    locker = models.ForeignKey(
        Locker,
        on_delete=models.CASCADE,
        related_name="reservations",
    )
    reserved_until = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="ACTIVE")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    released_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.locker.locker_number}"