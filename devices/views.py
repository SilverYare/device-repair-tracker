from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from homepage.views import page
from .models import Device
from .serializers import DeviceSerializer


def devices(request):
    """Страница со списком устройств."""
    devices_list = Device.objects.all()
    items = ""
    for device in devices_list:
        items += (
            f'<li class="list-group-item">'
            f'<a href="/devices/{device.id}/">{device}</a>'
            f"</li>"
        )
    content = f"""
    <h1>Устройства</h1>
    <ul class="list-group">{items}</ul>
    """
    return HttpResponse(page("Устройства", content))


def device_detail(request, device_id):
    """Страница с деталями устройства."""
    try:
        device = Device.objects.get(id=device_id)
    except Device.DoesNotExist:
        content = """
        <h1 class="text-danger">Устройство не найдено</h1>
        <a href="/devices/" class="btn btn-outline-secondary">
            ← к списку устройств
        </a>
        """
        return HttpResponse(
            page("Устройство не найдено", content),
            status=404,
        )

    content = f"""
    <div class="card">
        <div class="card-body">
            <h5 class="card-title">
                {device.device_type} {device.model}
            </h5>
            <p class="card-text"><strong>ID:</strong> {device.id}</p>
            <p class="card-text">
                <strong>Серийный номер:</strong> {device.serial_number}
            </p>
            <a href="/devices/" class="btn btn-outline-secondary">
                ← к списку устройств
            </a>
        </div>
    </div>
    """
    return HttpResponse(page(str(device), content))


@api_view(["GET"])
def api_devices(request):
    """API для получения списка устройств."""
    devices_list = Device.objects.all()
    serializer = DeviceSerializer(devices_list, many=True)
    return Response(serializer.data)
