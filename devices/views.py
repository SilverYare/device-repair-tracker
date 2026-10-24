from django.shortcuts import render

from .models import Device

# ... импорты API ...


def devices(request):
    devices_list = Device.objects.all()
    context = {"devices": devices_list}
    return render(request, "devices/device_list.html", context)


def device_detail(request, device_id):
    device = Device.objects.filter(id=device_id).first()
    context = {"device": device}
    status_code = 404 if device is None else 200
    return render(
        request,
        "devices/device_detail.html",
        context,
        status=status_code,
    )
