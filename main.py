"""Сервис отслеживания ремонта устройств. Точка входа."""

from decorators import log_action
from domain import (
    Client,
    Device,
    Master,
    RequestStatus,
)
from domain.devices import (
    add_device,
    find_device_by_id,
    show_devices,
    sort_devices_by_model,
)
from domain.masters import (
    add_master,
    find_master_by_id,
    show_masters,
)
from domain.requests import (
    assign_master,
    change_status,
    create_request,
    get_master_workload,
    show_requests,
    sort_requests_by_cost,
)
from domain.storage import (
    load_clients,
    load_devices,
    load_masters,
    load_requests,
    save_clients,
    save_devices,
    save_masters,
    save_requests,
)
from utils import input_bool, input_int, input_str

CLIENTS_FILE = "data/clients.json"
MASTERS_FILE = "data/masters.json"
DEVICES_FILE = "data/devices.json"
REQUESTS_FILE = "data/requests.json"


def action_add_client(clients: list[Client]) -> None:
    """Диалог добавления клиента."""
    name = input_str("ФИО клиента: ")
    phone = input_str("Телефон: ")
    email = input_str("Email: ")
    new_id = max((c.id for c in clients), default=0) + 1
    clients.append(Client(new_id, name, phone, email))
    print(f"Клиент добавлен с id={new_id}")


def action_add_master(masters: list[Master]) -> None:
    """Диалог добавления мастера."""
    name = input_str("ФИО мастера: ")
    phone = input_str("Телефон: ")
    specialization = input_str("Специализация: ")
    new_id = max((m.id for m in masters), default=0) + 1
    add_master(masters, new_id, name, phone, specialization)
    print(f"Мастер добавлен с id={new_id}")


def action_add_device(devices: list[Device]) -> None:
    """Диалог добавления устройства."""
    device_type = input_str("Тип (ноутбук/смартфон/планшет/телевизор): ")
    model = input_str("Модель: ")
    serial = input_str("Серийный номер: ")
    new_id = max((d.id for d in devices), default=0) + 1
    add_device(devices, new_id, model, serial, device_type)
    print(f"Устройство добавлено с id={new_id}")


def action_create_request(
    requests: list,
    devices: list[Device],
    clients: list[Client],
) -> None:
    """Диалог создания заявки."""
    device_id = input_int("ID устройства: ")
    device = find_device_by_id(devices, device_id)
    if device is None:
        print("Устройство не найдено.")
        return

    client_id = input_int("ID клиента: ")
    client = next((c for c in clients if c.id == client_id), None)
    if client is None:
        print("Клиент не найден.")
        return

    is_urgent = input_bool("Срочный ремонт? (да/нет): ")
    new_id = max((r.id for r in requests), default=0) + 1
    request = create_request(requests, new_id, device, client, is_urgent)
    print(f"Создана заявка: {request}")


@log_action
def action_assign_master(
    requests: list, masters: list[Master]
) -> None:
    """Диалог назначения мастера на заявку."""
    request_id = input_int("ID заявки: ")
    master_id = input_int("ID мастера: ")
    master = find_master_by_id(masters, master_id)
    if master is None:
        print("Мастер не найден.")
        return
    if assign_master(requests, request_id, master):
        print("Мастер назначен.")
    else:
        print("Заявка не найдена.")


def action_change_status(requests: list) -> None:
    """Диалог изменения статуса заявки."""
    request_id = input_int("ID заявки: ")
    print("Статусы: 1 — Принята, 2 — Диагностика, 3 — В ремонте, "
          "4 — Готова, 5 — Выдана")
    code = input_int("Новый код статуса: ")
    try:
        status = RequestStatus.from_code(code)
    except ValueError as error:
        print(f"Ошибка: {error}")
        return
    if change_status(requests, request_id, status):
        print("Статус изменён.")
    else:
        print("Заявка не найдена.")


def action_workload(requests: list, masters: list[Master]) -> None:
    """Диалог подсчёта загрузки мастера."""
    master_id = input_int("ID мастера: ")
    master = find_master_by_id(masters, master_id)
    if master is None:
        print("Мастер не найден.")
        return
    print(f"Активных заявок: {get_master_workload(requests, master)}")


def main() -> None:
    """Точка запуска приложения."""
    clients = load_clients(CLIENTS_FILE)
    masters = load_masters(MASTERS_FILE)
    devices = load_devices(DEVICES_FILE)
    requests = load_requests(REQUESTS_FILE, devices, clients, masters)

    while True:
        print("\n=== Сервис отслеживания ремонта устройств ===")
        print("1. Показать устройства")
        print("2. Добавить устройство")
        print("3. Показать мастеров")
        print("4. Добавить мастера")
        print("5. Добавить клиента")
        print("6. Создать заявку")
        print("7. Назначить мастера")
        print("8. Изменить статус заявки")
        print("9. Показать заявки")
        print("10. Загрузка мастера")
        print("0. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            show_devices(sort_devices_by_model(devices))
        elif choice == "2":
            action_add_device(devices)
        elif choice == "3":
            show_masters(masters)
        elif choice == "4":
            action_add_master(masters)
        elif choice == "5":
            action_add_client(clients)
        elif choice == "6":
            action_create_request(requests, devices, clients)
        elif choice == "7":
            action_assign_master(requests, masters)
        elif choice == "8":
            action_change_status(requests)
        elif choice == "9":
            show_requests(sort_requests_by_cost(requests))
        elif choice == "10":
            action_workload(requests, masters)
        elif choice == "0":
            break
        else:
            print("Неизвестная команда.")

    save_clients(CLIENTS_FILE, clients)
    save_masters(MASTERS_FILE, masters)
    save_devices(DEVICES_FILE, devices)
    save_requests(REQUESTS_FILE, requests)
    print("Данные сохранены. До свидания!")


if __name__ == "__main__":
    main()
