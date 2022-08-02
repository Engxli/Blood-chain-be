import graphene
from django.db.models import QuerySet
from graphql import GraphQLError

from nft.models import NFTMint
from nft.types import NFTMintType
from shared.utils import (
    get_profile_from_context,
    get_used_nfts_mint_from_smart_contract,
)


class NFTMintMutation(graphene.Mutation):

    nfts = graphene.List(NFTMintType)

    def mutate(
        root,
        info: graphene.ResolveInfo,
    ) -> "NFTMintMutation":
        profile = get_profile_from_context(info)
        qs = NFTMint.objects.filter(user=profile, used=False).values_list(
            "signed_message", flat=True
        )
        msgs = list(qs)
        used_messages = get_used_nfts_mint_from_smart_contract(msgs)
        if used_messages is None:
            raise GraphQLError("Invalid signed messages")
        qs2 = NFTMint.objects.filter(signed_message__in=used_messages)
        qs2.update(used=True)
        nfts = NFTMint.objects.filter(user=profile, used=False)
        return NFTMintMutation(nfts=nfts)


class NFTMutation(graphene.ObjectType):
    nft_mint = NFTMintMutation.Field()
