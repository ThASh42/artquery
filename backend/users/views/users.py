from django.shortcuts import render
from django.views import View
from ..api.v1.serializers.users import UserSerializer


class UserRegisterView(View):
    serializer_class = UserSerializer

    def get(self, request):
        serializer = self.serializer_class()
        context = {'serializer': serializer}
        return render(request, 'accounts/register.html', context)
