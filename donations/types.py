import graphene_django

from donations import models


class DonationType(graphene_django.DjangoObjectType):
    class Meta:
        model = models.Donation
        convert_choices_to_enum = False
