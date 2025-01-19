from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from rest_framework import generics, status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.renderers import (
    BrowsableAPIRenderer, JSONRenderer, TemplateHTMLRenderer
)
from rest_framework.response import Response

from ..models import CustomUser
from ..serializers.users import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    '''
    API view for CRUD operations and list/retrieve functionality.
    '''
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    renderer_classes = [
        TemplateHTMLRenderer, JSONRenderer, BrowsableAPIRenderer
    ]

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            if request.accepted_renderer.format == 'html':
                return redirect(reverse('users:register'))

            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = serializer.save()
        login(request, user)
        token = Token.objects.create(user=user)

        if request.accepted_renderer.format == 'html':
            messages.success(request, "Registration successful!")
            return redirect(reverse('authentication:login'))

        return Response(
            {
                'token': token.key,
                'data': UserSerializer(user).data,
            },
            status=status.HTTP_201_CREATED,
        )


class UserRegisterView(generics.GenericAPIView):
    '''
    Handle GET for the registration form
    '''
    serializer_class = UserSerializer
    rendered_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class()
        context = {'serializer': serializer}
        return render(request, 'accounts/register.html', context)
