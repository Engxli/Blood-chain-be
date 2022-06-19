from django.conf import settings
from django.db import models

from shared.models import TimestampMixin


class Request(TimestampMixin, models.Model):
    class BloodType(models.TextChoices):
        Amin = "A-"
        Apos = "A+"
        Omin = "O-"
        Opos = "O+"
        Bmin = "B-"
        Bpos = "B+"
        ABmin = "AB-"
        ABpos = "AB+"

    class Severity(models.TextChoices):
        LOW = "LOW"
        MEDIUM = "MEDIUM"
        HIGH = "HIGH"

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="request_owner",
    )
    blood_type = models.CharField(max_length=3, choices=BloodType.choices)
    severity = models.CharField(max_length=6, choices=Severity.choices)
    quantity = models.PositiveIntegerField()
    details = models.TextField()
    donors = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="request_donor",
    )
