from django.shortcuts import render
from .models import Device
# ... импорты API ...

def devices(request):
    devices_list = Device.objects.all()
    return render(request, "devices/device_list.html", {"devices": devices_list})

def device_detail(request, device_id):
    device = Device.objects.filter(id=device_id).first()
    return render(request, "devices/device_detail.html", {"device": device}, status=404 if device is None else 200)