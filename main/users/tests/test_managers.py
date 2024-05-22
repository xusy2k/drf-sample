from io import StringIO

import pytest
from django.core.management import call_command
from faker import Faker

from ..models import User


@pytest.mark.django_db()
class TestUserManager:
    def test_create_user(self):
        fake = Faker("es_ES")
        data = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "phone_number": fake.phone_number(),
            "email": fake.email(),
            "hobbies": fake.sentence(nb_words=30),
            "password": fake.password(
                length=42,
                special_chars=True,
                digits=True,
                upper_case=True,
                lower_case=True,
            ),
        }

        user = User.objects.create_user(**data)
        assert user.email == data["email"]
        assert not user.is_staff
        assert not user.is_superuser
        assert user.check_password(data["password"])
        assert user.username is None

    def test_create_superuser(self):
        fake = Faker("es_ES")
        data = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "phone_number": fake.phone_number(),
            "email": fake.email(),
            "hobbies": fake.sentence(nb_words=30),
            "password": fake.password(
                length=42,
                special_chars=True,
                digits=True,
                upper_case=True,
                lower_case=True,
            ),
        }
        user = User.objects.create_superuser(**data)
        assert user.email == data["email"]
        assert user.is_staff
        assert user.is_superuser
        assert user.check_password(data["password"])
        assert user.username is None

    def test_create_superuser_username_ignored(self):
        fake = Faker("es_ES")
        data = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "phone_number": fake.phone_number(),
            "email": fake.email(),
            "hobbies": fake.sentence(nb_words=30),
            "password": fake.password(
                length=42,
                special_chars=True,
                digits=True,
                upper_case=True,
                lower_case=True,
            ),
        }
        user = User.objects.create_superuser(**data)
        assert user.username is None


@pytest.mark.django_db()
def test_createsuperuser_command():
    """Ensure createsuperuser command works with our custom manager."""
    out = StringIO()
    fake = Faker("es_ES")
    email = fake.email()
    command_result = call_command(
        "createsuperuser",
        "--email",
        email,
        interactive=False,
        stdout=out,
    )

    assert command_result is None
    assert out.getvalue() == "Superuser created successfully.\n"
    user = User.objects.get(email=email)
    assert not user.has_usable_password()
