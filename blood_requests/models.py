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
    
    class Status(models.IntegerChoices):
        ONGOING = 1
        COMPLETE = 2
        CANCELED = 3

    owner: _Owner = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name="blood_requests",
    )
    blood_type: models.CharField[_BloodType, str] = models.CharField(
        max_length=3, choices=BloodType.choices
    )
    file_number = models.IntegerField(null=True)
    severity = models.CharField(max_length=6, choices=Severity.choices)
    status = models.IntegerField(choices=Status.choices, null=True)
    quantity = models.PositiveIntegerField()
    details = models.TextField(blank=True, default="")

    def __str__(self) -> str:
        return f"{self.blood_type} Blood Request from {self.owner}"
