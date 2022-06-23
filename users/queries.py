from graphene import Field, ObjectType, ResolveInfo
from graphql_auth.schema import MeQuery

from users.models import UserProfile
from users.types import UserProfileType


class UserQuery(MeQuery, ObjectType):
    profile = Field(UserProfileType)

    def resolve_profile(root, info: ResolveInfo) -> UserProfile:

        try:
            profile = UserProfile.objects.get(user_id=info.context.user.id)
        except UserProfile.DoesNotExist:
            profile = UserProfile.objects.create(user=info.context.user)

        return profile
