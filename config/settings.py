"""
Django settings for config project.

Сгенерировано 'django-admin startproject' для Django 5.2.

Документация:
https://docs.djangoproject.com/en/5.2/topics/settings/
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

import sys
from pathlib import Path

# Корень проекта: папка, где лежат manage.py, models/, data/, main.py
BASE_DIR = Path(__file__).resolve().parent.parent

# Делаем корень проекта доступным для импорта,
# чтобы Django видел пакет models/ из ПР3.
sys.path.insert(0, str(BASE_DIR))


# --- Безопасность ---

# ВНИМАНИЕ: этот ключ предназначен только для разработки.
# Для production его нужно заменить и хранить в переменной окружения.
SECRET_KEY = (
    "django-insecure-"
    "=#g2y=k4r!wv8@z%p$m^7x9(h3j5t6s1b0l&c*q+n_d4e7f2a"
)

# Режим отладки. Для разработки — True.
DEBUG = False

# Список разрешённых хостов.
# При DEBUG = False нужно указать конкретные адреса.
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]


# --- Приложения ---

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Приложения проекта
    "homepage",
    "devices",
    "masters",
    "repairs",
]


# --- Middleware ---

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# --- URL и WSGI ---

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# --- База данных ---

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# --- Валидация паролей ---

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        ),
    },
]


# --- Локализация ---

LANGUAGE_CODE = "ru-RU"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_TZ = True


# --- Статические файлы ---

STATIC_URL = "static/"

# Тип первичного ключа по умолчанию
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
