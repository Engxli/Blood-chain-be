import graphene
import graphene_django
from django.contrib.auth import get_user_model

from donations import models
from users.models import UserProfile


User = get_user_model()


class UserType(graphene_django.DjangoObjectType):
    class Meta:
        model = User


class UserProfileType(graphene_django.DjangoObjectType):
    can_donate = graphene.Boolean()

    class Meta:
        model = UserProfile

    def resolve_can_donate(self, info: graphene.ResolveInfo) -> bool:
        profile = models.UserProfile.objects.get(pk=self.id)
        return profile.can_donate
