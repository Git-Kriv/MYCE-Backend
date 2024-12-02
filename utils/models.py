"""Module containing models for execution phase"""

import uuid
from django.db import models


HOUSE_TYPE = [
    ("Bungalow", "Bungalow"),
    ("Villa", "Villa"),
    ("Farm House", "Farm House"),
    ("Apartment", "Apartment"),
]
INDUSTRY_PROPERTY_TYPE = [
    ("Office Space", "Office Space"),
    ("Retail Space", "Retail Space"),
]

COMMERICAL_PROPERTY_TYPE = [
    ("Factory Structure", "Factory Structure"),
    ("Warehouses", "Warehouses"),
]


class House(models.Model):
    """
    House model
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    home_type = models.CharField(
        choices=HOUSE_TYPE, max_length=255, blank=False, null=False, default="Bungalow"
    )
    location = models.CharField(max_length=255, blank=False, null=False)
    location_line_1 = models.CharField(max_length=255, blank=False, null=False)
    location_line_2 = models.CharField(max_length=255, blank=True, null=True)
    plan_details = models.TextField(blank=True, null=True)
    digital_survey = models.BooleanField(default=False)

    floor_plan = models.ImageField(upload_to="floor_plans/", blank=True, null=True)

    user = models.ForeignKey("user_auth.CustomUser", on_delete=models.CASCADE)

    def __str__(self):
        return self.name + "--" + self.address

    class Meta:
        verbose_name_plural = "Houses"
        ordering = ["home_type"]


class IndustrialProperty(models.Model):
    """
    Industrial Property model
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    property_type = models.CharField(
        choices=INDUSTRY_PROPERTY_TYPE,
        max_length=255,
        blank=False,
        null=False,
        default="Office Space",
    )
    location = models.CharField(max_length=255, blank=False, null=False)
    location_line_1 = models.CharField(max_length=255, blank=False, null=False)
    location_line_2 = models.CharField(max_length=255, blank=True, null=True)
    plan_details = models.TextField(blank=True, null=True)
    digital_survey = models.BooleanField(default=False)

    floor_plan = models.ImageField(upload_to="floor_plans/", blank=True, null=True)
    user = models.ForeignKey("user_auth.CustomUser", on_delete=models.CASCADE)

    def __str__(self):
        return self.type + "--" + self.location_line_1

    class Meta:
        verbose_name_plural = "Industrial Properties"
        ordering = ["property_type"]


class CommercialProperty(models.Model):
    """
    Commercial Property model
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cp_type = models.CharField(
        max_length=255, blank=False, null=False, default="Factory Structure"
    )
    location = models.CharField(max_length=255, blank=False, null=False)
    location_line_1 = models.CharField(max_length=255, blank=False, null=False)
    location_line_2 = models.CharField(max_length=255, blank=True, null=True)
    plan_details = models.TextField(blank=True, null=True)
    digital_survey = models.BooleanField(default=False)
    floor_plan = models.ImageField(upload_to="floor_plans/", blank=True, null=True)
    user = models.ForeignKey("user_auth.CustomUser", on_delete=models.CASCADE)

    def __str__(self):
        return self.type + "--" + self.location_line_1

    class Meta:
        verbose_name_plural = "Commercial Properties"
        ordering = ["cp_type"]


class Inquiries(models.Model):
    """
    Inquiries model
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(blank=False, null=False)
    phone_number = models.CharField(max_length=13, blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    report = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.email + "--" + self.phone_number

    class Meta:
        verbose_name_plural = "Inquiries"
        ordering = ["email", "phone_number"]
