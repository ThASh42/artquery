from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator


class EmailBackend(ModelBackend):
    '''
    Email and username must be unique values for the user model
    '''

    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            if is_email(username):
                user = UserModel.objects.get(email=username)
            else:
                user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None


def is_email(value):
    validator = EmailValidator()
    try:
        validator(value)
        return True
    except ValidationError:
        return False
