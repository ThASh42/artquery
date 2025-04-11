from rest_framework import status, viewsets
from rest_framework.response import Response

from .....general.constants import (
    ACCESS_TOKEN_LIFETIME_SECONDS,
    REFRESH_TOKEN_LIFETIME_SECONDS,
)
from ....models import CustomUser
from ..serializers.users import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API view for CRUD operations and list/retrieve of users functionality.
    """

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = serializer.save()

        tokens = serializer.get_tokens(user)
        response = Response(
            {"data": UserSerializer(user).data, "tokens": tokens},
            status=status.HTTP_201_CREATED,
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

        return response
