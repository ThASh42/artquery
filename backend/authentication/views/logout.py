from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View


class LogoutView(View):

    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse('users:register'))
