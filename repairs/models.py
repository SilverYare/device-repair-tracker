from django.db import models

from devices.models import Device
from masters.models import Master


class Request(models.Model):
    client_name = models.CharField(max_length=100)
    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE
    )
    master = models.ForeignKey(
        Master,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    is_urgent = models.BooleanField(default=False)
    status_code = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Заявка №{self.id} - {self.client_name}"
