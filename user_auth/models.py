import uuid

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
# pylint: disable=C0115


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("The Phone No.  field must be set")
        try:
            if extra_fields["email"] is not None:
                extra_fields["email"] = self.normalize_email(extra_fields["email"])
        except KeyError:
            pass
        try:
            if extra_fields["name"] is not None:
                name = extra_fields["name"]
                extra_fields.pop("name")
        except KeyError:
            # print("[ERROR]: ", e)
            name = phone_number
        user = self.model(phone_number=phone_number, name=name, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, name, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("name", name)
        return self.create_user(phone_number, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    ## User Details
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone_number = models.BigIntegerField(unique=True, blank=False, null=False)
    details_submitted = models.BooleanField(default=False)
    address = models.TextField(blank=True, null=True)

    ## User Permissions
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.name + "--" + str(self.phone_number)

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.phone_number
        super(CustomUser, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Users"
        ordering = ["name", "email"]


class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.BigIntegerField(unique=True, blank=False, null=False)
    email = models.EmailField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.full_name + "--" + str(self.phone_number)

    def save(self, *args, **kwargs):
        if not self.full_name:
            self.full_name = self.first_name + " " + self.last_name
        super(UserProfile, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "User Profiles"
        ordering = ["full_name", "email"]



class OTP(models.Model):
    """Model for storing OTPs"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    otp_val = models.CharField(max_length=6, editable=False)
    phone_number = models.CharField(max_length=13)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.phone_number) + "-" + self.otp_val

    class Meta:
        verbose_name_plural = "OTP"
        ordering = ["phone_number", "created_at"]
