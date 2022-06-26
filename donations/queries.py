from typing import Any

import graphene
import graphene_django
from django.db.models import QuerySet

from donations import models, types


class DonationQuery(graphene.ObjectType):
    donations = graphene_django.DjangoListField(
        types.DonationType, pending=graphene.Boolean()
    )

    def resolve_donations(
        root, info: graphene.ResolveInfo, **kwargs: Any
    ) -> QuerySet[models.Donation]:

        if kwargs and kwargs.pop("pending"):
            return models.Donation.objects.filter(
                status=1, donor__user_id=info.context.user.id
            )

        return models.Donation.objects.filter(
            donor__user_id=info.context.user.id
        )
