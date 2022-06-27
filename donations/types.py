import graphene_django

from donations.models import Donation


class DonationType(graphene_django.DjangoObjectType):
    class Meta:
        model = Donation
