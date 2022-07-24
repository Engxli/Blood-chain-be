from django.db import models

from shared.models import TimestampMixin
from users.models import UserProfile


class Donation(TimestampMixin, models.Model):
    class Status(models.IntegerChoices):
        PENDING = 1
        COMPLETE = 2
        CANCELED = 3

    status = models.IntegerField(choices=Status.choices, null=True)
    request = models.ForeignKey(
        "requests.Request",
        null=True,
        on_delete=models.CASCADE,
        related_name="donations",
    )
    donor = models.ForeignKey(
        UserProfile,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="donations",
    )
    completed_at = models.DateTimeField(null=True, blank=True)
    verification = models.ImageField(null=True)

    def __str__(self) -> str:
        donor = self.donor
        requester = self.request.owner if self.request else None
        return f"{donor}'s Donation for {requester}'s request"
