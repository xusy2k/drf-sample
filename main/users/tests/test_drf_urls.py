from django.conf import settings
from django.urls import resolve
from django.urls import reverse


def test_signup():
    assert reverse("api:users:signup") == f"/api/{settings.VERSION_API}/signup/"
    assert resolve(f"/api/{settings.VERSION_API}/signup/").view_name == "api:users:signup"


def test_profile():
    assert reverse("api:users:profile") == f"/api/{settings.VERSION_API}/profile/"
    assert resolve(f"/api/{settings.VERSION_API}/profile/").view_name == "api:users:profile"
