from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path

def home(request):
    return HttpResponse("Backend Running 🚀")

urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),

    path("api/auth/", include("accounts.urls")),
    path("api/", include("lockers.urls")),
    path("api/", include("reservations.urls")),
]