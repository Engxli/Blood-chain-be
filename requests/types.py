import graphene_django

from requests import models


class RequestType(graphene_django.DjangoObjectType):
    class Meta:
        model = models.Request
