from typing import Any

import graphene
import graphene_django
from django.db.models import QuerySet

from donations import models, types


class DonationQuery(graphene.ObjectType):
    donations = graphene_django.DjangoListField(types.DonationType)
    pending_donations = graphene_django.DjangoListField(types.DonationType)

    def resolve_pending_donations(
        root, info: graphene.ResolveInfo, **kwargs: Any
    ) -> QuerySet[models.Donation]:
        return models.Donation.objects.filter(
            status="PENDING", donor__user_id=info.context.user.id
        )


# make options for fe to filter by Fe
