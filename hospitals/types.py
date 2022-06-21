import graphene_django

from hospitals import models


class HospitalType(graphene_django.DjangoObjectType):
    class Meta:
        model = models.Hospital
