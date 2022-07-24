import calendar
import time
from typing import Any, Optional

import graphene
from decouple import config
from django.db.models import Choices
from eth_account.messages import encode_defunct
from graphql_jwt.exceptions import PermissionDenied
from web3 import Web3
from web3.types import ENS

from nft.abi import abi, contract_address
from nft.models import NFTMint
from users.models import CustomUser, UserProfile


w3 = Web3(Web3.HTTPProvider(config("ALCHEMY_API", default="")))
smart_contract = w3.eth.contract(address=ENS(contract_address), abi=abi)
private_key = config("PRIVATE_KEY", default="")


def get_user_from_context(
    info: graphene.ResolveInfo,
) -> CustomUser:
    return info.context.user


def get_profile_from_context(
    info: graphene.ResolveInfo,
) -> UserProfile:
    user = get_user_from_context(info)
    if user.is_anonymous:
        raise PermissionDenied
    return user.profile


def get_graphene_enum(enum: type[Choices]) -> graphene.Enum:
    return graphene.Enum.from_enum(enum)


def give_permission_to_mint(
    profile: UserProfile, amount: Optional[str] = ""
) -> None:
    address = profile.crypto_wallet
    # address must not be empty
    if address:

        def to_32byte_hex(val: Any) -> Any:
            return Web3.toHex(Web3.toBytes(val).rjust(32, b"\0"))

        # Current GMT time in a tuple format
        current_GMT = time.gmtime()
        # ts stores timestamp
        ts = str(calendar.timegm(current_GMT))
        _msg = encode_defunct(text=(address.lower() + ts))
        signature = w3.eth.account.sign_message(_msg, private_key=private_key)
        nft_mint = {
            "ts": ts,
            "signed_message": Web3.toHex(signature.messageHash),
            "signature_v": signature.v,
            "signature_r": to_32byte_hex(signature.r),
            "signature_s": to_32byte_hex(signature.s),
        }
        NFTMint.objects.create(**nft_mint, user=profile)


def get_used_nfts_mint_from_smart_contract(
    signed_messages: list[str],
) -> list[Any]:
    returned_values = smart_contract.functions.check_used_signed(
        signed_messages
    ).call()
    only_used_messages = (value for value in returned_values if value[0])
    return [signed_messages[msg[1]] for msg in only_used_messages]
