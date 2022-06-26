from django.db import models

from requests.models import Request
from shared.models import TimestampMixin
from users.models import UserProfile


class Donation(TimestampMixin, models.Model):
    class Status(models.IntegerChoices):
        PENDING = 1
        COMPLETE = 2
        CANCELED = 3

    status = models.IntegerField(choices=Status.choices)
    request = models.ForeignKey(
        Request, on_delete=models.CASCADE, related_name="donations"
    )
    donor = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="donations"
    )

    def __str__(self) -> str:
        return f"{self.donor.user.username}'s Donation for {self.request.owner.user.username}'s request"
