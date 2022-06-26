from django.db import models

from shared.enums import BloodType as _BloodType
from shared.models import TimestampMixin
from users.models import UserProfile


class Request(TimestampMixin, models.Model):
    BloodType = _BloodType

    class Severity(models.TextChoices):
        LOW = "LOW"
        MEDIUM = "MEDIUM"
        HIGH = "HIGH"

    owner = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name="blood_requests",
    )
    blood_type = models.CharField(max_length=3, choices=BloodType.choices)
    severity = models.CharField(max_length=6, choices=Severity.choices)
    quantity = models.PositiveIntegerField()
    details = models.TextField()

    def __str__(self) -> str:
        return (
            f"{self.blood_type} Blood Request from {self.owner.user.username}"
        )
