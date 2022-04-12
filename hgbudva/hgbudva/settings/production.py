# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

from .base import *

DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": "localhost",
        "PORT": "",
    }
}

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "basic": {"format": "%(message)s"},
        "simple": {"format": "%(levelname)s %(message)s"},
        "verbose": {"format": "%(levelname)s %(asctime)s %(message)s"},
    },
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "services": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(BASE_DIR, "logs/services.log"),
            "maxBytes": 1024 * 1024 * 15,
            "backupCount": 10,
            "formatter": "verbose",
        },
    },
    "loggers": {
        "services": {
            "handlers": ["services"],
            "level": "DEBUG",
        },
    },
}

# CACHE SETTINGS
CACHE_TTL = 60 * 12

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
    }
}

CACHE_MIDDLEWARES = [
    "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.cache.FetchFromCacheMiddleware",
]

MIDDLEWARE[2:2] = CACHE_MIDDLEWARES

SECURE_HSTS_SECONDS = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"

ALLOWED_HOSTS = [
    "hgbudvanskarivijera.com",
    "dev.hgbudvanskarivijera.com",
    "localhost",
]

CRON_CLASSES = [
    "utils.backup_cron.Backup",
]

try:
    from .local import *
except ImportError:
    pass
