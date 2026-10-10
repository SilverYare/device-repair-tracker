"""Пользовательские декораторы проекта."""

import functools
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)


def log_action(func):
    """Логировать вызов функции и её результат."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info("Вызов %s", func.__name__)
        result = func(*args, **kwargs)
        logging.info("Результат %s: %s", func.__name__, result)
        return result

    return wrapper
