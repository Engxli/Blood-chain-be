import graphene

from analytics.types import AnalyticsType
from blood_requests.models import Request
from donations.models import Donation


class AnalyticsQuery(graphene.ObjectType):
    analytics = graphene.Field(AnalyticsType)

    def resolve_analytics(root, info: graphene.ResolveInfo) -> "AnalyticsType":
        total_requests = Request.objects.all().count()
        total_donations = Donation.objects.all().count()
        total_cases = total_requests + total_donations
        return AnalyticsType(
            total_requests=total_requests,
            total_donations=total_donations,
            total_cases=total_cases,
        )
