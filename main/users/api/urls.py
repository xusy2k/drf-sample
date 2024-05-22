from django.urls import path

from .views import UserCreateView
from .views import UserDetailView
from .views import UserListView

app_name = "users"

urlpatterns = [
    path("signup/", UserCreateView.as_view(), name="signup"),
    path("profile/", UserDetailView.as_view(), name="profile"),
    path("list/", UserListView.as_view(), name="list"),
]
