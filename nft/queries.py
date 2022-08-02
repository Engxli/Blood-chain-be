from typing import Any

import graphene
from django.db.models import QuerySet
from graphql import GraphQLError

from nft import models, types
from shared.utils import (
    Web3,
    get_profile_from_context,
    get_used_nfts_mint_from_smart_contract,
    smart_contract,
)


class NFTQuery(graphene.ObjectType):
    nfts = graphene.List(types.NFTType, address=graphene.String())

    nft_mint = graphene.List(types.NFTMintType)

    def resolve_nfts(root, info: graphene.ResolveInfo, address: str) -> Any:
        owned_nfts = smart_contract.functions.owned_nfts(
            Web3.toChecksumAddress(address)
        ).call()
        return models.NFT.objects.filter(id__in=owned_nfts)

    def resolve_nft_mint(
        root, info: graphene.ResolveInfo
    ) -> QuerySet[models.NFTMint]:
        profile = get_profile_from_context(info)
        qs = models.NFTMint.objects.filter(
            user=profile, used=False
        ).values_list("signed_message", flat=True)
        msgs = list(qs)
        used_messages = get_used_nfts_mint_from_smart_contract(msgs)
        if used_messages is None:
            raise GraphQLError("Invalid signed messages")
        qs2 = models.NFTMint.objects.filter(signed_message__in=used_messages)
        qs2.update(used=True)
        return models.NFTMint.objects.filter(user=profile, used=False)
