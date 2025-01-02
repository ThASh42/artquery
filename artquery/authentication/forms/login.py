from django import forms
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

from artquery.users.models import CustomUser

DEFAULT_ATTRS = {'class': 'form-control width-300'}


class CustomAuthenticationForm(forms.Form):

    username = forms.CharField(
        label=_("Username or email address"),
        widget=forms.TextInput(
            attrs={
                **DEFAULT_ATTRS,
                'placeholder': _('Username or email address'),
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={**DEFAULT_ATTRS})
    )

    class Meta:
        model = CustomUser
        fields = (
            'email',
            'password',
        )

    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if email and password:
            self.user_cache = authenticate(username=email, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    "Invalid email or password.",
                    code='invalid_login',
                )
        return self.cleaned_data

    def get_user(self):
        return self.user_cache
