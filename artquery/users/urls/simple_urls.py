from django.urls import path

from ..views.users import RegistrationView

app_name = "users"

urlpatterns = [path('register', RegistrationView.as_view(), name='register')]
