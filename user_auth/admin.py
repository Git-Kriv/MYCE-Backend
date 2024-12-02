from django.contrib import admin

from user_auth.models import UserProfile, CustomUser


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name")


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(CustomUser)
