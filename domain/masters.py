"""Функции работы с коллекцией мастеров."""

from typing import Optional

from .master import Master


def add_master(
    masters: list[Master],
    master_id: int,
    name: str,
    phone: str,
    specialization: str,
) -> Master:
    """Создать мастера и добавить в коллекцию."""
    master = Master(master_id, name, phone, specialization)
    masters.append(master)
    return master


def find_master_by_id(
    masters: list[Master], master_id: int
) -> Optional[Master]:
    """Найти мастера по id."""
    return next((m for m in masters if m.id == master_id), None)


def find_masters_by_specialization(
    masters: list[Master], specialization: str
) -> list[Master]:
    """Найти мастеров по специализации."""
    spec = specialization.strip().lower()
    return [m for m in masters if m.specialization.lower() == spec]


def show_masters(masters: list[Master]) -> None:
    """Вывод списка мастеров."""
    if not masters:
        print("Мастера не найдены.")
        return
    for master in masters:
        print(master)