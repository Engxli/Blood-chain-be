import graphene

from hospitals.queries import HospitalQuery
from requests.queries import RequestQuery
from users.mutations import AuthMutation, UserProfileMutaion
from users.queries import UserQuery


class Query(HospitalQuery, RequestQuery, UserQuery, graphene.ObjectType):
    pass


class Mutation(UserProfileMutaion, AuthMutation, graphene.ObjectType):
    pass


SCHEMA = graphene.Schema(query=Query, mutation=Mutation)
