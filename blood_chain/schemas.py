import graphene

from requests.queries import RequestQuery


class Query(RequestQuery, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    pass


SCHEMA = graphene.Schema(query=Query)
