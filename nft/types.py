import graphene_django

from nft import models


class NFTMintType(graphene_django.DjangoObjectType):
    class Meta:
        model = models.NFTMint
