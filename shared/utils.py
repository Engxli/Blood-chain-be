import graphene
from django.db.models import Choices
from graphql_jwt.exceptions import PermissionDenied

from users.models import CustomUser, UserProfile


def get_user_from_context(
    info: graphene.ResolveInfo,
) -> CustomUser:
    return info.context.user


def get_profile_from_context(
    info: graphene.ResolveInfo,
) -> UserProfile:
    user = get_user_from_context(info)
    if user.is_anonymous:
        raise PermissionDenied
    return user.profile


def get_graphene_enum(enum: type[Choices]) -> graphene.Enum:
    return graphene.Enum.from_enum(enum)
