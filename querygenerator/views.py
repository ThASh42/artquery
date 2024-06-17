from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm


def index(request):
    return render(request, 'querygenerator/index.html')


def user_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('querygenerator:index')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'querygenerator/register.html', {
        'form': form,
    })


def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('querygenerator:index')
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'querygenerator/login.html', {
        'form': form,
    })


@login_required
def user_logout(request):
    logout(request)
    return redirect('querygenerator:login')
