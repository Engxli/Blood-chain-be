from typing import Any

import graphene
import graphene_django
from graphql import GraphQLError

from requests import models, types


class RequestQuery(graphene.ObjectType):
    request = graphene.Field(types.RequestType, id=graphene.Int())
    requests = graphene_django.DjangoListField(
        types.RequestType,
        only_eligible=graphene.Boolean(required=False, default_value=None),
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
        blood_list_eligible = {
            "A-": ["A-", "O-"],
            "A+": ["A-", "A+", "O+", "O-"],
            "B-": ["B-", "O-"],
            "B+": ["B-", "B+", "O+", "O-"],
            "AB-": ["A-", "O-", "B-", "AB-"],
            "AB+": ["A-", "A+", "O+", "O-", "AB+", "AB-", "B-", "B+"],
            "O+": ["O+", "O-"],
            "O-": ["O-"],
        }

        if only_eligible and info.context.user.is_active:
            if info.context.user.profile.blood_type:
                return models.Request.objects.filter(
                    blood_type__in=blood_list_eligible.get(
                        info.context.user.profile.blood_type
                    )
                )
        return models.Request.objects.all()
