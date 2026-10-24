from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Request
from .serializers import RequestSerializer


def requests_list(request):
    """Страница со списком заявок."""
    requests_qs = Request.objects.all()
    context = {"requests": requests_qs}
    return render(request, "repairs/request_list.html", context)


def request_detail(request, request_id):
    """Страница с деталями заявки."""
    req = Request.objects.filter(id=request_id).first()
    context = {"request": req}
    status_code = 404 if req is None else 200
    return render(
        request,
        "repairs/request_detail.html",
        context,
        status=status_code,
    )


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
