"""Функции для работы с мастерами."""

from typing import Optional


def add_master(masters: list[dict], name: str, specialization: str) -> dict:
    """Добавить мастера в список."""
    new_id = max((m["id"] for m in masters), default=0) + 1
    master = {"id": new_id, "name": name, "specialization": specialization}
    masters.append(master)
    return master


def find_master_by_id(masters: list[dict], master_id: int) -> Optional[dict]:
    """Найти мастера по id."""
    for master in masters:
        if master["id"] == master_id:
            return master
    return None


def find_masters_by_specialization(
    masters: list[dict], specialization: str
) -> list[dict]:
    """Найти мастеров по специализации."""
    specialization = specialization.strip().lower()
    return [
        m for m in masters if m["specialization"].lower() == specialization
    ]