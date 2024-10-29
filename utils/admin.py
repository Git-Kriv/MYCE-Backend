from django.contrib import admin
from .models import House, IndustrialProperty, CommercialProperty, Inquiries


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ("home_type", "plan_details", "digital_survey", "user")
    search_fields = ("home_type", "plan_details")
    list_filter = ("home_type", "digital_survey")
    ordering = ("home_type",)


@admin.register(IndustrialProperty)
class IndustrialPropertyAdmin(admin.ModelAdmin):
    list_display = ("property_type", "plan_details", "digital_survey", "user")
    search_fields = ("property_type", "plan_details")
    list_filter = ("property_type", "digital_survey")
    ordering = ("property_type",)


@admin.register(CommercialProperty)
class CommercialPropertyAdmin(admin.ModelAdmin):
    list_display = ("cp_type", "plan_details", "digital_survey", "user")
    search_fields = ("cp_type", "plan_details")
    list_filter = ("cp_type", "digital_survey")
    ordering = ("cp_type",)


@admin.register(Inquiries)
class InquiriesAdmin(admin.ModelAdmin):
    list_display = ("email", "phone_number", "message")
    search_fields = ("email", "phone_number", "message")
    ordering = ("email", "phone_number")
