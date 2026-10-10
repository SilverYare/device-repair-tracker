"""Маршрутизация верхнего уровня."""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("homepage.urls")),
    path("devices/", include("devices.urls")),
    path("masters/", include("masters.urls")),
    path("requests/", include("repairs.urls")),
]

handler404 = "homepage.views.page_not_found"