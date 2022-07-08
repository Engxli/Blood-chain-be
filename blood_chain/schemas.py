import graphene

from donations.queries import DonationQuery
from hospitals.queries import HospitalQuery
from nft.queries import NFTQuery
from requests.queries import RequestQuery
from users.mutations import AuthMutation, UserProfileMutation
from users.queries import UserQuery


class Query(
    DonationQuery,
    HospitalQuery,
    NFTQuery,
    RequestQuery,
    UserQuery,
    graphene.ObjectType,
):
    pass


class Mutation(UserProfileMutation, AuthMutation, graphene.ObjectType):
    pass


SCHEMA = graphene.Schema(query=Query, mutation=Mutation)
