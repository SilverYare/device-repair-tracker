"""Тесты заявок и функций работы с ними."""

from domain.client import Client
from domain.device import Laptop
from domain.master import Master
from domain.request import Request
from domain.requests import (
    assign_master,
    change_status,
    create_request,
    get_master_workload,
    sort_requests_by_cost,
)
from domain.status import RequestStatus


def make_fixtures():
    laptop = Laptop(1, "Lenovo", "NB-1")
    client = Client(1, "Иван", "+7-900", "ivan@example.com")
    master = Master(1, "Пётр", "+7-900", "ноутбуки")
    return laptop, client, master


def test_request_creation():
    laptop, client, _ = make_fixtures()
    request = Request(1, laptop, client, is_urgent=False)
    assert request.id == 1
    assert request.device is laptop
    assert request.client is client
    assert request.status == RequestStatus.ACCEPTED
    assert request.cost == 1300.0


def test_assign_master():
    laptop, client, master = make_fixtures()
    request = Request(1, laptop, client)
    request.assign_master(master)
    assert request.master is master


def test_change_status():
    laptop, client, _ = make_fixtures()
    request = Request(1, laptop, client)
    request.change_status(RequestStatus.IN_REPAIR)
    assert request.status == RequestStatus.IN_REPAIR


def test_create_and_assign_via_functions():
    laptop, client, master = make_fixtures()
    requests = []
    create_request(requests, 1, laptop, client, is_urgent=False)
    assert len(requests) == 1
    assert assign_master(requests, 1, master)
    assert requests[0].master is master


def test_get_master_workload():
    laptop, client, master = make_fixtures()
    requests = []
    create_request(requests, 1, laptop, client)
    create_request(requests, 2, laptop, client)
    assign_master(requests, 1, master)
    assign_master(requests, 2, master)
    change_status(requests, 2, RequestStatus.ISSUED)
    assert get_master_workload(requests, master) == 1


def test_sort_requests_by_cost():
    laptop, client, _ = make_fixtures()
    requests = []
    create_request(requests, 1, laptop, client, is_urgent=True)
    create_request(requests, 2, laptop, client, is_urgent=False)
    sorted_requests = sort_requests_by_cost(requests)
    assert sorted_requests[0].cost <= sorted_requests[1].cost
