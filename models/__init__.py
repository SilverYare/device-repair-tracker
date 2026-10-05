"""Пакет классов предметной области."""

from models.person import Person
from models.client import Client
from models.master import Master
from models.device import Device, Laptop, Smartphone, Tablet, TV
from models.status import RequestStatus
from models.request import Request

__all__ = [
    "Person",
    "Client",
    "Master",
    "Device",
    "Laptop",
    "Smartphone",
    "Tablet",
    "TV",
    "RequestStatus",
    "Request",
]