from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.schemas.coreapi import serializers
from proj_manage.models import ArchitectureDesign, SellingProperty, BuyingProperty
from proj_manage.serializers import (
    ArchitectureDesignSerializer,
    SellingPropertySerializer,
    BuyingPropertySerializer,
    SwimmingPoolSerializer,
)
from user_auth.helpers import (
    jwt_auth_required,
)


@api_view(["GET", "POST"])
@jwt_auth_required
def architecture_design_view(request):
    """Retrieve or create Architecture Design entries."""
    if request.method == "GET":
        designs = ArchitectureDesign.objects.filter(user=request.user)
        serializer = ArchitectureDesignSerializer(designs, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        request.data["user"] = request.user.id
        serializer = ArchitectureDesignSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
@jwt_auth_required
def selling_property_view(request):
    """Retrieve or create Selling Property entries."""
    if request.method == "GET":
        properties = SellingProperty.objects.filter(user=request.user)
        serializer = SellingPropertySerializer(properties, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        request.data["user"] = request.user.id
        serializer = SellingPropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
@jwt_auth_required
def buying_property_view(request):
    """Retrieve or create Buying Property entries."""
    if request.method == "GET":
        properties = BuyingProperty.objects.filter(user=request.user)
        serializer = BuyingPropertySerializer(properties, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        request.data["user"] = request.user.id
        serializer = BuyingPropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@jwt_auth_required
def swimming_pool(request):
    if request.method == "POST":
        request.data["user"] = request.user.id
        serializer = SwimmingPoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
