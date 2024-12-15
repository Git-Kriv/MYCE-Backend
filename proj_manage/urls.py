from django.urls import path
from proj_manage import views

urlpatterns = [
    path(
        "architecture-design/",
        views.architecture_design_view,
        name="architecture_design",
    ),
    path("selling-property/", views.selling_property_view, name="selling_property"),
    path("buying-property/", views.buying_property_view, name="buying_property"),
    path("swimming_pool/", views.swimming_pool, name="swimming_pool"),
    path(
        "project-management-service/",
        views.project_management_services,
        name="project_management_service",
    ),
]
