"""View-функции для мастеров."""

from django.http import HttpResponse

from homepage.views import page
from models.master import Master
from models.masters import find_master_by_id
from models.storage import load_masters


def masters(request):
    """Список мастеров."""
    masters_list = load_masters("data/masters.json")
    items = ""
    for master in masters_list:
        items += (
            f'<li class="list-group-item">'
            f'<a href="/masters/{master.id}/">{master}</a>'
            f"</li>"
        )
    content = f"""
    <h1>Мастера</h1>
    <ul class="list-group">{items}</ul>
    """
    return HttpResponse(page("Мастера", content))


def master_detail(request, master_id):
    """Страница отдельного мастера."""
    masters_list = load_masters("data/masters.json")
    master: Master | None = find_master_by_id(masters_list, master_id)
    if master is None:
        content = """
        <h1 class="text-danger">Мастер не найден</h1>
        <a href="/masters/" class="btn btn-outline-secondary">
            ← к списку мастеров
        </a>
        """
        return HttpResponse(page("Мастер не найден", content), status=404)
    content = f"""
    <div class="card">
        <div class="card-body">
            <h5 class="card-title">{master.name}</h5>
            <p class="card-text"><strong>ID:</strong> {master.id}</p>
            <p class="card-text"><strong>Телефон:</strong> {master.phone}</p>
            <p class="card-text">
                <strong>Специализация:</strong> {master.specialization}
            </p>
            <a href="/masters/" class="btn btn-outline-secondary">
                ← к списку мастеров
            </a>
        </div>
    </div>
    """
    return HttpResponse(page(str(master), content))