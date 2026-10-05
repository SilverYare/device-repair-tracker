"""Вспомогательные функции безопасного ввода."""

from datetime import date


def input_str(prompt: str) -> str:
    """Запросить непустую строку."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Ошибка: значение не может быть пустым.")


def input_int(prompt: str) -> int:
    """Запросить целое число."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите целое число.")


def input_float(prompt: str) -> float:
    """Запросить число с плавающей точкой."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите число.")


def input_bool(prompt: str) -> bool:
    """Запросить да/нет."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("да", "д", "yes", "y"):
            return True
        if answer in ("нет", "н", "no", "n"):
            return False
        print("Ошибка: введите 'да' или 'нет'.")


def input_date(prompt: str) -> date:
    """Запросить дату в формате ДД.ММ.ГГГГ."""
    while True:
        try:
            day, month, year = input(prompt).strip().split(".")
            return date(int(year), int(month), int(day))
        except (ValueError, AttributeError):
            print("Ошибка: формат ДД.ММ.ГГГГ.")