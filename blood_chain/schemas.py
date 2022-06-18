import graphene

from users.mutations import AuthMutation
from users.queries import UserQuery


class Query(UserQuery, graphene.ObjectType):
    pass


class Mutation(AuthMutation, graphene.ObjectType):
    pass


SCHEMA = graphene.Schema(mutation=Mutation, query=Query)
