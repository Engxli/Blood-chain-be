from typing import Any

import graphene
import graphene_django
from graphql import GraphQLError

from requests import models, types


class RequestQuery(graphene.ObjectType):
    request = graphene.Field(types.RequestType, id=graphene.Int())
    requests = graphene_django.DjangoListField(
        types.RequestType,
        only_eligible=graphene.Boolean(required=False, default_value=False),
    )

    def resolve_request(
        root, info: graphene.ResolveInfo, **kwargs: Any
    ) -> models.Request:
        try:
            return models.Request.objects.get(**kwargs)
        except models.Request.DoesNotExist as exc:
            raise GraphQLError(str(exc))

    def resolve_requests(
        root, info: graphene.ResolveInfo, only_eligible: bool
    ) -> Any:

        if only_eligible and info.context.user.is_authenticated:
            if info.context.user.profile.blood_type:
                return models.Request.objects.filter(
                    blood_type__in=info.context.user.profile.blood_type.donate_to
                )
        return models.Request.objects.all()
