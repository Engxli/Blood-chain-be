import graphene
import graphene_django

from requests import types


class DonationQuery(graphene.ObjectType):
    donations = graphene_django.DjangoListField(types.DonationType)
