import secrets
import time

import environ
import jwt
import requests

from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth import get_user_model

from rest_framework_simplejwt.authentication import JWTAuthentication

from user_auth.models import OTP


env = environ.Env()
environ.Env.read_env()

# pylint: disable=no-member

JWT_authenticator = JWTAuthentication()


def send_otp(phone_number):
    """Sends an OTP to the given phone number."""

    otp = "".join([str(secrets.randbelow(10)) for _ in range(6)])
    response = requests.post(
        "https://www.fast2sms.com/dev/bulkV2",
        headers={
            "authorization": env("FAST2SMS_API_AUTHORISATION_KEY"),
            "Content-Type": "application/json",
        },
        params={
            "route": "dlt",
            "sender_id": env("FAST2SMS_SENDER_ID"),
            "numbers": phone_number,
            "message": env("MESSAGE"),
            "flash": "0",
            "variables_values": str(otp),
        },
        timeout=10,
    )
    response = response.json()
    if response["return"]:
        OTP.objects.create(otp_val=otp, phone_number=phone_number)
        return True, "success"
    print("[OTP_PROCESS] ERROR: ", response["message"])
    return False


def verify_otp(otp, mobile_number):
    """Verifies the OTP sent to the given mobile number"""

    otp_objects = OTP.objects.filter(phone_number=mobile_number)
    current_time = time.time()
    print("[OTP_PROCESS] INFO: Printing entered OTP and OTP Object")

    for otp_object in otp_objects:
        print("[OTP_PROCESS] INFO: ", otp, str(otp_object.otp_val))
        if otp_object.otp_val == otp:
            time_difference = current_time - otp_object.created_at.timestamp()
            if time_difference > 6000:
                otp_object.delete()

                return False
            otp_object.delete()
            return True
        if current_time - otp_object.created_at.timestamp() > 6000:
            otp_object.delete()
    return False

def jwt_auth_required(view_func):
    """Decorator to check if the user is authenticated."""

    def wrapped_view(request, *args, **kwargs):
        print("[AUTH_PROCESS] INFO: JWT AUTHENTICATION STARTED")

        auth_header = request.META.get("HTTP_AUTHORIZATION", "")
        if not auth_header or not auth_header.startswith("Bearer "):
            return JsonResponse({"error": "Not Authorized"}, status=401)
        payloads = JWT_authenticator.authenticate(request)
        user, token = payloads
        print(user, token)

        try:
            token = auth_header.split(" ")[1]

            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user_id = payload.get("user_id")

            if not user_id:
                return JsonResponse({"error": "Invalid token"}, status=401)

            User = get_user_model()
            try:
                request.user = User.objects.get(id=user_id)
                print("[AUTH_PROCESS] INFO: JWT AUTHENTICATION PASSED")
                return view_func(request, *args, **kwargs)
            except User.DoesNotExist:
                return JsonResponse({"error": "User not found"}, status=404)

        except jwt.ExpiredSignatureError:
            print(auth_header)
            token = auth_header.split(" ")[1]
            print(token)
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user_id = payload.get("user_id")

            return JsonResponse({"error": "Token has expired"}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({"error": "Invalid token"}, status=401)

    return wrapped_view
