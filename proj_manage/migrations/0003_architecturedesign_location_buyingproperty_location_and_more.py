# Generated by Django 5.0.6 on 2024-12-02 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("proj_manage", "0002_swimmingpool"),
    ]

    operations = [
        migrations.AddField(
            model_name="architecturedesign",
            name="location",
            field=models.CharField(default="TEST", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="buyingproperty",
            name="location",
            field=models.CharField(default="TEST", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="sellingproperty",
            name="location",
            field=models.CharField(default="TEST", max_length=255),
            preserve_default=False,
        ),
    ]