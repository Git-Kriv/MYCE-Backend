from django.urls import path

from user_auth.views import (
    signup,
    verify_phone,
    verify_and_return_creds,
    user_profile,
    verify_email,
)

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("verify_phone/", verify_phone, name="verify_phone"),
    path("verify_otp/", verify_and_return_creds, name="verify_and_return_creds"),
    path("user_profile/", user_profile, name="user_profile"),
    path("verify_email", verify_email, name="verify_email"),
]
