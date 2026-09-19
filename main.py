"""Сервис отслеживания ремонта устройств. Точка входа."""

from storage import load_json, save_json
from devices import (
    add_device,
    find_device_by_id,
    find_devices_by_client,
    filter_devices_by_type,
    sort_devices_by_client,
)
from masters import (
    add_master,
    find_master_by_id,
    find_masters_by_specialization,
)
from requests import (
    create_request,
    assign_master,
    change_status,
    get_request_status,
    filter_requests_by_status,
    sort_requests_by_cost,
    get_master_workload,
)
from utils import input_int, input_bool

DEVICES_FILE = "data/devices.json"
MASTERS_FILE = "data/masters.json"
REQUESTS_FILE = "data/requests.json"


def show_devices(devices: list[dict]) -> None:
    """Вывести список устройств."""
    if not devices:
        print("Устройства не найдены.")
        return
    for device in devices:
        print(
            f"[{device['id']}] {device['client_name']} — "
            f"{device['device_type']} {device['model']} "
            f"(SN: {device['serial_number']})"
        )


def show_requests(requests: list[dict]) -> None:
    """Вывести список заявок."""
    if not requests:
        print("Заявки не найдены.")
        return
    for request in requests:
        status = get_request_status(request["status_code"])
        print(
            f"[{request['id']}] устройство #{request['device_id']}, "
            f"мастер: {request['master_id']}, "
            f"статус: {status}, стоимость: {request['cost']} руб."
        )


def show_masters(masters: list[dict]) -> None:
    """Вывести список мастеров."""
    if not masters:
        print("Мастера не найдены.")
        return
    for master in masters:
        print(
            f"[{master['id']}] {master['name']} — "
            f"{master['specialization']}"
        )


def main() -> None:
    """Основной цикл меню приложения."""
    devices = load_json(DEVICES_FILE)
    masters = load_json(MASTERS_FILE)
    requests = load_json(REQUESTS_FILE)

    while True:
        print("\n=== Сервис отслеживания ремонта устройств ===")
        print("1. Показать устройства")
        print("2. Найти устройства по клиенту")
        print("3. Отобрать устройства по типу")
        print("4. Показать мастеров")
        print("5. Создать заявку на ремонт")
        print("6. Назначить мастера на заявку")
        print("7. Изменить статус заявки")
        print("8. Показать заявки")
        print("9. Загрузка мастера")
        print("0. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            show_devices(sort_devices_by_client(devices))
        elif choice == "2":
            query = input("Подстрока имени клиента: ")
            show_devices(find_devices_by_client(devices, query))
        elif choice == "3":
            device_type = input("Тип устройства: ")
            show_devices(filter_devices_by_type(devices, device_type))
        elif choice == "4":
            show_masters(masters)
        elif choice == "5":
            device_id = input_int("ID устройства: ")
            device = find_device_by_id(devices, device_id)
            if device is None:
                print("Устройство не найдено.")
                continue
            is_urgent = input_bool("Срочный ремонт? (да/нет): ")
            request = create_request(
                requests,
                device_id,
                device["device_type"],
                is_urgent,
            )
            print(f"Создана заявка #{request['id']}, "
                  f"стоимость: {request['cost']} руб.")
        elif choice == "6":
            request_id = input_int("ID заявки: ")
            master_id = input_int("ID мастера: ")
            if assign_master(requests, request_id, master_id):
                print("Мастер назначен.")
            else:
                print("Заявка или мастер не найдены.")
        elif choice == "7":
            request_id = input_int("ID заявки: ")
            status_code = input_int("Новый статус (1–5): ")
            if change_status(requests, request_id, status_code):
                print("Статус изменён.")
            else:
                print("Не удалось изменить статус.")
        elif choice == "8":
            show_requests(sort_requests_by_cost(requests))
        elif choice == "9":
            master_id = input_int("ID мастера: ")
            load = get_master_workload(requests, master_id)
            print(f"Активных заявок у мастера: {load}")
        elif choice == "0":
            break
        else:
            print("Неизвестная команда.")

    save_json(DEVICES_FILE, devices)
    save_json(MASTERS_FILE, masters)
    save_json(REQUESTS_FILE, requests)
    print("Данные сохранены. До свидания!")


if __name__ == "__main__":
    main()