# Generated by Django 5.0.6 on 2024-12-24 18:40

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
            name="CommercialProperty",
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
                (
                    "cp_type",
                    models.CharField(default="Factory Structure", max_length=255),
                ),
                ("location", models.CharField(max_length=255)),
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
                "verbose_name_plural": "Commercial Properties",
                "ordering": ["cp_type"],
            },
        ),
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
                (
                    "home_type",
                    models.CharField(
                        choices=[
                            ("Bungalow", "Bungalow"),
                            ("Villa", "Villa"),
                            ("Farm House", "Farm House"),
                            ("Apartment", "Apartment"),
                        ],
                        default="Bungalow",
                        max_length=255,
                    ),
                ),
                ("location", models.CharField(max_length=255)),
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
                "ordering": ["home_type"],
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
                (
                    "property_type",
                    models.CharField(
                        choices=[
                            ("Office Space", "Office Space"),
                            ("Retail Space", "Retail Space"),
                        ],
                        default="Office Space",
                        max_length=255,
                    ),
                ),
                ("location", models.CharField(max_length=255)),
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
                "ordering": ["property_type"],
            },
        ),
        migrations.CreateModel(
            name="Inquiries",
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
                ("email", models.EmailField(max_length=254)),
                ("phone_number", models.CharField(max_length=13)),
                ("message", models.TextField()),
                ("report", models.TextField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Received", "Received"),
                            ("In Progress", "In Progress"),
                            ("Processed", "Processed"),
                        ],
                        default="Received",
                        max_length=255,
                    ),
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
                "verbose_name_plural": "Inquiries",
                "ordering": ["email", "phone_number"],
            },
        ),
    ]
