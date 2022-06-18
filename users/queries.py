import graphene
from graphql_auth.schema import MeQuery

from users.types import UserProfileType

from .models import UserProfile


class UserQuery(MeQuery, graphene.ObjectType):
    profile = graphene.Field(UserProfileType)

    def resolve_profile(root, info: graphene.ResolveInfo) -> UserProfile:
        profile = UserProfile.objects.get(user_id=info.context.user.id)
        if profile:
            return profile
        return UserProfile.objects.create(user=info.context.user)
