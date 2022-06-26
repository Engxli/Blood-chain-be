from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from shared.enums import BloodType as _BloodType


class CustomUser(AbstractUser):
    pass


class UserProfile(models.Model):
    BloodType = _BloodType

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    crypto_wallet = models.CharField(max_length=35, default="", blank=True)
    phone = models.CharField(max_length=8, default="", blank=True)
    blood_type = models.CharField(
        max_length=3,
        choices=BloodType.choices,
        default=BloodType.ABmin,
        blank=True,
    )

    def __str__(self) -> str:
        return self.user.email

    class Meta:
        verbose_name = "Profile"
