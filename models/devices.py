"""Функции для работы с устройствами."""

from typing import Optional


def add_device(
    devices: list[dict],
    client_name: str,
    device_type: str,
    model: str,
    serial_number: str,
) -> dict:
    """Добавить устройство в список. Вернуть созданную запись."""
    new_id = max((device["id"] for device in devices), default=0) + 1
    device = {
        "id": new_id,
        "client_name": client_name,
        "device_type": device_type,
        "model": model,
        "serial_number": serial_number,
    }
    devices.append(device)
    return device


def find_device_by_id(devices: list[dict], device_id: int) -> Optional[dict]:
    """Найти устройство по id. Вернуть None, если не найдено."""
    for device in devices:
        if device["id"] == device_id:
            return device
    return None


def find_devices_by_client(devices: list[dict], query: str) -> list[dict]:
    """Найти устройства по подстроке в имени клиента."""
    query = query.strip().lower()
    return [d for d in devices if query in d["client_name"].lower()]


def filter_devices_by_type(devices: list[dict], device_type: str) -> list[dict]:
    """Отобрать устройства по типу."""
    device_type = device_type.strip().lower()
    return [d for d in devices if d["device_type"].lower() == device_type]


def sort_devices_by_client(devices: list[dict]) -> list[dict]:
    """Отсортировать устройства по имени клиента (lambda-ключ)."""
    return sorted(devices, key=lambda d: d["client_name"])