from django.urls import include
from django.urls import path

app_name = "api"
urlpatterns = [
    path("", include("main.users.api.urls")),
]
