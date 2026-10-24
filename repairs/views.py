from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from homepage.views import page
from .models import Request
from .serializers import RequestSerializer


def requests_list(request):
    """Страница со списком заявок."""
    requests_list = Request.objects.all()
    items = ""
    for req in requests_list:
        status_class = "bg-secondary" if req.status_code == 5 else "bg-success"
        items += (
            f'<li class="list-group-item d-flex '
            f'justify-content-between align-items-center">'
            f'<a href="/requests/{req.id}/">'
            f"{req.client_name} — {req.device.model}</a>"
            f'<span class="badge {status_class}">'
            f"Код: {req.status_code}</span>"
            f"</li>"
        )
    content = f"""
    <h1>Заявки на ремонт</h1>
    <ul class="list-group">{items}</ul>
    """
    return HttpResponse(page("Заявки", content))


def request_detail(request, request_id):
    """Страница с деталями заявки."""
    try:
        req = Request.objects.get(id=request_id)
    except Request.DoesNotExist:
        content = """
        <h1 class="text-danger">Заявка не найдена</h1>
        <a href="/requests/" class="btn btn-outline-secondary">
            ← к списку заявок
        </a>
        """
        return HttpResponse(
            page("Заявка не найдена", content),
            status=404,
        )

    master_name = req.master.name if req.master else "не назначен"
    content = f"""
    <div class="card">
        <div class="card-body">
            <h5 class="card-title">Заявка №{req.id}</h5>
            <p class="card-text">
                <strong>Клиент:</strong> {req.client_name}
            </p>
            <p class="card-text">
                <strong>Устройство:</strong>
                {req.device.device_type} {req.device.model}
            </p>
            <p class="card-text">
                <strong>Мастер:</strong> {master_name}
            </p>
            <p class="card-text">
                <strong>Статус:</strong> Код {req.status_code}
            </p>
            <a href="/requests/" class="btn btn-outline-secondary">
                ← к списку заявок
            </a>
        </div>
    </div>
    """
    return HttpResponse(page(f"Заявка №{req.id}", content))


@api_view(["GET", "POST"])
def api_requests(request):
    """API для получения и создания заявок."""
    if request.method == "GET":
        requests_qs = Request.objects.all()
        serializer = RequestSerializer(requests_qs, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
