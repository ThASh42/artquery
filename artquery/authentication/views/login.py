from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from artquery.users.serializers.users import UserSerializer

from ..serializers.login import LoginSerializers


class LoginView(APIView):

    def post(self, request):
        serializer = LoginSerializers(
            data=request.data, context={'request': request}
        )
        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'data': UserSerializer(user).data,
            'token': token.key,
        })
