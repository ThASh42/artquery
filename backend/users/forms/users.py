from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from rest_framework.validators import UniqueValidator

from backend.users.models import CustomUser

DEFAULT_ATTRS = {"class": "form-control"}


class CustomUserCreationForm(UserCreationForm):

    username = forms.CharField(
        label=_("Your username"),
        max_length=150,
        required=True,
        strip=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())],
        widget=forms.TextInput(
            attrs={**DEFAULT_ATTRS, "placeholder": _("Your username...")},
        ),
    )
    first_name = forms.CharField(
        label=_("Your first name"),
        max_length=150,
        required=False,
        strip=True,
        widget=forms.TextInput(
            attrs={
                **DEFAULT_ATTRS,
                "placeholder": _("First name..."),
            },
        ),
    )
    last_name = forms.CharField(
        label=_("Your last name"),
        max_length=150,
        required=False,
        strip=True,
        widget=forms.TextInput(
            attrs={
                **DEFAULT_ATTRS,
                "placeholder": _("Last name..."),
            },
        ),
    )
    email = forms.EmailField(
        label=_("Your email"),
        max_length=264,
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())],
        widget=forms.EmailInput(
            attrs={
                **DEFAULT_ATTRS,
                "placeholder": _("Email adress..."),
            },
        ),
    )
    password1 = forms.CharField(
        label=_("Password"),
        required=True,
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                **DEFAULT_ATTRS,
                "placeholder": "**********",
            },
        ),
    )
    password2 = forms.CharField(
        label=_("Confirm password"),
        required=True,
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                **DEFAULT_ATTRS,
                "placeholder": "**********",
            },
        ),
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )
