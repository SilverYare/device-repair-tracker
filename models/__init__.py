"""Пакет классов предметной области."""

from .person import Person
from .client import Client
from .master import Master
from .device import Device, Laptop, Smartphone, Tablet, TV
from .status import RequestStatus
from .request import Request

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