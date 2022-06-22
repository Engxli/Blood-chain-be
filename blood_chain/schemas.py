import graphene

from hospitals.queries import HospitalQuery
from requests.queries import RequestQuery
from users.mutations import AuthMutation
from users.queries import UserQuery


class Query(HospitalQuery, RequestQuery, UserQuery, graphene.ObjectType):
    pass


class Mutation(AuthMutation, graphene.ObjectType):
    pass


SCHEMA = graphene.Schema(mutation=Mutation, query=Query)
