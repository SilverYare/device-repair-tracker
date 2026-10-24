"""Маршруты для заявок на ремонт."""

from django.urls import path

from . import views

app_name = "repairs"

urlpatterns = [
    path("", views.requests_list, name="requests_list"),
    path(
        "<int:request_id>/",
        views.request_detail,
        name="request_detail",
    ),
]
