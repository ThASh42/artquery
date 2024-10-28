from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from ..models import CustomUser
from ..serializers.users import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        user = serializer.save()
        token = Token.objects.create(user=user)
        return Response(
            {
                'token': token.key,
                'data': UserSerializer(user).data,
            },
            status=status.HTTP_201_CREATED,
        )
