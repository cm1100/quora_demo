# Generated by Django 5.2 on 2025-04-09 09:00

import accounts.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="customuser",
            managers=[
                ("objects", accounts.models.CustomUserManager()),
            ],
        ),
    ]
