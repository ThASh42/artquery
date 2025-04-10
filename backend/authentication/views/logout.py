from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status


class LogoutView(View):

    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get("refresh_token")
        if refresh_token:
            try:
                refresh = RefreshToken(refresh_token)
                refresh.blacklist()
            except Exception as e:
                return response({"error":"Error invalidating token: " + str(e)}, status=status.HTTP_400_BAD_REQUEST)

        response = HttpResponseRedirect(reverse('authentication:login'))
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")

        return response
