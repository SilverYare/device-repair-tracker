"""Маршруты для мастеров."""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.masters, name="masters"),
    path("<int:master_id>/", views.master_detail, name="master_detail"),
]
