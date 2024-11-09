""" Module for login and signup views. """ ""

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from user_auth.serializers import (
    UserRegisterSerializer,
    UserProfileSerializer,
)
from user_auth.helpers import verify_otp, send_otp, send_email, jwt_auth_required
from user_auth.models import CustomUser, UserProfile

# pylint: disable=no-member


@api_view(["POST", "GET"])
@jwt_auth_required
def signup(request):  # pylint: disable=R1710
    """Signup view."""
    if request.method == "GET":
        # Returns the registration form with fields to be filled
        registration_serializer = UserRegisterSerializer()
        return Response(
            registration_serializer.data,
        )
    if request.method == "POST":
        user = request.user
        phone_number = user.phone_number
        if UserProfile.objects.filter(phone_number=phone_number).exists():
            return Response(
                {"error": "Details already submitted for this user."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user, user_profile_data = serializer.save()
            refresh = RefreshToken.for_user(user)
            data = {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user_profile": user_profile_data,
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([AllowAny])
def verify_phone(request):
    """To check if a user exists with same phone number if not then create user and send OTP"""

    if request.method == "POST":
        try:
            phone_number = request.data["phone_number"]

            if int(phone_number) == 1234567890:  # FIXME: Only for  testing.
                return Response(
                    {"success": "Phone number exists", "registered": False},
                    status=status.HTTP_200_OK,
                )

            user = CustomUser.objects.filter(phone_number=phone_number).first()
            if user is None:
                if send_otp(phone_number):
                    user = CustomUser.objects.create(
                        phone_number=phone_number, details_submitted=False
                    )
                    return Response(
                        {"error": "Mobile No. not registered", "registered": False},
                        status=status.HTTP_404_NOT_FOUND,
                    )

                return Response(
                    data={"error": "OTP not sent"},
                    status=status.HTTP_422_UNPROCESSABLE_ENTITY,
                )

            if send_otp(phone_number):
                return Response(
                    {"success": "Phone number exists", "registered": True},
                    status=status.HTTP_200_OK,
                )
            return Response(
                data={"error": "OTP not sent"},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )
        except CustomUser.DoesNotExist:
            print("[OTP FLOW] ERROR: ", "User not found")
            return Response(
                {"error": "Invalid request"},
                status=status.HTTP_400_BAD_REQUEST,
            )
    return Response(
        {"error": "Method Not Allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED
    )


@api_view(["POST"])
@permission_classes(AllowAny)
def verify_email(request):
    """To check if a user exists with same phone number if not then create user and send OTP"""

    if request.method == "POST":
        try:
            email = request.data["email"]

            if email == "test@myce.com":  # FIXME: Only for  testing.
                return Response(
                    {"success": "Phone number exists", "registered": False},
                    status=status.HTTP_200_OK,
                )

            user = CustomUser.objects.filter(email=email).first()
            if user is None:
                if send_email(email):

                    user = CustomUser.objects.create(
                        email=email, details_submitted=False
                    )
                    return Response(
                        {"error": "Mobile No. not registered", "registered": False},
                        status=status.HTTP_404_NOT_FOUND,
                    )

                return Response(
                    data={"error": "OTP not sent"},
                    status=status.HTTP_422_UNPROCESSABLE_ENTITY,
                )

            if send_email(email):
                return Response(
                    {"success": "Phone number exists", "registered": True},
                    status=status.HTTP_200_OK,
                )
            return Response(
                data={"error": "OTP not sent"},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )
        except CustomUser.DoesNotExist:
            print("[OTP FLOW] ERROR: ", "User not found")
            return Response(
                {"error": "Invalid request"},
                status=status.HTTP_400_BAD_REQUEST,
            )
    return Response(
        {"error": "Method Not Allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED
    )


@api_view(["POST"])
@permission_classes([AllowAny])
def verify_and_return_creds(request):
    """To verify the otp sent to the user"""
    try:
        otp = request.data["otp"]
        phone_number = request.data["phone_number"]
        # FIXME: This is just for the google app testing
        if str(phone_number) == "1234567890":
            if CustomUser.objects.filter(phone_number=int(phone_number)).exists():
                user = CustomUser.objects.get(phone_number=phone_number)
                refresh = RefreshToken.for_user(user)
            else:
                user = CustomUser.objects.create(
                    name="TEST", phone_number=phone_number, details_submitted=False
                )
                refresh = RefreshToken.for_user(user)

            user_profile = UserProfile.objects.filter(user=user)

            if user_profile.exists():
                user_profile_data = UserProfileSerializer(user_profile.first()).data
            else:
                user_profile_data = None

            data = {
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "user_profile": user_profile_data,
            }
            return Response({"key": True, "data": data}, status=status.HTTP_200_OK)
        # REMOVE THIS COMPLETE BLOCK AFTER TESTING ^
        if verify_otp(otp, phone_number):
            user = CustomUser.objects.get(phone_number=phone_number)
            refresh = RefreshToken.for_user(user)

            user_profile = UserProfile.objects.filter(user=user)
            if user_profile.exists():
                user_profile_data = UserProfileSerializer(user_profile.first()).data
            else:
                user_profile_data = None

            data = {
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "user_profile": user_profile_data,
            }
            return Response({"key": True, "data": data}, status=status.HTTP_200_OK)

        return Response({"key": False}, status=status.HTTP_401_UNAUTHORIZED)

    except Exception as e:
        print("[OTP_PROCESS] ERROR: ", str(e))
        return Response({"key": False}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT"])
@jwt_auth_required
def user_profile(request):  # pylint: disable=R1710
    """To get the user profile"""

    if request.method == "GET":
        try:
            user = request.user
            return Response(
                {"user_profile": UserProfileSerializer(user.user_profile).data},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {
                    "error": "Invalid request",
                    "ERROR": str(e),
                },  # For logging purposes only - delete later
                status=status.HTTP_400_BAD_REQUEST,
            )
    if request.method == "PUT":
        try:
            user = request.user
            user_profile = user.user_profile
            request.data["user"] = request.user.id

            if (
                "phone_number" in request.data
            ):  # FIXME : Later add send otp and logic to handle the case.
                if request.data["phone_number"] != user.phone_number:
                    user.phone_number = request.data["phone_number"]
                    user.save()
            else:
                request.data["phone_number"] = user_profile.phone_number
            if "address" not in request.data:
                request.data["age"] = user_profile.age

            request.data["user"] = user.id
            request.data["first_name"] = (
                request.data["first_name"]
                if "first_name" in request.data
                else user_profile.first_name
            )
            request.data["last_name"] = (
                request.data["last_name"]
                if "last_name" in request.data
                else user_profile.last_name
            )
            request.data["full_name"] = (
                request.data["first_name"] + " " + request.data["last_name"]
            )

            serializer = UserProfileSerializer(user_profile, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"user_profile": serializer.data}, status=status.HTTP_200_OK
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except UserProfile.DoesNotExist:
            return Response(
                {"error": "User Profile not found"}, status=status.HTTP_404_NOT_FOUND
            )
