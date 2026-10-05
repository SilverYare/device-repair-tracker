"""Базовый абстрактный класс человека."""

from abc import ABC, abstractmethod


class Person(ABC):
    """Общий предок клиентов и мастеров."""

    def __init__(self, person_id: int, name: str, phone: str) -> None:
        self._id = person_id
        self._name = name
        self._phone = phone

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not value.strip():
            raise ValueError("Имя не может быть пустым")
        self._name = value

    @property
    def phone(self) -> str:
        return self._phone

    @abstractmethod
    def role(self) -> str:
        """Роль в системе; переопределяется в подклассах."""

    def __str__(self) -> str:
        return f"{self.role().capitalize()} #{self._id}: {self._name}"