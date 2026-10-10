"""Главная страница проекта."""

from django.http import HttpResponse


def index(request):
    """Приветственная страница."""
    return HttpResponse("Сервис отслеживания ремонта устройств")


def page_not_found(request, exception):
    """Страница 404."""
    return HttpResponse("Страница не найдена", status=404)