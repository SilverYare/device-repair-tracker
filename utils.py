"""Вспомогательные функции ввода с обработкой ошибок."""

from datetime import date


def input_int(prompt: str) -> int:
    """Запросить у пользователя целое число; повторять при ошибке."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите целое число.")


def input_float(prompt: str) -> float:
    """Запросить у пользователя число с плавающей точкой."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите число.")


def input_bool(prompt: str) -> bool:
    """Запросить у пользователя да/нет."""
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
        raw = input(prompt).strip()
        try:
            day, month, year = raw.split(".")
            return date(int(year), int(month), int(day))
        except (ValueError, AttributeError):
            print("Ошибка: введите дату в формате ДД.ММ.ГГГГ.")