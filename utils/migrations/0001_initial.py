# Generated by Django 5.0.6 on 2024-06-19 01:32

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="House",
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
                ("type", models.CharField(max_length=255)),
                ("location_line_1", models.CharField(max_length=255)),
                (
                    "location_line_2",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("plan_details", models.TextField(blank=True, null=True)),
                ("digital_survey", models.BooleanField(default=False)),
                (
                    "floor_plan",
                    models.ImageField(blank=True, null=True, upload_to="floor_plans/"),
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
                "verbose_name_plural": "Houses",
                "ordering": ["type"],
            },
        ),
        migrations.CreateModel(
            name="IndustrialProperty",
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
                ("type", models.CharField(max_length=255)),
                ("location_line_1", models.CharField(max_length=255)),
                (
                    "location_line_2",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("plan_details", models.TextField(blank=True, null=True)),
                ("digital_survey", models.BooleanField(default=False)),
                (
                    "floor_plan",
                    models.ImageField(blank=True, null=True, upload_to="floor_plans/"),
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
                "verbose_name_plural": "Industrial Properties",
                "ordering": ["type"],
            },
        ),
    ]
