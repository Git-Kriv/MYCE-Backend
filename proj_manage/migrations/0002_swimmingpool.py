# Generated by Django 5.0.6 on 2024-11-29 13:16

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("proj_manage", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="SwimmingPool",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("location_details", models.TextField(blank=True, null=True)),
                ("size_availability", models.TextField(blank=True, null=True)),
                ("pool_size", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "equipment_list",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Swimming Pools",
            },
        ),
    ]
