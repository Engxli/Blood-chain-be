from typing import Any

import graphene
from graphene_file_upload.scalars import Upload
from graphql import GraphQLError
from graphql_jwt.decorators import login_required

from blood_requests.models import Request
from donations import models, types
from shared.utils import get_user_from_context


class CreateDonation(graphene.Mutation):
    class Arguments:
        request_id = graphene.Int(required=True)

    donation = graphene.Field(types.DonationType)

    def mutate(
        root, info: graphene.ResolveInfo, request_id: int
    ) -> "CreateDonation":
        user = get_user_from_context(info)
        try:
            req = Request.objects.get(pk=request_id)
        except Request.DoesNotExist as exc:
            raise GraphQLError(str(exc))

        if req.status != Request.Status.ONGOING:
            raise GraphQLError("Request is no longer ongoing")

        if user.is_anonymous:
            donation = models.Donation.objects.create(
                donator=None,
                request=req,
                status=models.Donation.Status.PENDING,
            )
        else:
            if user.profile.can_donate:
                donation = models.Donation.objects.create(
                    donor=user.profile,
                    request=req,
                    status=models.Donation.Status.PENDING,
                )
            else:
                raise GraphQLError("not eligible for donation")
        return CreateDonation(donation=donation)


class CancelDonation(graphene.Mutation):
    class Arguments:
        donation_id = graphene.Int(required=True)

    donation = graphene.Field(types.DonationType)

    @login_required
    def mutate(
        root, info: graphene.ResolveInfo, donation_id: int
    ) -> "CancelDonation":
        try:
            donation = models.Donation.objects.get(id=donation_id)
        except models.Donation.DoesNotExist as exc:
            raise GraphQLError(str(exc))
        if donation.status != donation.Status.PENDING:
            raise GraphQLError("donation is already complete")
        donation.status = donation.Status.CANCELED
        donation.save()
        return CancelDonation(donation=donation)


class CompleteDonationRequest(graphene.Mutation):
    class Arguments:
        donation_id = graphene.Int(required=True)
        image = Upload(required=True)

    donation = graphene.Field(types.DonationType)

    @login_required
    def mutate(
        root, info: graphene.ResolveInfo, **kwargs: Any
    ) -> "CompleteDonationRequest":
        try:
            donation = models.Donation.objects.get(
                id=kwargs.pop("donation_id")
            )
        except models.Donation.DoesNotExist as exc:
            raise GraphQLError(str(exc))

        for attr, value in kwargs.items():
            setattr(donation, attr, value)
        donation.save()
        return CompleteDonationRequest(donation=donation)


class DeleteDonation(graphene.Mutation):
    class Arguments:
        donation_id = graphene.Int()

    status = graphene.Boolean()

    @login_required
    def mutate(
        root, info: graphene.ResolveInfo, donation_id: int
    ) -> "DeleteDonation":
        try:
            donation = models.Donation.objects.get(id=donation_id)
        except models.Donation.DoesNotExist:
            return DeleteDonation(status=False)
        donation.delete()
        return DeleteDonation(status=True)


class DonationMutation(graphene.ObjectType):
    create_donation = CreateDonation.Field()
    cancel_donation = CancelDonation.Field()
    complete_donation_request = CompleteDonationRequest.Field()
    delete_donation = DeleteDonation.Field()
