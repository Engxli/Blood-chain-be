from django.db import models

from requests.models import Request
from shared.models import TimestampMixin
from users.models import UserProfile


class Donation(TimestampMixin, models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING"
        COMPLETE = "COMPLETE"
        CANCELED = "CANCELED"

    status = models.CharField(max_length=8, choices=Status.choices)
    request = models.ForeignKey(
        Request, on_delete=models.CASCADE, related_name="donations"
    )
    donor = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="donations"
    )

    def __str__(self) -> str:
        return f"{self.donor.user.username}'s Donation for {self.request.owner.user.username}'s request"
