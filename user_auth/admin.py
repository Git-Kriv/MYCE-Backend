from django.contrib import admin

from user_auth.models import UserProfile, CustomUser, OTP


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name")


class OTPAdmin(admin.ModelAdmin):
    list_display = ("otp_val", "email")


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(CustomUser)
admin.site.register(OTP, OTPAdmin)
