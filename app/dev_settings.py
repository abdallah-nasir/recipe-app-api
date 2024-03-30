import os
import sys
from django.conf import settings

MIDDLEWARE = getattr(settings, "MIDDLEWARE")
INSTALLED_APPS = getattr(settings, "INSTALLED_APPS")

BASE_DIR = getattr(
    settings,
    "BASE_DIR",
)

ALLOWED_HOSTS = ["*"]
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
MEDIA_URL = os.getenv("MEDIA_URL")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
if "test" not in sys.argv:
    MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"] + MIDDLEWARE
    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK": lambda request: True,
    }
    INSTALLED_APPS = INSTALLED_APPS + ["debug_toolbar"]
