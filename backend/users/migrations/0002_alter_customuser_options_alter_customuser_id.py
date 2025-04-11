# Generated by Django 5.1.2 on 2024-10-21 09:13

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="customuser",
            options={"verbose_name_plural": "Users"},
        ),
        migrations.AlterField(
            model_name="customuser",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4,
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
