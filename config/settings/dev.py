import os
from config.settings.base import *

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "celeryproject",
        "USER": "tupa",
        "PASSWORD": "123456",
        "HOST": os.environ.get("DATABASE_HOST", "db"),
        "PORT": 5432,
    }
}
