import uuid

from django.db import models


class House(models.Model):
    """
    House model
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=255, blank=False, null=False)
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
        ordering = ["type"]

class IndustrialProperty(models.Model):
    """
    Industrial Property model
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=255, blank=False, null=False)
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
        ordering = ["type"]
