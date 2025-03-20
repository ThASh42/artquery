from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from rest_framework import generics, status, viewsets
from rest_framework.renderers import (
    BrowsableAPIRenderer, JSONRenderer, TemplateHTMLRenderer
)
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from ..models import CustomUser
from ..serializers.users import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    '''
    API view for CRUD operations and list/retrieve functionality.
    '''
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    renderer_classes = [
        JSONRenderer, BrowsableAPIRenderer, TemplateHTMLRenderer
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
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        if request.accepted_renderer.format == 'html':
            messages.success(request, "Registration successful!")
            return redirect(reverse('authentication:login'))

        response = Response(
            {'data': UserSerializer(user).data,}, 
            status=status.HTTP_201_CREATED,
        )
        response.set_cookie(
            key="jwt", 
            value=access_token, 
            httponly=True, 
            secure=True, 
            max_age=15*60,
        )

        return response


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
