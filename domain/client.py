"""Класс клиента сервиса."""

from typing import Any

from .person import Person


class Client(Person):
    """Клиент — владелец устройства."""

    def __init__(
        self,
        person_id: int,
        name: str,
        phone: str,
        email: str = "",
    ) -> None:
        super().__init__(person_id, name, phone)
        self._email = email

    @property
    def email(self) -> str:
        return self._email

    def role(self) -> str:
        return "клиент"

    @classmethod
    def from_data(cls, data: dict[str, Any]) -> "Client":
        """Создать клиента из словаря."""
        return cls(
            person_id=data["id"],
            name=data["name"],
            phone=data["phone"],
            email=data.get("email", ""),
        )

    def to_data(self) -> dict[str, Any]:
        """Преобразовать клиента в словарь."""
        return {
            "id": self._id,
            "name": self._name,
            "phone": self._phone,
            "email": self._email,
        }

    def __str__(self) -> str:
        return f"[{self._id}] {self._name} ({self._phone})"
