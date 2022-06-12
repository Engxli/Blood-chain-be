from django.conf import settings
from django.db import models

from shared.models import TimestampMixin


class Request(TimestampMixin, models.Model):
    BLOOD_CHOICES = (
        ("A-", "A-"),
        ("A+", "A+"),
        ("B-", "B-"),
        ("B+", "B+"),
        ("O-", "O-"),
        ("O+", "O+"),
        ("AB-", "AB-"),
        ("AB+", "AB+"),
    )
    SEVERITY_CHOICES = (
        ("LOW", "LOW"),
        ("MEDIUM", "MEDIUM"),
        ("HIGH", "HIGH"),
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="request_owner",
    )
    blood_type = models.CharField(max_length=3, choices=BLOOD_CHOICES)
    severity = models.CharField(max_length=6, choices=SEVERITY_CHOICES)
    quantity = models.PositiveIntegerField()
    details = models.TextField()
    donors = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="request_donor",
    )
