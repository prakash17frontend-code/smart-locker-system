from django.utils import timezone
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Reservation
from .serializers import ReservationSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Reservation.objects.select_related("user", "locker").order_by("-created_at")

        if user.is_staff:
            return queryset

        return queryset.filter(user=user)

    def perform_create(self, serializer):
        reservation = serializer.save(
            user=self.request.user,
            status="ACTIVE",
        )

        locker = reservation.locker
        locker.status = "reserved"
        locker.save()

    @action(detail=True, methods=["put"], url_path="release")
    def release(self, request, pk=None):
        reservation = self.get_object()

        if not request.user.is_staff and reservation.user != request.user:
            return Response(
                {"detail": "You do not have permission to release this reservation."},
                status=status.HTTP_403_FORBIDDEN,
            )

        if reservation.status == "RELEASED":
            return Response(
                {"detail": "Reservation is already released."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        reservation.status = "RELEASED"
        reservation.released_at = timezone.now()
        reservation.save()

        locker = reservation.locker
        locker.status = "available"
        locker.save()

        return Response(
            {"detail": "Reservation released successfully."},
            status=status.HTTP_200_OK,
        )