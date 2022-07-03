from typing import Any

import graphene
import graphene_django
from django.db.models import QuerySet
from graphql import GraphQLError


<<<<<<< HEAD:requests/queries.py
from requests import models, types
from shared.enums import BloodType
from shared.utils import get_profile_from_context


=======
from requests_api import models, types


>>>>>>> origin/MAS-55-nft:requests_api/queries.py


class RequestQuery(graphene.ObjectType):
    request = graphene.Field(types.RequestType, id=graphene.Int())
    requests = graphene_django.DjangoListField(
        types.RequestType, only_eligible=graphene.Boolean(default_value=False)
    )

    def resolve_request(
        root, info: graphene.ResolveInfo, **kwargs: Any
    ) -> models.Request_api:
        try:
            return models.Request_api.objects.get(**kwargs)
        except models.Request_api.DoesNotExist as exc:
            raise GraphQLError(str(exc))

    def resolve_requests(
        root, info: graphene.ResolveInfo, only_eligible: bool
    ) -> QuerySet[models.Request]:
        qs = models.Request.objects.all()
        if only_eligible:
            profile = get_profile_from_context(info)
            if profile.blood_type:
                blood_type = BloodType(profile.blood_type)
                qs = qs.filter(blood_type__in=blood_type.donates_to)

        return qs
