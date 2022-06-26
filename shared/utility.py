import graphene
from graphql import GraphQLError

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
        raise GraphQLError("login required!")
    return user.profile
