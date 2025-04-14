from django import forms
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

from backend.users.models import CustomUser

DEFAULT_ATTRS = {"class": "form-control"}


class CustomAuthenticationForm(forms.Form):

    username = forms.CharField(
        label=_("Username or email address"),
        max_length=264,
        required=True,
        strip=True,
        widget=forms.TextInput(
            attrs={
                **DEFAULT_ATTRS,
                "placeholder": _("Enter your username or email"),
            },
        ),
    )
    password = forms.CharField(
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

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "password",
        )

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            self.user_cache = authenticate(
                username=username, password=password
            )
            if self.user_cache is None:
                raise forms.ValidationError(
                    _("Invalid email or password."),
                    code="invalid_login",
                )
            elif not self.user_cache.is_active:
                raise forms.ValidationError(
                    _("This account is inactive."),
                    code="inactive",
                )
        return self.cleaned_data

    def get_user(self):
        return getattr(self, "user_cache", None)
