"""
With these settings, tests run faster.
"""

from .base import *  # noqa: F403
from .base import TEMPLATES
from .base import env

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="sA5v8tidlQREqUl2b0vcXcyjfsFRoof99tz2NbDc5MERBWxX6KxuKY86ejiBleeK",
)
# https://docs.djangoproject.com/en/dev/ref/settings/#test-runner
TEST_RUNNER = "django.test.runner.DiscoverRunner"

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

# DEBUGGING FOR TEMPLATES
# ------------------------------------------------------------------------------
TEMPLATES[0]["OPTIONS"]["debug"] = True  # type: ignore[index]

# MEDIA
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = "http://media.testserver"
# Your stuff...
# ------------------------------------------------------------------------------

# Celery
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#task-always-eager
CELERY_TASK_ALWAYS_EAGER = env.bool("DJANGO_CELERY_TASK_ALWAYS_EAGER", True)
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#task-eager-propagates
CELERY_TASK_EAGER_PROPAGATES = env.bool("DJANGO_CELERY_TASK_EAGER_PROPAGATES", True)
