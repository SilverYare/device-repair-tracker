"""Функции работы с коллекцией заявок."""

from typing import Optional

from .client import Client
from .device import Device
from .master import Master
from .request import Request
from .status import RequestStatus


def create_request(
    requests: list[Request],
    request_id: int,
    device: Device,
    client: Client,
    is_urgent: bool = False,
) -> Request:
    """Создать заявку и добавить в коллекцию."""
    request = Request(request_id, device, client, is_urgent)
    requests.append(request)
    return request


def find_request_by_id(
    requests: list[Request], request_id: int
) -> Optional[Request]:
    """Найти заявку по id."""
    return next((r for r in requests if r.id == request_id), None)


def assign_master(
    requests: list[Request], request_id: int, master: Master
) -> bool:
    """Назначить мастера на заявку."""
    request = find_request_by_id(requests, request_id)
    if request is None:
        return False
    request.assign_master(master)
    return True


def change_status(
    requests: list[Request], request_id: int, new_status: RequestStatus
) -> bool:
    """Изменить статус заявки."""
    request = find_request_by_id(requests, request_id)
    if request is None:
        return False
    request.change_status(new_status)
    return True


def filter_requests_by_status(
    requests: list[Request], status: RequestStatus
) -> list[Request]:
    """Фильтр по статусу."""
    return [r for r in requests if r.status == status]


def sort_requests_by_cost(
    requests: list[Request], descending: bool = False
) -> list[Request]:
    """Сортировка по стоимости (lambda)."""
    return sorted(requests, key=lambda r: r.cost, reverse=descending)


def get_master_workload(
    requests: list[Request], master: Master
) -> int:
    """Количество активных заявок у мастера."""
    active = {
        RequestStatus.ACCEPTED,
        RequestStatus.DIAGNOSTICS,
        RequestStatus.IN_REPAIR,
    }
    return sum(
        1 for r in requests
        if r.master is master and r.status in active
    )


def show_requests(requests: list[Request]) -> None:
    """Вывод списка заявок."""
    if not requests:
        print("Заявки не найдены.")
        return
    for request in requests:
        print(request)
