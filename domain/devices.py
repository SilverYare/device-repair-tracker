"""Функции работы с коллекцией устройств."""

from typing import Optional

from .device import Device


def add_device(
    devices: list[Device],
    device_id: int,
    model: str,
    serial_number: str,
    device_type: str = "ноутбук",
) -> Device:
    """Создать устройство нужного типа и добавить в коллекцию."""
    from .device import Laptop, Smartphone, Tablet, TV

    mapping = {
        "ноутбук": Laptop,
        "смартфон": Smartphone,
        "планшет": Tablet,
        "телевизор": TV,
    }
    device_cls = mapping.get(device_type.strip().lower(), Laptop)
    device = device_cls(device_id, model, serial_number)
    devices.append(device)
    return device


def find_device_by_id(
    devices: list[Device], device_id: int
) -> Optional[Device]:
    """Найти устройство по id."""
    return next((d for d in devices if d.id == device_id), None)


def find_devices_by_client(
    devices: list[Device], query: str
) -> list[Device]:
    """Поиск устройств по подстроке в модели."""
    query = query.strip().lower()
    return [d for d in devices if query in d.model.lower()]


def sort_devices_by_model(devices: list[Device]) -> list[Device]:
    """Сортировка устройств по модели (lambda)."""
    return sorted(devices, key=lambda d: d.model)


def show_devices(devices: list[Device]) -> None:
    """Вывод списка устройств."""
    if not devices:
        print("Устройства не найдены.")
        return
    for device in devices:
        print(device)

def filter_devices_by_type(
    devices: list[Device], device_type: str
) -> list[Device]:
    """Отобрать устройства по типу."""
    device_type = device_type.strip().lower()
    return [d for d in devices if d.device_type == device_type]