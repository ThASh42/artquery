from django.urls import path

from .views.login import LoginView
from .views.logout import LogoutView

app_name = "authentication"

urlpatterns = [
    path("login", LoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
]
