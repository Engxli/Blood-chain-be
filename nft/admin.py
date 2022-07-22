from django.contrib import admin

from nft import models


@admin.register(models.AttributeName)
class NFTAttrNameAdmin(admin.ModelAdmin[models.AttributeName]):
    pass


@admin.register(models.Attributes)
class NFTAttrAdmin(admin.ModelAdmin[models.Attributes]):
    pass


@admin.register(models.NFT)
class NFTAdmin(admin.ModelAdmin[models.NFT]):
    list_display = ("id", "name", "image")
    list_filter = ("attributes__attr_name",)
