from django.shortcuts import render
from django.views import View

from ..forms import CustomAuthenticationForm


class LoginView(View):

    def get(self, request):
        login_form = CustomAuthenticationForm()
        return render(
            request,
            "authentication/login.html",
            {
                "login_form": login_form,
            },
        )
