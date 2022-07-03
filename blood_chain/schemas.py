import graphene

from hospitals.queries import HospitalQuery
from nft.queries import NFTQuery
from requests_api.queries import RequestQuery
from users.mutations import AuthMutation
from users.queries import UserQuery


class Query(
    HospitalQuery, RequestQuery, UserQuery, NFTQuery, graphene.ObjectType
):
    pass


class Mutation(AuthMutation, graphene.ObjectType):
    pass


SCHEMA = graphene.Schema(query=Query, mutation=Mutation)
