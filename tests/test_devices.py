"""Тесты устройств и функций работы с ними."""

from domain.device import Laptop, Smartphone, Tablet, TV
from domain.devices import (
    add_device,
    find_device_by_id,
    filter_devices_by_type,
    sort_devices_by_model,
)


def test_device_creation():
    laptop = Laptop(1, "Lenovo", "NB-1")
    assert laptop.id == 1
    assert laptop.model == "Lenovo"
    assert laptop.device_type == "ноутбук"


def test_device_cost():
    laptop = Laptop(1, "Lenovo", "NB-1")
    assert laptop.calculate_repair_cost(False) == 1300.0
    assert laptop.calculate_repair_cost(True) == 1950.0


def test_smartphone_coefficient():
    phone = Smartphone(2, "Samsung", "SM-2")
    assert phone.calculate_repair_cost(False) == 1000.0


def test_tv_coefficient():
    tv = TV(3, "LG", "TV-3")
    assert tv.calculate_repair_cost(False) == 1400.0


def test_tablet_coefficient():
    tablet = Tablet(4, "iPad", "TB-4")
    assert tablet.calculate_repair_cost(False) == 1100.0


def test_add_and_find_device():
    devices = []
    add_device(devices, 1, "Lenovo", "NB-1", "ноутбук")
    add_device(devices, 2, "Samsung", "SM-2", "смартфон")
    assert len(devices) == 2
    assert find_device_by_id(devices, 1).model == "Lenovo"
    assert find_device_by_id(devices, 99) is None


def test_filter_by_type():
    devices = []
    add_device(devices, 1, "Lenovo", "NB-1", "ноутбук")
    add_device(devices, 2, "Samsung", "SM-2", "смартфон")
    laptops = filter_devices_by_type(devices, "ноутбук")
    assert len(laptops) == 1
    assert laptops[0].model == "Lenovo"


def test_sort_by_model():
    devices = []
    add_device(devices, 1, "Zebra", "Z-1", "ноутбук")
    add_device(devices, 2, "Apple", "A-2", "смартфон")
    sorted_devices = sort_devices_by_model(devices)
    assert sorted_devices[0].model == "Apple"
