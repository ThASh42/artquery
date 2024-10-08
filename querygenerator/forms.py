from django import forms  # noqa:F401
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            'username',
            'email',
        )

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        DEFAULT_ATTRS = {'class': 'form-control width-300'}
        self.fields['username'].widget.attrs.update(
            DEFAULT_ATTRS | {'placeholder': 'Username'}
        )
        self.fields['email'].widget.attrs.update(
            DEFAULT_ATTRS | {'placeholder': 'Email'}
        )
        self.fields['password1'].widget.attrs.update(
            DEFAULT_ATTRS | {'placeholder': 'Password'}
        )
        self.fields['password2'].widget.attrs.update(
            DEFAULT_ATTRS | {'placeholder': 'Repeat your password'}
        )


class CustomAuthenticationForm(AuthenticationForm):

    class Meta:
        model = CustomUser

    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        DEFAULT_ATTRS = {'class': 'form-control width-300'}
        self.fields['username'].widget.attrs.update(
            DEFAULT_ATTRS | {'placeholder': 'Username'}
        )
        self.fields['password'].widget.attrs.update(
            DEFAULT_ATTRS | {'placeholder': 'Password'}
        )
