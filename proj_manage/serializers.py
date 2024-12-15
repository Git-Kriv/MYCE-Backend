from rest_framework import serializers
from .models import (
    ArchitectureDesign,
    SellingProperty,
    BuyingProperty,
    SwimmingPool,
    ProjectManagementService,
)


class ArchitectureDesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchitectureDesign
        fields = [
            "id",
            "user",
            "location_line_1",
            "location_line_2",
            "land_size",
            "digital_survey",
            "requirement_type",
            "requirements",
        ]
        read_only_fields = ["id"]


class SellingPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = SellingProperty
        fields = [
            "id",
            "user",
            "location_line_1",
            "location_line_2",
            "property_type",
            "land_size",
            "owner_details",
            "property_documents",
            "expected_price",
        ]
        read_only_fields = ["id"]


class BuyingPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyingProperty
        fields = [
            "id",
            "user",
            "location_line_1",
            "location_line_2",
            "property_type",
            "land_size",
            "budget",
        ]
        read_only_fields = ["id"]


class SwimmingPoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwimmingPool
        fields = "__all__"


class ProjectManagementServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectManagementService
        fields = "__all__"
