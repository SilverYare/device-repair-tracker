from django.db import models


class Device(models.Model):
    model = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=50)
    DEVICE_TYPES = [
        ('laptop', 'Ноутбук'),
        ('smartphone', 'Смартфон'),
        ('tablet', 'Планшет'),
        ('tv', 'Телевизор'),
    ]
    device_type = models.CharField(max_length=20, choices=DEVICE_TYPES)

    def __str__(self):
        return f"{self.device_type} {self.model}"
