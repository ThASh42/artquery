import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from ..managers.users import UserManager


class CustomUser(AbstractUser):
    id = models.UUIDField(  # noqa:A003
        primary_key=True, default=uuid.uuid4, editable=False
    )

    objects = UserManager()

    class Meta:
        verbose_name_plural = "Users"

    def __str__(self) -> str:
        return f'{self.username} | {self.email} | {self.id}'
