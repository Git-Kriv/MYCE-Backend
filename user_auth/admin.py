from django.contrib import admin

from user_auth.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name')

admin.site.register(UserProfile, UserProfileAdmin)
