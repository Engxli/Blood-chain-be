from typing import Any

import graphene
from decouple import config
from web3 import Web3
from web3.types import ENS

from nft.abi import abi


w3 = Web3(Web3.HTTPProvider(config("ALCHEMY_API", default="")))


con = w3.eth.contract(
    address=ENS("0x383aE8211d30df791b0Fc162F867908F9e65488a"), abi=abi
)


class NFTQuery(graphene.ObjectType):
    nfts = graphene.List(
        graphene.NonNull(graphene.String), address=graphene.String()
    )

    def resolve_nfts(root, info: graphene.ResolveInfo, address: str) -> Any:
        return con.functions.getOwnedNFTs(address).call()
