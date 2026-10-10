"""Статусы заявки."""

from enum import Enum


class RequestStatus(Enum):
    """Возможные статусы заявки на ремонт."""

    ACCEPTED = (1, "Принята")
    DIAGNOSTICS = (2, "Диагностика")
    IN_REPAIR = (3, "В ремонте")
    READY = (4, "Готова к выдаче")
    ISSUED = (5, "Выдана")

    def __init__(self, code: int, title: str) -> None:
        self.code = code
        self.title = title

    @classmethod
    def from_code(cls, code: int) -> "RequestStatus":
        """Получить статус по числовому коду."""
        for status in cls:
            if status.code == code:
                return status
        raise ValueError(f"Неизвестный код статуса: {code}")

    def __str__(self) -> str:
        return self.title