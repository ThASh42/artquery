from django.urls import path

from .views.users import UserRegisterView

app_name = "users"

urlpatterns = [path("register", UserRegisterView.as_view(), name="register")]
