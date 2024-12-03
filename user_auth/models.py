import uuid

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

# pylint: disable=C0115


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        try:
            if extra_fields["phone_number"] is not None:
                extra_fields["phone_number"] = int(extra_fields["phone_number"])
        except KeyError or TypeError:
            pass
        try:
            if extra_fields["name"] is not None:
                name = extra_fields["name"]
                extra_fields.pop("name")
        except KeyError:
            name = email
        user = self.model(email=email, name=name, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("name", name)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    ## User Details
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True, null=False, blank=False)
    phone_number = models.BigIntegerField(blank=True, null=True)

    details_submitted = models.BooleanField(default=False)
    address = models.TextField(blank=True, null=True)

    ## User Permissions
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return str(self.name) + "--" + str(self.email)

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
    phone_number = models.BigIntegerField(blank=True, null=True)
    email = models.EmailField(null=False, blank=False)

    def __str__(self):
        return str(self.full_name) + "--" + str(self.email)

    def save(self, *args, **kwargs):
        if not self.full_name:
            self.full_name = str(self.first_name) + " " + str(self.last_name)
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
        return str(self.phone_number) + "-" + str(self.otp_val)

    class Meta:
        verbose_name_plural = "OTP"
        ordering = ["phone_number", "created_at"]
