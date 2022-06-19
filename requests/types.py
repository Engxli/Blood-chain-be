import graphene
import graphene_django

from requests import models
from users.types import UserType


class RequestType(graphene_django.DjangoObjectType):
    owner = graphene.Field(UserType)
    # donors = graphene.

    class Meta:
        model = models.Request
