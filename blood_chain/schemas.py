import graphene

from users.mutations import AuthMutation


class Query(graphene.ObjectType):
    pass


class Mutation(AuthMutation, graphene.ObjectType):
    pass


SCHEMA = graphene.Schema(mutation=Mutation)
