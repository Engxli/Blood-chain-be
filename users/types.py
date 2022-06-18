import graphene_django
from django.contrib.auth import get_user_model

from .models import UserProfile


User = get_user_model()


class UserType(graphene_django.DjangoObjectType):
    class Meta:
        model = User


class UserProfileType(graphene_django.DjangoObjectType):
    class Meta:
        model = UserProfile
