from django.contrib.auth import login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.users.api.v1.serializers.users import UserSerializer

from .....general.constants import (
    ACCESS_TOKEN_LIFETIME_SECONDS,
    REFRESH_TOKEN_LIFETIME_SECONDS,
)
from ..serializers.login import LoginSerializer


class LoginAPIView(APIView):

    def post(self, request):
        serializer = LoginSerializer(
            data=request.data, context={"request": request}
        )
        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        user = serializer.save()

        tokens = serializer.get_tokens(user)
        response = Response(
            {"data": UserSerializer(user).data, "token_data": tokens}
        )

        response.set_cookie(
            key="access_token",
            value=tokens["access"],
            httponly=True,
            secure=True,
            samesite="Strict",
            max_age=ACCESS_TOKEN_LIFETIME_SECONDS,
        )

        response.set_cookie(
            key="refresh_token",
            value=tokens["refresh"],
            httponly=True,
            secure=True,
            samesite="Strict",
            max_age=REFRESH_TOKEN_LIFETIME_SECONDS,
        )

        login(request, user)

        return response
