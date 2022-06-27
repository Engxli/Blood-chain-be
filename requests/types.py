import graphene
import graphene_django

from requests import models
from users.types import UserProfileType


class RequestType(graphene_django.DjangoObjectType):
    owner = graphene.Field(UserProfileType)

    class Meta:
        model = models.Request
