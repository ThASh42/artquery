from django.shortcuts import render
from django.views import View
from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from ..forms import CustomUserCreationForm
from ..models import CustomUser
from ..serializers.users import UserSerializer


class RegistrationView(View):

    def get(self, request):
        register_form = CustomUserCreationForm()
        return render(
            request, 'accounts/register.html', {
                "register_form": register_form,
            }
        )


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
