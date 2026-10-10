"""Устройства и их подклассы."""

from abc import ABC, abstractmethod
from typing import Any


class Device(ABC):
    """Базовый класс устройства."""

    BASE_PRICE: float = 1000.0
    URGENT_MULTIPLIER: float = 1.5

    def __init__(
        self,
        device_id: int,
        model: str,
        serial_number: str,
    ) -> None:
        self._id = device_id
        self._model = model
        self._serial_number = serial_number

    @property
    def id(self) -> int:
        return self._id

    @property
    def model(self) -> str:
        return self._model

    @property
    def serial_number(self) -> str:
        return self._serial_number

    @property
    @abstractmethod
    def device_type(self) -> str:
        """Тип устройства; переопределяется в подклассах."""

    @property
    @abstractmethod
    def coefficient(self) -> float:
        """Коэффициент стоимости ремонта; переопределяется."""

    def calculate_repair_cost(self, is_urgent: bool = False) -> float:
        """Расчёт стоимости ремонта с учётом срочности."""
        cost = self.BASE_PRICE * self.coefficient
        if is_urgent:
            cost *= self.URGENT_MULTIPLIER
        return round(cost, 2)

    @staticmethod
    def validate_serial(serial: str) -> bool:
        """Проверка серийного номера."""
        return bool(serial.strip())

    @classmethod
    def from_data(cls, data: dict[str, Any]) -> "Device":
        """Фабрика: создать нужный подкласс по типу."""
        device_type = data["device_type"].strip().lower()
        common = {
            "device_id": data["id"],
            "model": data["model"],
            "serial_number": data["serial_number"],
        }
        mapping = {
            "ноутбук": Laptop,
            "смартфон": Smartphone,
            "планшет": Tablet,
            "телевизор": TV,
        }
        device_cls = mapping.get(device_type, Laptop)
        return device_cls(**common)

    def to_data(self) -> dict[str, Any]:
        """Преобразовать устройство в словарь."""
        return {
            "id": self._id,
            "device_type": self.device_type,
            "model": self._model,
            "serial_number": self._serial_number,
        }

    def __str__(self) -> str:
        return (
            f"[{self._id}] {self.device_type} "
            f"{self._model} (SN: {self._serial_number})"
        )


class Laptop(Device):
    @property
    def device_type(self) -> str:
        return "ноутбук"

    @property
    def coefficient(self) -> float:
        return 1.3


class Smartphone(Device):
    @property
    def device_type(self) -> str:
        return "смартфон"

    @property
    def coefficient(self) -> float:
        return 1.0


class Tablet(Device):
    @property
    def device_type(self) -> str:
        return "планшет"

    @property
    def coefficient(self) -> float:
        return 1.1


class TV(Device):
    @property
    def device_type(self) -> str:
        return "телевизор"

    @property
    def coefficient(self) -> float:
        return 1.4
