from django.shortcuts import render
from .models import Request
# ... импорты API ...

def requests_list(request):
    requests_qs = Request.objects.all()
    return render(request, "repairs/request_list.html", {"requests": requests_qs})

def request_detail(request, request_id):
    req = Request.objects.filter(id=request_id).first()
    return render(request, "repairs/request_detail.html", {"request": req}, status=404 if req is None else 200)