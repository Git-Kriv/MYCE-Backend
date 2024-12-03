# Generated by Django 5.0.6 on 2024-12-03 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "proj_manage",
            "0003_architecturedesign_location_buyingproperty_location_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="buyingproperty",
            name="property_type",
            field=models.CharField(
                choices=[
                    ("Land", "Land"),
                    ("Residential", "Residential"),
                    ("Commercial", "Commercial"),
                ],
                max_length=255,
            ),
        ),
    ]