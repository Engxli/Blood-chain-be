from django.contrib import admin

from nft import models
from shared.admin import export_as_csv


@admin.register(models.Attributes)
class NFTAttrAdmin(admin.ModelAdmin[models.Attributes]):
    list_display = ["name", "value"]
    list_filter = ("name",)


@admin.register(models.NFT)
class NFTAdmin(admin.ModelAdmin[models.NFT]):
    list_display = ("id", "name", "image")
    list_filter = ("attributes__name",)
    actions = (export_as_csv,)
