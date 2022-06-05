import graphene

from requests.queries import RequestQueries


class Query(RequestQueries, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    pass


SCHEMA = graphene.Schema(
    query=Query,
)
