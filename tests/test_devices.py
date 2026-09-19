"""Тесты функций работы с устройствами."""

from devices import (
    add_device,
    find_device_by_id,
    find_devices_by_client,
    filter_devices_by_type,
)


def test_add_device():
    devices = []
    device = add_device(devices, "Иванов И.И.", "ноутбук", "Lenovo", "NB-1")
    assert len(devices) == 1
    assert device["id"] == 1
    assert device["client_name"] == "Иванов И.И."


def test_find_device_by_id():
    devices = []
    add_device(devices, "Иванов И.И.", "ноутбук", "Lenovo", "NB-1")
    assert find_device_by_id(devices, 1) is not None
    assert find_device_by_id(devices, 99) is None


def test_find_devices_by_client():
    devices = []
    add_device(devices, "Иванов И.И.", "ноутбук", "Lenovo", "NB-1")
    add_device(devices, "Петрова А.С.", "смартфон", "Samsung", "SM-2")
    found = find_devices_by_client(devices, "иванов")
    assert len(found) == 1
    assert found[0]["client_name"] == "Иванов И.И."


def test_filter_devices_by_type():
    devices = []
    add_device(devices, "Иванов И.И.", "ноутбук", "Lenovo", "NB-1")
    add_device(devices, "Петрова А.С.", "смартфон", "Samsung", "SM-2")
    laptops = filter_devices_by_type(devices, "ноутбук")
    assert len(laptops) == 1
    assert laptops[0]["model"] == "Lenovo"