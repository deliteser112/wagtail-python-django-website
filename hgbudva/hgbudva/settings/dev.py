from .base import *
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

DEBUG = True
ALLOWED_HOSTS = ["*"]

INTERNAL_IPS = [
    "127.0.0.1",
    "37.0.70.34",
    "78.155.33.19",
]

INSTALLED_APPS += ["debug_toolbar"]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "hgbudvadev.sqlite3",
    }
}

try:
    from .local import *
except ImportError:
    pass
