import graphene
import graphene_django

from donations.types import DonationType
from requests import models
from shared.utils import get_graphene_enum
from users.types import UserProfileType


BloodTypeEnum = get_graphene_enum(models.Request.BloodType)


class RequestType(graphene_django.DjangoObjectType):
    owner = graphene.Field(UserProfileType)
    blood_type = graphene.Field(BloodTypeEnum)
    donations = graphene.Field(DonationType)

    class Meta:
        model = models.Request
