from django.contrib import admin

from nft import models


@admin.register(models.AttributeName)
class NFTArrtNameAdmin(admin.ModelAdmin[models.AttributeName]):
    pass


@admin.register(models.Attributes)
class NFTArrtAdmin(admin.ModelAdmin[models.Attributes]):
    pass


@admin.register(models.NFT)
class NFTAdmin(admin.ModelAdmin[models.NFT]):
    pass
