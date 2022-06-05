import graphene

from hospitals.queries import HospitalQuery

class Query(HospitalQuery,graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    pass


SCHEMA = graphene.Schema(query=Query)
