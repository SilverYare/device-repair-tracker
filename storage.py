"""Загрузка и сохранение данных в JSON."""

import json
import os
from typing import Any

from domain import Client, Device, Master, Request


def load_json(filename: str) -> list[dict[str, Any]]:
    """Загрузить список словарей из JSON."""
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError) as error:
        print(f"Ошибка чтения {filename}: {error}")
        return []


def save_json(filename: str, data: list[dict[str, Any]]) -> None:
    """Сохранить список словарей в JSON."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except OSError as error:
        print(f"Ошибка записи {filename}: {error}")


def load_clients(filename: str) -> list[Client]:
    return [Client.from_data(d) for d in load_json(filename)]


def save_clients(filename: str, clients: list[Client]) -> None:
    save_json(filename, [c.to_data() for c in clients])


def load_masters(filename: str) -> list[Master]:
    return [Master.from_data(d) for d in load_json(filename)]


def save_masters(filename: str, masters: list[Master]) -> None:
    save_json(filename, [m.to_data() for m in masters])


def load_devices(filename: str) -> list[Device]:
    return [Device.from_data(d) for d in load_json(filename)]


def save_devices(filename: str, devices: list[Device]) -> None:
    save_json(filename, [d.to_data() for d in devices])


def load_requests(
    filename: str,
    devices: list[Device],
    clients: list[Client],
    masters: list[Master],
) -> list[Request]:
    """Загрузить заявки, восстановив связи с устройствами, клиентами и мастерами."""
    requests: list[Request] = []
    for data in load_json(filename):
        try:
            requests.append(Request.from_data(data, devices, clients, masters))
        except ValueError as error:
            print(f"Пропущена заявка: {error}")
    return requests


def save_requests(filename: str, requests: list[Request]) -> None:
    save_json(filename, [r.to_data() for r in requests])
