"""
ПР1. Сервис отслеживания ремонта устройств.
Начальный сценарий: регистрация заявки, расчёт стоимости и определение статуса.
Используются только простые типы данных, ветвления, функции и импорт модулей.
"""

from datetime import date


# --- Справочные данные (простые типы) ---

BASE_PRICE = 1000.0          # базовая стоимость диагностики, руб.
URGENT_MULTIPLIER = 1.5      # коэффициент срочности
DEVICE_COEFFICIENTS = {      # в ПР2 заменим на коллекцию, пока — условная логика
    "ноутбук": 1.3,
    "смартфон": 1.0,
    "планшет": 1.1,
    "телевизор": 1.4,
}


def calculate_repair_cost(device_type: str, is_urgent: bool) -> float:
    """
    Рассчитывает предварительную стоимость ремонта.

    :param device_type: тип устройства (строка)
    :param is_urgent: срочный ли ремонт (bool)
    :return: стоимость ремонта (float)
    """
    device_type = device_type.strip().lower()

    if device_type == "ноутбук":
        coefficient = 1.3
    elif device_type == "смартфон":
        coefficient = 1.0
    elif device_type == "планшет":
        coefficient = 1.1
    elif device_type == "телевизор":
        coefficient = 1.4
    else:
        coefficient = 1.0  # неизвестный тип — базовая стоимость

    cost = BASE_PRICE * coefficient

    if is_urgent:
        cost = cost * URGENT_MULTIPLIER

    return round(cost, 2)


def get_request_status(status_code: int) -> str:
    """
    Возвращает текстовое описание статуса заявки по коду.

    :param status_code: код статуса (int)
    :return: описание статуса (str)
    """
    if status_code == 1:
        return "Принята"
    elif status_code == 2:
        return "Диагностика"
    elif status_code == 3:
        return "В ремонте"
    elif status_code == 4:
        return "Готова к выдаче"
    elif status_code == 5:
        return "Выдана"
    else:
        return "Неизвестный статус"


def create_repair_request(
    client_name: str,
    device_type: str,
    device_model: str,
    is_urgent: bool,
) -> str:
    """
    Формирует текстовое описание заявки на ремонт.

    :param client_name: ФИО клиента
    :param device_type: тип устройства
    :param device_model: модель устройства
    :param is_urgent: срочность ремонта
    :return: строка с описанием заявки
    """
    if not client_name.strip():
        return "Ошибка: не указано имя клиента."

    if not device_type.strip() or not device_model.strip():
        return "Ошибка: не указаны тип или модель устройства."

    cost = calculate_repair_cost(device_type, is_urgent)
    status = get_request_status(1)  # новая заявка всегда «Принята»
    today = date.today()

    urgency_text = "срочный" if is_urgent else "обычный"

    return (
        f"Заявка от {today}\n"
        f"Клиент: {client_name}\n"
        f"Устройство: {device_type} {device_model}\n"
        f"Тип ремонта: {urgency_text}\n"
        f"Предварительная стоимость: {cost} руб.\n"
        f"Статус: {status}"
    )


# --- Демонстрация работы сценария ---

if __name__ == "__main__":
    print("=== Сервис отслеживания ремонта устройств ===")
    print()

    # Пример 1: обычный ремонт ноутбука
    print(create_repair_request(
        client_name="Иванов Иван Иванович",
        device_type="ноутбук",
        device_model="Lenovo IdeaPad 5",
        is_urgent=False,
    ))
    print()

    # Пример 2: срочный ремонт смартфона
    print(create_repair_request(
        client_name="Петрова Анна Сергеевна",
        device_type="смартфон",
        device_model="Samsung Galaxy S23",
        is_urgent=True,
    ))
    print()

    # Пример 3: проверка обработки ошибки
    print(create_repair_request(
        client_name="",
        device_type="планшет",
        device_model="iPad Air",
        is_urgent=False,
    ))