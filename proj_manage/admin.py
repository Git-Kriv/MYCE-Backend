from django.contrib import admin
from .models import ArchitectureDesign, SellingProperty, BuyingProperty


@admin.register(ArchitectureDesign)
class ArchitectureDesignAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "land_size",
        "requirement_type",
        "digital_survey",
    )
    search_fields = ("location_line_1", "location_line_2", "requirement_type")
    list_filter = ("requirement_type", "digital_survey")
    ordering = ("location_line_1",)


@admin.register(SellingProperty)
class SellingPropertyAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "property_type",
        "land_size",
        "expected_price",
    )
    search_fields = ("location_line_1", "location_line_2", "property_type")
    list_filter = ("property_type",)
    ordering = ("location_line_1",)


@admin.register(BuyingProperty)
class BuyingPropertyAdmin(admin.ModelAdmin):
    list_display = (
        "location_line_1",
        "user",
        "property_type",
        "land_size",
        "budget",
    )
    search_fields = ("location_line_1", "location_line_2", "property_type")
    list_filter = ("property_type",)
    ordering = ("location_line_1",)
