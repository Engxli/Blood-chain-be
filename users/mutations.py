from typing import Any

import graphene
from graphql_auth import mutations
from graphql_jwt.exceptions import PermissionDenied

from requests.types import BloodTypeEnum
from shared.utils import get_profile_from_context
from users import types


class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    login = mutations.ObtainJSONWebToken.Field()


class UpdateProfile(graphene.Mutation):
    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()
        crypto_wallet = graphene.String()
        blood_type = BloodTypeEnum()

    profile = graphene.Field(types.UserProfileType)

    def mutate(
        root, info: graphene.ResolveInfo, **kwargs: Any
    ) -> "UpdateProfile":
        profile = get_profile_from_context(info)
        for key, value in kwargs.items():
            if key in ["first_name", "last_name", "email"]:
                setattr(profile.user, key, value)
            else:
                setattr(profile, key, value)
        profile.user.save()
        profile.save()
        return UpdateProfile(profile=profile)


class DeleteProfile(graphene.Mutation):
    status = graphene.Boolean()

    def mutate(
        root, info: graphene.ResolveInfo, **kwargs: Any
    ) -> "DeleteProfile":
        try:
            profile = get_profile_from_context(info)
        except PermissionDenied:
            return DeleteProfile(status=False)
        profile.user.delete()
        return DeleteProfile(status=True)

class UserProfileMutaion(graphene.ObjectType):
    update_profile = UpdateProfile.Field()
    delete_profile = DeleteProfile.Field()
