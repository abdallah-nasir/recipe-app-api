ALLOWED_HOSTS = ["*"]
from pathlib import Path

SECRET_KEY = 'django-insecure-e+)641!z*+#^)j7b^*+uuazrgi1ys)p+u10d7)6k!u^f9q-9ea'
BASE_DIR = Path(__file__).resolve().parent.parent
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = 'static/'
