"""Тесты функций работы с заявками."""

from requests import (
    calculate_repair_cost,
    get_request_status,
    create_request,
    assign_master,
    change_status,
    get_master_workload,
)


def test_calculate_repair_cost():
    assert calculate_repair_cost("ноутбук", False) == 1300.0
    assert calculate_repair_cost("смартфон", True) == 1500.0
    assert calculate_repair_cost("неизвестно", False) == 1000.0


def test_get_request_status():
    assert get_request_status(1) == "Принята"
    assert get_request_status(5) == "Выдана"
    assert get_request_status(99) == "Неизвестный статус"


def test_create_request():
    requests = []
    request = create_request(requests, device_id=1, device_type="ноутбук",
                             is_urgent=False)
    assert len(requests) == 1
    assert request["id"] == 1
    assert request["cost"] == 1300.0


def test_assign_master_and_change_status():
    requests = []
    create_request(requests, 1, "ноутбук", False)
    assert assign_master(requests, 1, 5) is True
    assert requests[0]["master_id"] == 5
    assert change_status(requests, 1, 3) is True
    assert requests[0]["status_code"] == 3


def test_get_master_workload():
    requests = []
    create_request(requests, 1, "ноутбук", False)
    create_request(requests, 2, "смартфон", False)
    assign_master(requests, 1, 1)
    assign_master(requests, 2, 1)
    change_status(requests, 2, 5)  # выдана — не активная
    assert get_master_workload(requests, 1) == 1