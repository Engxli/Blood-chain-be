from typing import Any, Iterable

import graphene
import graphene_django
from graphql import GraphQLError

from donations import models, types


class DonationQuery(graphene.ObjectType):
    donations = graphene_django.DjangoListField(types.DonationType)
    pending_donations = graphene_django.DjangoListField(types.DonationType)

    def resolve_pending_donations(
        root, info: graphene.ResolveInfo, **kwargs: Any
    ) -> Iterable[models.Donation]:
        try:
            return models.Donation.objects.filter(
                status="PENDING", donor__user_id=info.context.user.id
            )
        except models.Donation.DoesNotExist as exc:
            raise GraphQLError(str(exc))
