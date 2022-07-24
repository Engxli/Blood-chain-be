from typing import Any

import graphene
from graphql import GraphQLError
from graphql_jwt.decorators import login_required

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

class CancelBloodRequest(graphene.Mutation):
    class Arguments:
        request_id = graphene.Int(required=True)

    request = graphene.Field(RequestType)

    @login_required
    def mutate(
        root, info: graphene.ResolveInfo, request_id: int
    ) -> "CancelBloodRequest":
        try:
            request = Request.objects.get(id=request_id)
        except Request.DoesNotExist as exc:
            raise GraphQLError(str(exc))
        if request.status != request.Status.ONGOING:
            raise GraphQLError("Request is not ongoing")
        request.status = request.Status.CANCELED
        request.save()
        return CancelBloodRequest(request=request)

class CompleteBloodRequest(graphene.Mutation):
    class Arguments:
        request_id = graphene.Int(required=True)

    request = graphene.Field(RequestType)

    @login_required
    def mutate(
        root, info: graphene.ResolveInfo, request_id: int
    ) -> "CompleteBloodRequest":
        try:
            request = Request.objects.get(id=request_id)
        except Request.DoesNotExist as exc:
            raise GraphQLError(str(exc))
        if request.status != request.Status.ONGOING:
            raise GraphQLError("Request is not ongoing")
        request.status = request.Status.COMPLETE
        request.save()
        return CompleteBloodRequest(request=request)


class RequestMutation(graphene.ObjectType):
    create_blood_request = CreateBloodRequest.Field()
    cancel_blood_request = CancelBloodRequest.Field()
    complete_blood_request = CompleteBloodRequest.Field()
