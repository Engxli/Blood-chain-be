from typing import Any

import graphene
from django.db.models import QuerySet

from nft import models, types
from shared.utils import Web3, get_profile_from_context, smart_contract


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
        return models.NFTMint.objects.filter(user=profile, used=False)
