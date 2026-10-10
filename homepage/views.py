"""Главная страница и общий каркас страниц проекта."""

from django.http import HttpResponse

BOOTSTRAP_CSS = (
    "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
)


def page(title: str, content: str) -> str:
    """Собрать HTML-документ с общим каркасом."""
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{title}</title>
    <link rel="stylesheet" href="{BOOTSTRAP_CSS}">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark mb-4">
        <div class="container">
            <a class="navbar-brand" href="/">Ремонт устройств</a>
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link" href="/devices/">Устройства</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/masters/">Мастера</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/requests/">Заявки</a>
                </li>
            </ul>
        </div>
    </nav>
    <div class="container">
        {content}
    </div>
</body>
</html>"""


def index(request):
    """Главная страница."""
    content = """
    <h1 class="display-4">Сервис отслеживания ремонта устройств</h1>
    <p class="lead">Учёт устройств, заявок на ремонт и работы мастеров.</p>
    <p>Основные разделы:</p>
    <a href="/devices/" class="btn btn-primary me-2">Устройства</a>
    <a href="/masters/" class="btn btn-secondary me-2">Мастера</a>
    <a href="/requests/" class="btn btn-success">Заявки</a>
    """
    return HttpResponse(page("Ремонт устройств", content))


def page_not_found(request, exception):
    """Страница 404 в едином стиле."""
    content = """
    <h1 class="text-danger">404 — страница не найдена</h1>
    <p>Проверьте адрес или вернитесь на главную.</p>
    <a href="/" class="btn btn-primary">На главную</a>
    """
    return HttpResponse(
        page("404 — страница не найдена", content),
        status=404,
    )
