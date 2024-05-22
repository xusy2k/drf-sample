import logging

from rest_framework import filters
from rest_framework import generics
from rest_framework.permissions import AllowAny

from ..models import User
from .serializers import UserCreateSerializer
from .serializers import UserManualSerializer
from .serializers import UserReadOnlyModelSerializer

log = logging.getLogger(__name__)


class UserCreateView(generics.CreateAPIView):
    """
    Create a new user.
    """

    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        User.objects.create_user(**serializer.validated_data)


class UserDetailView(generics.RetrieveAPIView):
    """
    Retrieve a user.
    """

    serializer_class = UserReadOnlyModelSerializer

    def get_object(self):
        return self.request.user


class UserListView(generics.ListAPIView):
    """
    List all users.
    """

    serializer_class = UserManualSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ["first_name", "last_name", "email"]

    def get_queryset(self):
        qs = User.objects.all()
        if self.request.user.is_anonymous is False and self.request.user.is_superuser is False:
            qs = qs.filter(email=self.request.user.email)
        return qs

    def get_serializer_class(self, *args, **kwargs):
        if self.request.user.is_superuser:
            return UserManualSerializer
        return UserReadOnlyModelSerializer
