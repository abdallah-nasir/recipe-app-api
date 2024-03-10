import os
from django.conf import settings

BASE_DIR = getattr(
    settings,
    "BASE_DIR",
)

ALLOWED_HOSTS = ["*"]
SECRET_KEY = os.getenv("SECRET_KEY")
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}

STATIC_URL = "/static/"
DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": lambda request: True,
}
MEDIA_URL = os.getenv("MEDIA_URL")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
