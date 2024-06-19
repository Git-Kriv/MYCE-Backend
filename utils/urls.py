from django.urls import path

from utils.views import get_houses, get_industrial_properties

urlpatterns = [
    path("houses/", get_houses, name="get_houses"),
    path("industrial_properties/", get_industrial_properties, name="get_industrial_properties"),
]
