from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

class CookieTokenRefreshView(TokenRefreshView):
    def post(self, request):

        refresh_token = request.COOKIES.get("refresh_token") or request.POST.get("refresh")

        if not refresh_token:
            return Response({"error": "Refresh token not provided"}, status = status.HTTP_401_UNAUTHORIZED)
        try:
            refresh = RefreshToken(refresh_token)
            access_token = str(refresh.access_token)

            response = Response(f"token: {access_token}", status=status.HTTP_200_OK)
            response.set_cookie(key="access_token",
                                value=access_token,
                                httponly=True,
                                secure=True,
                                samesite="Strict",)
            return response
        except Exception as e:
            return Response({"error": f"{e}"}, status=status.HTTP_401_UNAUTHORIZED)
