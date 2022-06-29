import graphene
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
