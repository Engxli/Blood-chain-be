from typing import Union

from django.db import models
from django.db.models.expressions import Combinable

from shared.enums import BloodType as _BloodType
from shared.models import TimestampMixin
from users.models import UserProfile


_Owner = models.ForeignKey[Union[UserProfile, Combinable], UserProfile]


class Request(TimestampMixin, models.Model):
    BloodType = _BloodType

    class Severity(models.TextChoices):
        LOW = "LOW"
        MEDIUM = "MEDIUM"
        HIGH = "HIGH"

    owner: _Owner = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name="blood_requests",
    )
    blood_type: models.CharField[BloodType, str] = models.CharField(
        max_length=3, choices=BloodType.choices
    )
    severity = models.CharField(max_length=6, choices=Severity.choices)
    quantity = models.PositiveIntegerField()
    details = models.TextField()

    def __str__(self) -> str:
        return (
            f"{self.blood_type} Blood Request from {self.owner.user.username}"
        )
