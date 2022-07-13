import graphene

from blood_requests.models import Request
from blood_requests.types import BloodTypeEnum, RequestType
from blood_requests.utils import PositiveIntField
from shared.enums import BloodType
from shared.utils import get_graphene_enum, get_profile_from_context


SeverityTypeEnum = get_graphene_enum(Request.Severity)


class CreateBloodRequest(graphene.Mutation):
    request = graphene.Field(RequestType)

    class Arguments:
        blood_type = BloodTypeEnum()
        severity = SeverityTypeEnum()
        quantity = graphene.Argument(PositiveIntField)
        details = graphene.String()

    def mutate(
        root,
        info: graphene.ResolveInfo,
        blood_type: BloodType,
        severity: Request.Severity,
        quantity: int,
        details: str,
    ) -> Request:
        owner = get_profile_from_context(info)

        blood_request = Request.objects.create(
            owner=owner,
            blood_type=blood_type,
            severity=severity,
            quantity=quantity,
            details=details,
        )

        return CreateBloodRequest(request=blood_request)


class RequestMutation(graphene.ObjectType):
    create_blood_request = CreateBloodRequest.Field()
