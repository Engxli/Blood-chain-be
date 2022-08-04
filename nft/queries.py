from typing import Any

import graphene

from nft import models, types
from shared.utils import Web3, smart_contract


class NFTQuery(graphene.ObjectType):
    nfts = graphene.List(types.NFTType, address=graphene.String())

    def resolve_nfts(root, info: graphene.ResolveInfo, address: str) -> Any:
        owned_nfts = smart_contract.functions.owned_nfts(
            Web3.toChecksumAddress(address)
        ).call()
        return models.NFT.objects.filter(id__in=owned_nfts)
