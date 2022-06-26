from typing import Any

import graphene
import graphene_django
from django.db.models import QuerySet

from donations import types
from donations.models import Donation


class DonationQuery(graphene.ObjectType):
    donations = graphene_django.DjangoListField(types.DonationType)
    pending_donations = graphene_django.DjangoListField(types.DonationType)

    def resolve_pending_donations(
        root, info: graphene.ResolveInfo, **kwargs: Any
    ) -> QuerySet[Donation]:
        return Donation.objects.filter(
            status="PENDING", donor__user_id=info.context.user.id
        )


# make options for fe to filter by Fe
