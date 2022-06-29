from typing import Any

import graphene
import graphene_django
from django.db.models import QuerySet
from graphql import GraphQLError

from requests import models, types
from shared.enums import BloodType
from shared.utils import get_user_from_context


class RequestQuery(graphene.ObjectType):
    request = graphene.Field(types.RequestType, id=graphene.Int())
    requests = graphene_django.DjangoListField(
        types.RequestType, only_eligible=graphene.Boolean(default_value=False)
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
    ) -> QuerySet[models.Request]:
        user = get_user_from_context(info)
        if only_eligible and user.is_anonymous:
            raise GraphQLError(
                "cannot filter for only eligible blood types without logging in"
            )
        if only_eligible and user.is_authenticated:
            if user.profile.blood_type:
                return models.Request.objects.filter(
                    blood_type__in=BloodType(
                        user.profile.blood_type
                    ).donates_to
                )
        return models.Request.objects.all()
