"""View-функции для устройств."""

from django.http import HttpResponse

from homepage.views import page
from domain.device import Device
from domain.devices import find_device_by_id
from domain.storage import load_devices


def devices(request):
    """Список устройств."""
    devices_list = load_devices("data/devices.json")
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
    """Страница отдельного устройства."""
    devices_list = load_devices("data/devices.json")
    device: Device | None = find_device_by_id(devices_list, device_id)
    if device is None:
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
    cost = device.calculate_repair_cost(False)
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
            <p class="card-text">
                <strong>Стоимость ремонта:</strong> {cost} руб.
            </p>
            <a href="/devices/" class="btn btn-outline-secondary">
                ← к списку устройств
            </a>
        </div>
    </div>
    """
    return HttpResponse(page(str(device), content))
