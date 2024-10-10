from typing import List

from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from artquery.general.constants import ACCOUNT_NUMBER_LENGTH
from artquery.general.validators import HexStringValidator

from ..managers.accounts import AccountManager


class Account(AbstractBaseUser):
    account_number = models.CharField(
        max_length=ACCOUNT_NUMBER_LENGTH,
        primary_key=True,
        validators=(HexStringValidator(ACCOUNT_NUMBER_LENGTH),)
    )
    balance = models.PositiveBigIntegerField(default=0)
    display_image = models.URLField(max_length=200, blank=True)
    display_name = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = AccountManager()

    EMAIL_FIELD = None
    REQUIRED_FIELDS: List[str] = []
    USERNAME_FIELD = 'account_number'

    def __str__(self) -> str:
        return f'{self.account_number} | {self.balance}'

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True

    @property
    def id(self):  # noqa:A003
        return self.account_number
