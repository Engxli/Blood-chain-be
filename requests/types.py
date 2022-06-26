from typing import Iterable

import graphene
import graphene_django

from donations.models import Donation
from donations.types import DonationType
from requests import models
from users.types import UserProfileType


class RequestType(graphene_django.DjangoObjectType):
    owner = graphene.Field(UserProfileType)
    donations = graphene.List(DonationType)

    def resolve_donations(
        self, info: graphene.ResolveInfo
    ) -> Iterable[Donation]:
        return Donation.objects.filter(request_id=self.id)

    class Meta:
        model = models.Request
