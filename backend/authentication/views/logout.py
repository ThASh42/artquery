from django.contrib.auth import logout
from django.urls import reverse
from django.views import View
from django.http import HttpResponseRedirect

class LogoutView(View):

    def post(self, request, *args, **kwargs):
        logout(request)

        response = HttpResponseRedirect(reverse('authentication:login'))
        response.delete_cookie('jwt')

        return response
