import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CommonConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "main.common"
    verbose_name = _("Common")

    def ready(self):
        with contextlib.suppress(ImportError):
            from . import signals  # type: ignore  # noqa: F401
