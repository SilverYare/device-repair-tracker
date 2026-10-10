"""View-функции для мастеров."""

from django.http import HttpResponse


def masters(request):
    return HttpResponse("Список мастеров")


def master_detail(request, master_id):
    return HttpResponse(f"Мастер {master_id}")