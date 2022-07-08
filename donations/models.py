from django.db import models

from blood_requests.models import Request
from shared.models import TimestampMixin
from users.models import UserProfile


class Donation(TimestampMixin, models.Model):
    class Status(models.IntegerChoices):
        PENDING = 1
        COMPLETE = 2
        CANCELED = 3

    status = models.IntegerField(choices=Status.choices, null=True)
    request = models.ForeignKey(
        Request, null=True, on_delete=models.CASCADE, related_name="donations"
    )
    donor = models.ForeignKey(
        UserProfile,
        null=True,
        on_delete=models.CASCADE,
        related_name="donations",
    )

    def __str__(self) -> str:
        donor = self.donor.user.username if self.donor else "Unknown"
        requester = (
            self.request.owner.user.username if self.request else "Unknown"
        )
        return f"{donor}'s Donation for {requester}'s request"
