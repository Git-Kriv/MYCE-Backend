from django.urls import path
from . import views

urlpatterns = [
    path(
        "architecture-design/",
        views.architecture_design_view,
        name="architecture_design",
    ),
    path("selling-property/", views.selling_property_view, name="selling_property"),
    path("buying-property/", views.buying_property_view, name="buying_property"),
]
