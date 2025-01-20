from django.contrib.auth.models import BaseUserManager
from django.db import transaction
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):

    def create_superuser(self, username, password, email, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(username, password, email, **extra_fields)

    @transaction.atomic
    def create_user(self, username, password, email, **extra_fields):
        if not username:
            raise ValueError(_('The username must be set'))

        if not email:
            raise ValueError(_('the email must be set'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
