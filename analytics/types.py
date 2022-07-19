import graphene


class AnalyticsType(graphene.ObjectType):
    total_requests = graphene.Int()
    total_donations = graphene.Int()
    total_cases = graphene.Int()
