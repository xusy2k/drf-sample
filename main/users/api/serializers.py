from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from ..models import User


class UserSerializer(serializers.ModelSerializer[User]):
    """
    Default ModelSerializer UserSerializer
    """

    email = serializers.EmailField()
    phone_number = PhoneNumberField()

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "email_validated",
            "phone_number",
            "phone_number_validated",
            "hobbies",
        ]


class UserReadOnlyModelSerializer(UserSerializer):
    """
    UserSerializer serializer with read_only fields
    """

    class Meta(UserSerializer.Meta):
        read_only_fields = UserSerializer.Meta.fields


class UserCreateSerializer(serializers.ModelSerializer[User]):
    """
    UserSerializer serializer with password field
    """

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "hobbies",
            "password",
        ]
        extra_kwargs = {"password": {"required": False}}


class UserManualSerializer(serializers.Serializer):
    """
    Manual UserSerializer to speed up the process
    """

    id = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    email_validated = serializers.BooleanField()
    phone_number = serializers.CharField()
    phone_number_validated = serializers.BooleanField()
    hobbies = serializers.CharField()
