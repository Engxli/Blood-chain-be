import graphene_django

from requests import models
from users.types import UserType


class RequestType(UserType, graphene_django.DjangoObjectType):
    class Meta:
        model = models.Request
