from typing import ClassVar

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from .managers import UserManager


class User(AbstractUser):
    username = None  # type: ignore[assignment]

    email = models.EmailField(_("email address"), unique=True)
    email_validated = models.BooleanField(_("email validated"), default=False)

    phone_number = PhoneNumberField(_("phone number"), blank=True)
    phone_number_validated = models.BooleanField(
        _("phone number validated"),
        default=False,
    )

    hobbies = models.TextField(_("hobbies"), blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects: ClassVar[UserManager] = UserManager()

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"pk": self.id})
