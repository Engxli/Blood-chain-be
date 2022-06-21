import graphene
from graphql_auth.schema import MeQuery


class UserQuery(MeQuery, graphene.ObjectType):
    pass
