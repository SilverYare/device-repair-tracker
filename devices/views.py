"""View-функции для устройств."""

from django.http import HttpResponse


def devices(request):
    return HttpResponse("Список устройств")


def device_detail(request, device_id):
    return HttpResponse(f"Устройство {device_id}")