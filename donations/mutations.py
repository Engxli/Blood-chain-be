from datetime import datetime

import graphene
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
        req = Request.objects.get(pk=request_id)
        print(req)
        if user.is_anonymous:
            donation = models.Donation.objects.create(
                donator=None, request=req, status = 1
            )
        else:
            if user.profile.can_donate:
                donation = models.Donation.objects.create(
                    donor=user.profile, request=req, status = 1
                )
            else:
                raise GraphQLError("not eligible for donation")
        return CreateDonation(donation=donation)


class CompleteDonation(graphene.Mutation):
    class Arguments:
        donation_id = graphene.Int(required=True)

    donation = graphene.Field(types.DonationType)

    @login_required
    def mutate(
        root, info: graphene.ResolveInfo, donation_id: int
    ) -> "CompleteDonation":
        try:
            donation = models.Donation.objects.get(id=donation_id)
        except models.Donation.DoesNotExist as exc:
            raise GraphQLError(str(exc))
        donation.completed_at = datetime.now()
        donation.status = 2
        donation.save()
        return CompleteDonation(donation=donation)


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
    complete_donation = CompleteDonation.Field()
    delete_donation = DeleteDonation.Field()
