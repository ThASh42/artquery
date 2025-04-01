from django.contrib.auth import login
from django.shortcuts import redirect, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.users.serializers.users import UserSerializer

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

        tokens = serializer.get_tokens(user)
        response = Response({'data': UserSerializer(user).data, 'token_data': tokens})

        response.set_cookie(key="access_token",
                            value=tokens['access'],
                            httponly=True,
                            secure=True,
                            samesite="Strict",
                            max_age=60*60)

        response.set_cookie(key="refresh_token",
                            value=tokens['refresh'],
                            httponly=True,
                            secure=True,
                            samesite="Strict",
                            max_age=60*60*24*30)

        return response
