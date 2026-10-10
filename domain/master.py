"""Класс мастера по ремонту."""

from typing import Any

from .person import Person


class Master(Person):
    """Мастер, выполняющий ремонт."""

    def __init__(
        self,
        person_id: int,
        name: str,
        phone: str,
        specialization: str,
    ) -> None:
        super().__init__(person_id, name, phone)
        self._specialization = specialization

    @property
    def specialization(self) -> str:
        return self._specialization

    def role(self) -> str:
        return "мастер"

    @classmethod
    def from_data(cls, data: dict[str, Any]) -> "Master":
        """Создать мастера из словаря."""
        return cls(
            person_id=data["id"],
            name=data["name"],
            phone=data["phone"],
            specialization=data["specialization"],
        )

    def to_data(self) -> dict[str, Any]:
        """Преобразовать мастера в словарь."""
        return {
            "id": self._id,
            "name": self._name,
            "phone": self._phone,
            "specialization": self._specialization,
        }

    def __str__(self) -> str:
        return f"[{self._id}] {self._name} — {self._specialization}"
