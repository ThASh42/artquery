import uuid

from django.db import models


class CustomModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)  # noqa: A003

    class Meta:
        abstract = True
