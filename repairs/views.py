"""View-функции для заявок на ремонт."""

from django.http import HttpResponse

from homepage.views import page
from domain.request import Request
from domain.requests import find_request_by_id
from domain.storage import (
    load_clients,
    load_devices,
    load_masters,
    load_requests,
)

DATA = "data"


def _load_all():
    devices = load_devices(f"{DATA}/devices.json")
    clients = load_clients(f"{DATA}/clients.json")
    masters = load_masters(f"{DATA}/masters.json")
    return load_requests(
        f"{DATA}/requests.json", devices, clients, masters
    )


def requests_list(request):
    """Список заявок."""
    items = ""
    for req in _load_all():
        status_class = (
            "bg-secondary" if req.status.code == 5 else "bg-success"
        )
        items += (
            f'<li class="list-group-item d-flex '
            f'justify-content-between align-items-center">'
            f'<a href="/requests/{req.id}/">'
            f"{req.client.name} — {req.device.model}</a>"
            f'<span class="badge {status_class}">{req.status}</span>'
            f"</li>"
        )
    content = f"""
    <h1>Заявки на ремонт</h1>
    <ul class="list-group">{items}</ul>
    """
    return HttpResponse(page("Заявки", content))


def request_detail(request, request_id):
    """Страница отдельной заявки."""
    request_obj: Request | None = find_request_by_id(
        _load_all(), request_id
    )
    if request_obj is None:
        content = """
        <h1 class="text-danger">Заявка не найдена</h1>
        <a href="/requests/" class="btn btn-outline-secondary">
            ← к списку заявок
        </a>
        """
        return HttpResponse(page("Заявка не найдена", content), status=404)
    master_text = (
        request_obj.master.name if request_obj.master else "не назначен"
    )
    content = f"""
    <div class="card">
        <div class="card-body">
            <h5 class="card-title">Заявка №{request_obj.id}</h5>
            <p class="card-text">
                <strong>Клиент:</strong> {request_obj.client.name}
            </p>
            <p class="card-text">
                <strong>Устройство:</strong>
                {request_obj.device.device_type} {request_obj.device.model}
            </p>
            <p class="card-text">
                <strong>Мастер:</strong> {master_text}
            </p>
            <p class="card-text">
                <strong>Статус:</strong> {request_obj.status}
            </p>
            <p class="card-text">
                <strong>Стоимость:</strong> {request_obj.cost} руб.
            </p>
            <a href="/requests/" class="btn btn-outline-secondary">
                ← к списку заявок
            </a>
        </div>
    </div>
    """
    return HttpResponse(page(f"Заявка №{request_obj.id}", content))
