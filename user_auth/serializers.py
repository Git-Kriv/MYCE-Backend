"""Module for serializing the user_auth models."""

import secrets

from rest_framework import serializers

from user_auth.models import CustomUser, UserProfile


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        exclude = ("user",)

        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
            "email": {"required": True},
        }

    def create(self, validated_data):
        password = secrets.token_urlsafe(12)
        email = validated_data["email"]
        print(email)
        if CustomUser.objects.filter(email=validated_data["email"]).exists():
            user = CustomUser.objects.filter(email=validated_data["email"]).first()
            if not user.details_submitted:
                user.name = (
                    validated_data["first_name"] + " " + validated_data["last_name"]
                )
                if "phone_number" in validated_data:
                    user.phone_number = validated_data["phone_number"]
                else:
                    validated_data["phone_number"] = 0
                user.details_submitted = True
                user.save()

                validated_data["user"] = user
                validated_data["full_name"] = (
                    validated_data["first_name"] + " " + validated_data["last_name"]
                )
                user_profile = UserProfile.objects.create(**validated_data)
                serialized_user_profile = UserProfileSerializer(user_profile)
                return user, serialized_user_profile.data
            else:
                raise serializers.ValidationError(
                    {"error": "email already exists, please login"}
                )
        else:  # NOT Accessed as we have added @jwt_required() in the view - allows only OTP verified users

            raise serializers.ValidationError({"error": "email not found"})
