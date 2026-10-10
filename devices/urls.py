"""Маршруты для устройств."""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.devices, name="devices"),
    path("<int:device_id>/", views.device_detail, name="device_detail"),
]
