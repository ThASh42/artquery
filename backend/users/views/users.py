from django.shortcuts import render
from django.views import View

from ..api.v1.serializers.users import UserSerializer
from ..forms.users import CustomUserCreationForm


class UserRegisterView(View):
    serializer_class = UserSerializer

    def get(self, request):
        register_form = CustomUserCreationForm()
        context = {"register_form": register_form}
        return render(request, "accounts/register.html", context)
