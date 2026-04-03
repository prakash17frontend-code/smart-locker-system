from rest_framework.routers import DefaultRouter
from .views import LockerViewSet

router = DefaultRouter()
router.register(r"lockers", LockerViewSet, basename="lockers")

urlpatterns = router.urls