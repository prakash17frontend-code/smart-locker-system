from django.utils import timezone
from rest_framework import serializers
from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source="user.username", read_only=True)
    locker_number = serializers.CharField(source="locker.locker_number", read_only=True)

    class Meta:
        model = Reservation
        fields = [
            "id",
            "user",
            "user_name",
            "locker",
            "locker_number",
            "reserved_until",
            "status",
            "created_at",
            "updated_at",
            "released_at",
        ]
        read_only_fields = [
            "id",
            "user",
            "user_name",
            "locker_number",
            "status",
            "created_at",
            "updated_at",
            "released_at",
        ]

    def validate(self, attrs):
        locker = attrs.get("locker")
        reserved_until = attrs.get("reserved_until")

        if not locker:
            raise serializers.ValidationError({"locker": "Locker is required."})

        if not reserved_until:
            raise serializers.ValidationError(
                {"reserved_until": "Reservation end time is required."}
            )

        if reserved_until <= timezone.now():
            raise serializers.ValidationError(
                {"reserved_until": "reserved_until must be in the future."}
            )

        existing_reservation = Reservation.objects.filter(
            locker=locker,
            status="ACTIVE",
            released_at__isnull=True,
        ).exists()

        if existing_reservation:
            raise serializers.ValidationError(
                {"locker": "This locker already has an active reservation."}
            )

        if locker.status != "available":
            raise serializers.ValidationError({"locker": "Locker is not available."})

        return attrs