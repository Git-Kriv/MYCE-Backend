from django.http import JsonResponse
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

from proj_manage.models import (
    ArchitectureDesign,
    SellingProperty,
    BuyingProperty,
    SwimmingPool,
    ProjectManagementService,
)

from proj_manage.serializers import (
    ArchitectureDesignSerializer,
    SellingPropertySerializer,
    BuyingPropertySerializer,
    SwimmingPoolSerializer,
    ProjectManagementServiceSerializer,
)


# pyright: reportAttributeAccessIssue=false


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


@api_view(["GET"])
@jwt_auth_required
def all_inquiries(request):
    """Get all inquiries for all the models."""
    if request.method == "GET":
        user = request.user.id
        houses = House.objects.filter(user=user).order_by("-date_created")
        industrial_properties = IndustrialProperty.objects.filter(user=user).order_by(
            "-date_created"
        )
        commercial_properties = CommercialProperty.objects.filter(user=user).order_by(
            "-date_created"
        )
        inquiries = Inquiries.objects.filter(user=user).order_by("-date_created")
        houses_serializer = HouseSerializer(houses, many=True)
        industrial_properties_serializer = IndustrialPropertySerializer(
            industrial_properties, many=True
        )
        commercial_properties_serializer = CommercialPropertySerializer(
            commercial_properties, many=True
        )
        inquiries_serializer = InquiriesSerializer(inquiries, many=True)

        buying_property = BuyingProperty.objects.filter(user=user).order_by(
            "-date_created"
        )
        selling_property = SellingProperty.objects.filter(user=user).order_by(
            "-date_created"
        )
        architecture_design = ArchitectureDesign.objects.filter(user=user).order_by(
            "-date_created"
        )
        swimming_pool = SwimmingPool.objects.filter(user=user).order_by("-date_created")
        project_management_service = ProjectManagementService.objects.filter(
            user=user
        ).order_by("-date_created")

        buying_property_serializer = BuyingPropertySerializer(
            buying_property, many=True
        )
        selling_property_serializer = SellingPropertySerializer(
            selling_property, many=True
        )
        architecture_design_serializer = ArchitectureDesignSerializer(
            architecture_design, many=True
        )
        swimming_pool_serializer = SwimmingPoolSerializer(swimming_pool, many=True)
        project_management_service_serializer = ProjectManagementServiceSerializer(
            project_management_service, many=True
        )

        data = {
            "houses": houses_serializer.data,
            "industrial_properties": industrial_properties_serializer.data,
            "commercial_properties": commercial_properties_serializer.data,
            "inquiries": inquiries_serializer.data,
            "buying_property": buying_property_serializer.data,
            "selling_property": selling_property_serializer.data,
            "architecture_design": architecture_design_serializer.data,
            "swimming_pool": swimming_pool_serializer.data,
            "project_management_service": project_management_service_serializer.data,
        }

        return JsonResponse(data, safe=False, status=status.HTTP_200_OK)
