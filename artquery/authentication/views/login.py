from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from artquery.accounts.serializers.accounts import AccountSerializer

from ..serializers.login import LoginSerializers


class LoginView(APIView):

    def post(self, request):
        serializer = LoginSerializers(
            data=request.data, context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        account = serializer.save()
        refresh_token = RefreshToken.for_user(account)

        return Response({
            'account': AccountSerializer(account).data,
            'authentication': {
                'access_token': str(refresh_token.access_token),
                'refresh_token': str(refresh_token),
            },
        })
