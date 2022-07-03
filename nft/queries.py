import json
from typing import Any
from decouple import config

import graphene
from web3 import Web3

from nft.abi import abi
contract_address = "0x383aE8211d30df791b0Fc162F867908F9e65488a"
w3 = Web3(Web3.HTTPProvider(config("ALCHEMY_API")))

class NFTQuery(graphene.ObjectType):
    nfts = graphene.List( graphene.NonNull(graphene.String), address=graphene.String())

    def resolve_nfts(
        root, info: graphene.ResolveInfo, address: str
    ) -> list:
        contract = w3.eth.contract(address=contract_address, abi=abi)
        return contract.functions.getOwnedNFTs(address).call()
