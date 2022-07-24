from typing import Any

import graphene

from blood_requests.models import Request
from blood_requests.types import BloodTypeEnum, RequestType
from shared.scalars import PositiveIntField
from shared.utils import get_graphene_enum, get_profile_from_context


SeverityTypeEnum = get_graphene_enum(Request.Severity)


class CreateBloodRequest(graphene.Mutation):
    request = graphene.Field(RequestType)

    class Arguments:
        blood_type = BloodTypeEnum()
        severity = SeverityTypeEnum()
        quantity = graphene.Argument(PositiveIntField)
        file_number = graphene.Int(required=True)
        details = graphene.String()

    def mutate(
        root,
        info: graphene.ResolveInfo,
        **kwargs: Any,
    ) -> Request:
        owner = get_profile_from_context(info)
        blood_request = Request.objects.create(**kwargs, owner=owner)

        return CreateBloodRequest(request=blood_request)


class RequestMutation(graphene.ObjectType):
    create_blood_request = CreateBloodRequest.Field()
