"""Пакет классов предметной области."""

from domain.person import Person
from domain.client import Client
from domain.master import Master
from domain.device import Device, Laptop, Smartphone, Tablet, TV
from domain.status import RequestStatus
from domain.request import Request

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

