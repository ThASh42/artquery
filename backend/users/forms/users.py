from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from backend.users.models import CustomUser

DEFAULT_ATTRS = {'class': 'form-control width-300'}


class CustomUserCreationForm(UserCreationForm):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                **DEFAULT_ATTRS, 'placeholder': _('Your username..')
            }
        ),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                **DEFAULT_ATTRS,
                'placeholder': _('Email adress..'),
            }
        ),
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={**DEFAULT_ATTRS}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={**DEFAULT_ATTRS}),
    )
    first_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                **DEFAULT_ATTRS,
                'placeholder': _('First name..'),
            }
        ),
    )
    last_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                **DEFAULT_ATTRS,
                'placeholder': _('Last name..'),
            }
        ),
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
        )

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
