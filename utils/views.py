from django.http import JsonResponse
from environ import re
from rest_framework import status
from rest_framework.decorators import api_view


from user_auth.helpers import jwt_auth_required
from utils.models import House, IndustrialProperty, CommercialProperty, Inquiries
from utils.serializers import (
    HouseSerializer,
    IndustrialPropertySerializer,
    CommercialPropertySerializer,
    InquiriesSerializer,
)


@api_view(["GET", "POST"])
@jwt_auth_required
def get_houses(request):
    """Get all houses."""
    if request.method == "GET":
        houses = House.objects.filter(user=request.user)
        serializer = HouseSerializer(houses, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == "POST":
        request.data["user"] = request.user.id
        serializer = HouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
@jwt_auth_required
def get_industrial_properties(request):
    """Get all industrial properties."""
    if request.method == "GET":
        industrial_properties = IndustrialProperty.objects.filter(user=request.user)
        serializer = IndustrialPropertySerializer(industrial_properties, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == "POST":
        request.data["user"] = request.user.id
        serializer = IndustrialPropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
@jwt_auth_required
def get_commercial_properties(request):
    """Get all commercial properties."""
    if request.method == "GET":
        commercial_properties = CommercialProperty.objects.filter(user=request.user)
        serializer = CommercialPropertySerializer(commercial_properties, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == "POST":
        request.data["user"] = request.user.id
        serializer = CommercialPropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
@jwt_auth_required
def inquiry(request):
    """Post/Get an inquiry."""
    if request.method == "POST":
        request.data["user"] = request.user.id
        serializer = InquiriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "GET":
        request.data["user"] = request.user.id
        inquiries = Inquiries.objects.filter(user=request.user)
        serializer = InquiriesSerializer(inquiries, many=True)
        return JsonResponse(serializer.data, safe=False)
