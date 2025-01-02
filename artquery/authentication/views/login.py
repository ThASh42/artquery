from django.contrib.auth import login
from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from artquery.users.serializers.users import UserSerializer

from ..forms import CustomAuthenticationForm
from ..serializers.login import LoginSerializer


class LoginView(APIView):

    def get(self, request):
        login_form = CustomAuthenticationForm()
        return render(
            request, 'authentication/login.html', {
                "login_form": login_form,
            }
        )

    def post(self, request):
        serializer = LoginSerializer(
            data=request.data, context={'request': request}
        )
        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        user = serializer.save()

        login(request, user)

        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'data': UserSerializer(user).data,
            'token': token.key,
        })
