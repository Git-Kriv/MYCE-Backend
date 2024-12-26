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


INQUIRY_STATUS = [
    ("Received", "Received"),
    ("In Progress", "In Progress"),
    ("Processed", "Processed"),
]


class House(models.Model):
    """
    House model
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)
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
        return self.home_type + "--" + self.location

    class Meta:
        verbose_name_plural = "Houses"
        ordering = ["-date_created"]


class IndustrialProperty(models.Model):
    """
    Industrial Property model
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    date_created = models.DateTimeField(auto_now_add=True)
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
        return self.property_type + "--" + self.location_line_1

    class Meta:
        verbose_name_plural = "Industrial Properties"
        ordering = ["-date_created"]


class CommercialProperty(models.Model):
    """
    Commercial Property model
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    date_created = models.DateTimeField(auto_now_add=True)
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
        return self.cp_type + "--" + self.location_line_1

    class Meta:
        verbose_name_plural = "Commercial Properties"
        ordering = ["-date_created"]


class Inquiries(models.Model):
    """
    Inquiries model
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)

    email = models.EmailField(blank=False, null=False)
    phone_number = models.CharField(max_length=13, blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    report = models.TextField(blank=False, null=False)
    status = models.CharField(
        blank=False,
        null=False,
        default="Received",
        max_length=255,
        choices=INQUIRY_STATUS,
    )

    user = models.ForeignKey("user_auth.CustomUser", on_delete=models.CASCADE)

    def __str__(self):
        return self.email + "--" + self.phone_number

    class Meta:
        verbose_name_plural = "Inquiries"
        ordering = ["-date_created"]
