import graphene
from graphql import GraphQLError

from nft.models import NFTMint
from shared.utils import get_used_nfts_mint_from_smart_contract


class NFTMintMutation(graphene.Mutation):
    class Arguments:
        signed_messages = graphene.List(graphene.String)

    status = graphene.Boolean()

    def mutate(
        root,
        info: graphene.ResolveInfo,
        signed_messages: list[str],
    ) -> "NFTMintMutation":
        used_messages = get_used_nfts_mint_from_smart_contract(signed_messages)
        if used_messages is None:
            raise GraphQLError("Invalid signed messages")

        qs = NFTMint.objects.filter(signed_message__in=used_messages)
        qs.update(used=True)
        return NFTMintMutation(status=True)


class NFTMutation(graphene.ObjectType):
    nft_mint = NFTMintMutation.Field()
