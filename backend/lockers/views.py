from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Locker
from .permissions import IsAdminOrReadOnly
from .serializers import LockerSerializer

class LockerViewSet(viewsets.ModelViewSet):
    queryset = Locker.objects.all().order_by("locker_number")
    serializer_class = LockerSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]