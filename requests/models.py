from django.conf import settings
from django.db import models


# from hospitals import models

# Create your models here.
class Request(models.Model):
    # blood type choices
    BLOOD_CHOICES = (
        ("1", "A-"),
        ("2", "A+"),
        ("3", "B-"),
        ("4", "B+"),
        ("5", "O-"),
        ("6", "O+"),
        ("7", "AB-"),
        ("8", "AB+"),
    )
    # severity choices
    SEVERITY_CHOICES = (
        ("1", "LOW"),
        ("2", "MEDIUM"),
        ("3", "HIGH"),
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="request_owner",
    )
    blood_type = models.CharField(max_length=1, choices=BLOOD_CHOICES)
    severity = models.CharField(max_length=1, choices=SEVERITY_CHOICES)
    quantity = models.IntegerField()
    # hospital = models.ForeignKey(models.Hospital, on_delete=models.CASCADE,related_name="request")
    details = models.TextField()
    donors = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="request_donor",
    )
    created_at = models.DateTimeField(auto_now_add=True)
