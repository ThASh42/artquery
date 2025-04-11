from django.contrib.auth import logout
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from .constants import ACCESS_TOKEN_LIFETIME_SECONDS


class TokenRefreshMiddleware(MiddlewareMixin):
    """Middleware for processing authentication logic."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        access_token = request.COOKIES.get("access_token")
        refresh_token = request.COOKIES.get("refresh_token")

        if access_token:
            return self.get_response(request)

        if refresh_token:
            try:
                new_access_token = RefreshToken(refresh_token).access_token
                response = self.get_response(request)

                response.set_cookie(
                    key="access_token",
                    value=new_access_token,
                    httponly=True,
                    secure=True,
                    samesite="Strict",
                    max_age=ACCESS_TOKEN_LIFETIME_SECONDS,
                )
                return response

            except TokenError:
                return JsonResponse(
                    {"error": "Refresh token expired"}, status=401
                )

        if request.user.is_authenticated:
            logout(request)

        return self.get_response(request)
