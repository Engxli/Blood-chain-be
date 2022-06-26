from typing import Iterable

import graphene
import graphene_django

from donations.models import Donation
from donations.types import DonationType
from requests import models
from shared.utils import get_graphene_enum
from users.types import UserProfileType


BloodTypeEnum = get_graphene_enum(models.Request.BloodType)


class RequestType(graphene_django.DjangoObjectType):
    owner = graphene.Field(UserProfileType)
    blood_type = graphene.Field(BloodTypeEnum)
    donations = graphene.List(DonationType)

    def resolve_donations(
        self, info: graphene.ResolveInfo
    ) -> Iterable[Donation]:
        return Donation.objects.filter(request_id=self.id)

    class Meta:
        model = models.Request
