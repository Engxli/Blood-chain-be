from typing import Any

import graphene
import graphene_django
from graphql import GraphQLError

from requests import models, types


class RequestQueries(graphene.ObjectType):
    request = graphene.Field(types.RequestType, id=graphene.Int())
    requests = graphene_django.DjangoListField(types.RequestType)

    def resolve_request(
        root, info: graphene.ResolveInfo, **kwargs: Any
    ) -> models.Request:
        try:
            return models.Request.objects.get(**kwargs)
        except models.Request.DoesNotExist as exc:
            raise GraphQLError(str(exc))
