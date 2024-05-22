import pytest
from django.urls import reverse
from faker import Faker
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APIRequestFactory

from ..api.serializers import UserSerializer
from ..models import User


class TestUserViewSet:
    @pytest.fixture()
    def api_rf(self) -> APIRequestFactory:
        return APIRequestFactory()

    @pytest.mark.django_db()
    def test_signup_user(self):
        fake = Faker("es_ES")

        data = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "phone_number": fake.phone_number(),
            "email": fake.email(),
            "hobbies": fake.sentence(nb_words=30),
        }
        with pytest.raises(User.DoesNotExist):
            User.objects.get(email=data["email"])

        url = reverse("api:users:signup")
        client = APIClient()
        response = client.post(url, data, format="json")

        assert response.status_code == status.HTTP_201_CREATED
        assert User.objects.get().email == data["email"]

    def test_create_profile_user(self, user, create_authenticated_client):
        url_profile = reverse("api:users:profile")
        url_signup = reverse("api:users:signup")

        # Could a Anonymous User access to the profile of a user?
        anonymous_response = APIClient().get(url_profile, format="json")
        assert anonymous_response.status_code == status.HTTP_401_UNAUTHORIZED

        fake = Faker("es_ES")
        data = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "phone_number": fake.phone_number(),
            "email": fake.email(),
            "hobbies": fake.sentence(nb_words=30),
        }
        with pytest.raises(User.DoesNotExist):
            User.objects.get(email=data["email"])

        response = APIClient().post(url_signup, data, format="json")
        assert response.status_code == status.HTTP_201_CREATED

        # Could create a different user with same email?
        response_duplicated = APIClient().post(url_signup, data, format="json")
        assert response_duplicated.status_code == status.HTTP_400_BAD_REQUEST

        # Could a user access to the profile of another different user?
        another_user = User.objects.get(email=data["email"])
        assert another_user.email == data["email"]

        response_user = create_authenticated_client(user).get(
            url_profile,
            format="json",
        )
        assert response_user.status_code == status.HTTP_200_OK
        response_another_user = create_authenticated_client(another_user).get(
            url_profile,
            format="json",
        )
        assert response_another_user.status_code == status.HTTP_200_OK
        assert UserSerializer(user).data["email"] != UserSerializer(another_user).data["email"]
