import graphene

from analytics.queries import AnalyticsQuery
from blood_requests.mutations import RequestMutation
from blood_requests.queries import RequestQuery
from donations.mutations import DonationMutation
from donations.queries import DonationQuery
from hospitals.queries import HospitalQuery
from nft.queries import NFTQuery
from users.mutations import AuthMutation, UserProfileMutation
from users.queries import UserQuery


class Query(
    AnalyticsQuery,
    DonationQuery,
    HospitalQuery,
    NFTQuery,
    RequestQuery,
    UserQuery,
    graphene.ObjectType,
):
    pass


class Mutation(
    AuthMutation,
    DonationMutation,
    RequestMutation,
    UserProfileMutation,
    graphene.ObjectType,
):
    pass


SCHEMA = graphene.Schema(query=Query, mutation=Mutation)
