import graphene_django

from users import models


class UserType(graphene_django.DjangoObjectType):
    class Meta:
        model = models.CustomUser
        fields = ["id", "username"]
