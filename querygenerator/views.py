from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .forms import CustomAuthenticationForm, CustomUserCreationForm


def index(request):
    return render(request, 'querygenerator/index.html')


def user_register(request):
    if request.method == 'POST':
        register_form = CustomUserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data.get('username')
            password = register_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('querygenerator:index')
    else:
        register_form = CustomUserCreationForm()

    return render(
        request, 'querygenerator/register.html', {
            'register_form': register_form,
        }
    )


def user_login(request):
    if request.method == 'POST':
        login_form = CustomAuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('querygenerator:index')
    else:
        login_form = CustomAuthenticationForm()

    return render(
        request, 'querygenerator/login.html', {
            'login_form': login_form,
        }
    )


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('querygenerator:login')
