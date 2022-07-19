from datetime import timedelta
from typing import Optional, Union

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Q
from django.db.models.expressions import Combinable
from django.utils import timezone

from shared.enums import BloodType as _BloodType


_User = models.OneToOneField[
    Union["CustomUser", Combinable, None], Union["CustomUser", None]
]


class CustomUser(AbstractUser):
    pass


class UserProfile(models.Model):
    BloodType = _BloodType

    user: _User = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
        null=True,
        blank=True,
    )
    crypto_wallet = models.CharField(max_length=35, default="", blank=True)
    phone = models.CharField(max_length=8, default="", blank=True)
    blood_type: models.CharField[_BloodType, Optional[str]] = models.CharField(
        max_length=3, choices=BloodType.choices, null=True
    )

    def __str__(self) -> str:
        if user := self.user:
            return f"UserProfile: {user}"

        return f"Guest User {self.phone}"

    @property
    def can_donate(self) -> bool:
        from donations.models import Donation

        latest_valid_date = timezone.now() - timedelta(days=7 * 12)
        donation = Donation.objects.filter(
            Q(completed_at__gt=latest_valid_date) | Q(completed_at=None),
            donor=self,
        )
        return not donation.exists()

    class Meta:
        verbose_name = "Profile"
