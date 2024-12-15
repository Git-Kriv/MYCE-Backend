from concurrent.futures import ProcessPoolExecutor
import uuid

from django.db import models


PROPERTY_TYPE = [
    ("Land", "Land"),
    ("Residential", "Residential"),
    ("Commercial", "Commercial"),
]


REQUIREMENT_TYPE = [
    ("Villa", "Villa"),
    ("Bungalow", "Bungalow"),
    ("Farm House Location", "Farm House Location"),
    ("Residential Apartment", "Residential Apartment"),
    ("Commercial", "Commercial"),
    ("Industrial", "Industrial"),
    ("Interior Design", "Interior Design"),
]


class ArchitectureDesign(models.Model):
    """
    Architecture model
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey("user_auth.CustomUser", on_delete=models.CASCADE)
    location = models.CharField(max_length=255, blank=False, null=False)
    location_line_1 = models.CharField(max_length=255, blank=False, null=False)
    location_line_2 = models.CharField(max_length=255, blank=True, null=True)
    land_size = models.DecimalField(max_digits=10, decimal_places=2)
    digital_survey = models.BooleanField(default=False)
    requirement_type = models.CharField(choices=REQUIREMENT_TYPE, max_length=255)
    requirements = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.location_line_1 + "--" + self.location_line_2

    class Meta:
        verbose_name_plural = "Architecture and Design"
        ordering = ["location_line_1"]


class SellingProperty(models.Model):
    """
    Selling Property model
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey("user_auth.CustomUser", on_delete=models.CASCADE)

    location = models.CharField(max_length=255, blank=False, null=False)
    location_line_1 = models.CharField(max_length=255, blank=False, null=False)
    location_line_2 = models.CharField(max_length=255, blank=True, null=True)
    property_type = models.CharField(choices=REQUIREMENT_TYPE, max_length=255)
    land_size = models.DecimalField(max_digits=10, decimal_places=2)
    owner_details = models.TextField(blank=True, null=True)
    property_documents = models.FileField(
        upload_to="property_documents/", blank=True, null=True
    )
    # todo: Add Property Type
    expected_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.location_line_1 + "--" + self.location_line_2

    class Meta:
        verbose_name_plural = "Selling Property"
        ordering = ["location_line_1"]


class BuyingProperty(models.Model):
    """
    Buying Property model
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey("user_auth.CustomUser", on_delete=models.CASCADE)
    location = models.CharField(max_length=255, blank=False, null=False)
    location_line_1 = models.CharField(max_length=255, blank=False, null=False)
    location_line_2 = models.CharField(max_length=255, blank=True, null=True)
    property_type = models.CharField(choices=PROPERTY_TYPE, max_length=255)
    land_size = models.DecimalField(max_digits=10, decimal_places=2)
    budget = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.location_line_1 + "--" + self.location_line_2

    class Meta:
        verbose_name_plural = "Buying Property"
        ordering = ["location_line_1"]


class SwimmingPool(models.Model):
    """
    Swimming Pool Model
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey("user_auth.CustomUser", on_delete=models.CASCADE)
    location_details = models.TextField(blank=True, null=True)
    size_availability = models.TextField(blank=True, null=True)
    pool_size = models.CharField(max_length=255, blank=True, null=True)
    equipment_list = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Swimming Pools"


class ProjectManagementService(models.Model):
    """Project Management Service Model"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey("user_auth.CustomUser", on_delete=models.CASCADE)
    security = models.TextField(blank=True, null=True)
    house_keeping = models.TextField(blank=True, null=True)
    property_tax = models.TextField(blank=True, null=True)
    electrical_and_repairs = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Project Management Services"
