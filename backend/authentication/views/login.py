from django.contrib.auth import login
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

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

        login(request, user)

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        response = Response({'data': UserSerializer(user).data,})
        response.set_cookie(key="jwt", value=access_token, httponly=True, secure=True, max_age=15*60)

        return response
