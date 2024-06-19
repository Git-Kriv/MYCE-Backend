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
            "phone_number": {"required": True},
        }

    def create(self, validated_data):
        password = secrets.token_urlsafe(12)
        if CustomUser.objects.filter(
            phone_number=validated_data["phone_number"]
        ).exists():
            user = CustomUser.objects.filter(
                phone_number=int(validated_data["phone_number"])
            ).first()
            if not user.details_submitted:
                user.name = (
                    validated_data["first_name"] + " " + validated_data["last_name"]
                )
                if "email" in validated_data:
                    user.email = validated_data["email"]
                validated_data["email"] = None
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
                    {"phone_number": "Phone number already exists"}
                )
        else:  # NOT Accessed as we have added @jwt_required() in the view - allows only OTP verified users
            user = CustomUser.objects.create_user(
                name=validated_data["first_name"] + " " + validated_data["last_name"],
                email=validated_data["email"],
                phone_number=int(validated_data["phone_number"]),
                password=password,
                details_submitted=True,
            )
            validated_data["user"] = user

            user_profile = UserProfile.objects.create(**validated_data)
            serialized_user_profile = UserProfileSerializer(user_profile)
            return user, serialized_user_profile.data
