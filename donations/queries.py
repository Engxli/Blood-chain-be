from typing import Any

import graphene
import graphene_django
from django.db.models import QuerySet

from donations import models, types


class DonationQuery(graphene.ObjectType):
    user_donations = graphene_django.DjangoListField(
        types.DonationType, pending=graphene.Boolean()
    )
    request_donations = graphene_django.DjangoListField(
        types.DonationType, request_id=graphene.String()
    )

    def resolve_user_donations(
        root, info: graphene.ResolveInfo, **kwargs: Any
    ) -> QuerySet[models.Donation]:

        if kwargs.pop("pending", False):
            return models.Donation.objects.filter(
                status=models.Donation.Status.PENDING,
                donor__user_id=info.context.user.id,
            )

        return models.Donation.objects.filter(
            donor__user_id=info.context.user.id
        )

    def resolve_request_donations(
        root, info: graphene.ResolveInfo, request_id: int
    ) -> QuerySet[models.Donation]:
        return models.Donation.objects.filter(request__id=request_id)
