# Generated by Django 5.0.6 on 2024-10-29 06:27

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
            name="ArchitectureDesign",
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
                ("location_line_1", models.CharField(max_length=255)),
                (
                    "location_line_2",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("land_size", models.DecimalField(decimal_places=2, max_digits=10)),
                ("digital_survey", models.BooleanField(default=False)),
                (
                    "requirement_type",
                    models.CharField(
                        choices=[
                            ("Villa", "Villa"),
                            ("Bungalow", "Bungalow"),
                            ("Farm House Location", "Farm House Location"),
                            ("Residential Apartment", "Residential Apartment"),
                            ("Commercial", "Commercial"),
                            ("Industrial", "Industrial"),
                            ("Interior Design", "Interior Design"),
                        ],
                        max_length=255,
                    ),
                ),
                ("requirements", models.TextField(blank=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Architecture and Design",
                "ordering": ["location_line_1"],
            },
        ),
        migrations.CreateModel(
            name="BuyingProperty",
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
                ("location_line_1", models.CharField(max_length=255)),
                (
                    "location_line_2",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "property_type",
                    models.CharField(
                        choices=[
                            ("Villa", "Villa"),
                            ("Bungalow", "Bungalow"),
                            ("Farm House Location", "Farm House Location"),
                            ("Residential Apartment", "Residential Apartment"),
                            ("Commercial", "Commercial"),
                            ("Industrial", "Industrial"),
                            ("Interior Design", "Interior Design"),
                        ],
                        max_length=255,
                    ),
                ),
                ("land_size", models.DecimalField(decimal_places=2, max_digits=10)),
                ("budget", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Buying Property",
                "ordering": ["location_line_1"],
            },
        ),
        migrations.CreateModel(
            name="SellingProperty",
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
                ("location_line_1", models.CharField(max_length=255)),
                (
                    "location_line_2",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "property_type",
                    models.CharField(
                        choices=[
                            ("Villa", "Villa"),
                            ("Bungalow", "Bungalow"),
                            ("Farm House Location", "Farm House Location"),
                            ("Residential Apartment", "Residential Apartment"),
                            ("Commercial", "Commercial"),
                            ("Industrial", "Industrial"),
                            ("Interior Design", "Interior Design"),
                        ],
                        max_length=255,
                    ),
                ),
                ("land_size", models.DecimalField(decimal_places=2, max_digits=10)),
                ("owner_details", models.TextField(blank=True, null=True)),
                (
                    "property_documents",
                    models.FileField(
                        blank=True, null=True, upload_to="property_documents/"
                    ),
                ),
                (
                    "expected_price",
                    models.DecimalField(decimal_places=2, max_digits=10),
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
                "verbose_name_plural": "Selling Property",
                "ordering": ["location_line_1"],
            },
        ),
    ]
