from django.urls import path
from . import views

urlpatterns = [
    path("houses/", views.get_houses, name="get_houses"),
    path(
        "industrial-properties/",
        views.get_industrial_properties,
        name="get_industrial_properties",
    ),
    path(
        "commercial-properties/",
        views.get_commercial_properties,
        name="get_commercial_properties",
    ),
    path("inquiries/", views.post_inquiry, name="post_inquiry"),
]
