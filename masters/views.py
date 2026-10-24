from django.shortcuts import render

from .models import Master


def masters(request):
    """Страница со списком мастеров."""
    masters_list = Master.objects.all()
    context = {"masters": masters_list}
    return render(request, "masters/master_list.html", context)


def master_detail(request, master_id):
    """Страница с деталями мастера."""
    master = Master.objects.filter(id=master_id).first()
    context = {"master": master}
    status_code = 404 if master is None else 200
    return render(
        request,
        "masters/master_detail.html",
        context,
        status=status_code,
    )
