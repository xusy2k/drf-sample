from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.forms import UserChangeForm
from django.utils.translation import gettext_lazy as _
from phonenumber_field.formfields import PhoneNumberField

from .models import User


class UserChangeFormPhone(UserChangeForm):
    phone_number = PhoneNumberField(required=False)


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeFormPhone
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Personal info"),
            {"fields": ("first_name", "last_name", "phone_number", "hobbies")},
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["email", "first_name", "last_name", "is_superuser"]
    search_fields = ["first_name", "last_name"]
    ordering = ["id"]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
