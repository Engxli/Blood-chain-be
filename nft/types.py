import graphene
import graphene_django

from nft import models


class NFTType(graphene_django.DjangoObjectType):
    class Meta:
        model = models.NFT
        exclude = ("image",)

    image_url = graphene.String()

    def resolve_image_url(self, info: graphene.ResolveInfo) -> str:
        return info.context.build_absolute_uri(self.image.url)


class NFTMintType(graphene_django.DjangoObjectType):
    class Meta:
        model = models.NFTMint
