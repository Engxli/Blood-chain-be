from typing import Any

import graphene
import graphene_django
from graphql import GraphQLError

from hospitals import models, types
import hospitals


class HospitalQuery(graphene.ObjectType):
    hospital = graphene.Field(types.HospitalType, id=graphene.Int())
    hospitals = graphene_django.DjangoListField(types.HospitalType)

    def resolve_hospital(
        root, info: graphene.ResolveInfo, **kwargs: Any
    ) -> models.Hospital:
        try:
            return models.Hospital.objects.get(**kwargs)
        except models.Hospital.DoesNotExist as exc:
            raise GraphQLError(str(exc))
