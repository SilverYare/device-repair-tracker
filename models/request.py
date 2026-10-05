"""Заявка на ремонт устройства."""

from datetime import date
from typing import Any, Optional

from .client import Client
from .device import Device
from .master import Master
from .status import RequestStatus


class Request:
    """Заявка на ремонт."""

    def __init__(
        self,
        request_id: int,
        device: Device,
        client: Client,
        is_urgent: bool = False,
        status: RequestStatus = RequestStatus.ACCEPTED,
        master: Optional[Master] = None,
        created_at: Optional[str] = None,
    ) -> None:
        self._id = request_id
        self._device = device
        self._client = client
        self._is_urgent = is_urgent
        self._status = status
        self._master = master
        self._created_at = created_at or date.today().isoformat()

    @property
    def id(self) -> int:
        return self._id

    @property
    def device(self) -> Device:
        return self._device

    @property
    def client(self) -> Client:
        return self._client

    @property
    def master(self) -> Optional[Master]:
        return self._master

    @property
    def status(self) -> RequestStatus:
        return self._status

    @property
    def is_urgent(self) -> bool:
        return self._is_urgent

    @property
    def created_at(self) -> str:
        return self._created_at

    @property
    def cost(self) -> float:
        """Стоимость ремонта (делегируется устройству)."""
        return self._device.calculate_repair_cost(self._is_urgent)

    def assign_master(self, master: Master) -> None:
        """Назначить мастера на заявку."""
        self._master = master

    def change_status(self, new_status: RequestStatus) -> None:
        """Изменить статус заявки."""
        self._status = new_status

    @classmethod
    def from_data(
        cls,
        data: dict[str, Any],
        devices: list[Device],
        clients: list[Client],
        masters: list[Master],
    ) -> "Request":
        """Создать заявку из словаря, подтянув связанные объекты."""
        device = next(
            (d for d in devices if d.id == data["device_id"]), None
        )
        if device is None:
            raise ValueError(
                f"Устройство id={data['device_id']} не найдено"
            )
        client = next(
            (c for c in clients if c.id == data["client_id"]), None
        )
        if client is None:
            raise ValueError(
                f"Клиент id={data['client_id']} не найден"
            )
        master = None
        if data.get("master_id") is not None:
            master = next(
                (m for m in masters if m.id == data["master_id"]), None
            )
        status = RequestStatus.from_code(data["status_code"])
        return cls(
            request_id=data["id"],
            device=device,
            client=client,
            is_urgent=data["is_urgent"],
            status=status,
            master=master,
            created_at=data.get("created_at"),
        )

    def to_data(self) -> dict[str, Any]:
        """Преобразовать заявку в словарь для JSON."""
        return {
            "id": self._id,
            "device_id": self._device.id,
            "client_id": self._client.id,
            "master_id": self._master.id if self._master else None,
            "status_code": self._status.code,
            "is_urgent": self._is_urgent,
            "created_at": self._created_at,
        }

    def __str__(self) -> str:
        master_text = self._master.name if self._master else "не назначен"
        return (
            f"[{self._id}] {self._client.name} — "
            f"{self._device.device_type} {self._device.model}, "
            f"статус: {self._status}, "
            f"мастер: {master_text}, "
            f"стоимость: {self.cost} руб."
        )