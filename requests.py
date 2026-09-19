"""Функции для работы с заявками на ремонт."""

from typing import Optional

BASE_PRICE = 1000.0
URGENT_MULTIPLIER = 1.5


def calculate_repair_cost(device_type: str, is_urgent: bool) -> float:
    """Рассчитать предварительную стоимость ремонта."""
    device_type = device_type.strip().lower()

    if device_type == "ноутбук":
        coefficient = 1.3
    elif device_type == "смартфон":
        coefficient = 1.0
    elif device_type == "планшет":
        coefficient = 1.1
    elif device_type == "телевизор":
        coefficient = 1.4
    else:
        coefficient = 1.0

    cost = BASE_PRICE * coefficient
    if is_urgent:
        cost *= URGENT_MULTIPLIER
    return round(cost, 2)


def get_request_status(status_code: int) -> str:
    """Вернуть текстовый статус заявки по коду (функция из ПР1)."""
    if status_code == 1:
        return "Принята"
    elif status_code == 2:
        return "Диагностика"
    elif status_code == 3:
        return "В ремонте"
    elif status_code == 4:
        return "Готова к выдаче"
    elif status_code == 5:
        return "Выдана"
    return "Неизвестный статус"


def create_request(
    requests: list[dict],
    device_id: int,
    device_type: str,
    is_urgent: bool,
    master_id: Optional[int] = None,
) -> dict:
    """Создать заявку на ремонт."""
    new_id = max((r["id"] for r in requests), default=0) + 1
    request = {
        "id": new_id,
        "device_id": device_id,
        "master_id": master_id,
        "status_code": 1,
        "is_urgent": is_urgent,
        "cost": calculate_repair_cost(device_type, is_urgent),
    }
    requests.append(request)
    return request


def find_request_by_id(requests: list[dict], request_id: int) -> Optional[dict]:
    """Найти заявку по id."""
    for request in requests:
        if request["id"] == request_id:
            return request
    return None


def assign_master(
    requests: list[dict], request_id: int, master_id: int
) -> bool:
    """Назначить мастера на заявку. Вернуть True при успехе."""
    request = find_request_by_id(requests, request_id)
    if request is None:
        return False
    request["master_id"] = master_id
    return True


def change_status(
    requests: list[dict], request_id: int, new_status_code: int
) -> bool:
    """Изменить статус заявки. Вернуть True при успехе."""
    if new_status_code not in (1, 2, 3, 4, 5):
        return False
    request = find_request_by_id(requests, request_id)
    if request is None:
        return False
    request["status_code"] = new_status_code
    return True


def filter_requests_by_status(
    requests: list[dict], status_code: int
) -> list[dict]:
    """Отобрать заявки по статусу."""
    return [r for r in requests if r["status_code"] == status_code]


def sort_requests_by_cost(
    requests: list[dict], descending: bool = False
) -> list[dict]:
    """Отсортировать заявки по стоимости."""
    return sorted(requests, key=lambda r: r["cost"], reverse=descending)


def get_master_workload(requests: list[dict], master_id: int) -> int:
    """Количество активных заявок мастера (статусы 1–3)."""
    return sum(
        1
        for r in requests
        if r["master_id"] == master_id and r["status_code"] in (1, 2, 3)
    )