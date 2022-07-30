from django.contrib import admin

from nft import models


class AttributesInline(
    admin.TabularInline[models.Attributes, models.AttributeName]
):
    model = models.Attributes
    extra = 1


@admin.register(models.AttributeName)
class NFTAttrNameAdmin(admin.ModelAdmin[models.AttributeName]):
    list_display = ["name"]
    list_filter = ("name",)
    inlines = (AttributesInline,)


@admin.register(models.Attributes)
class NFTAttrAdmin(admin.ModelAdmin[models.Attributes]):
    list_display = ["attr_name", "value"]
    list_filter = ("attr_name",)


@admin.register(models.NFT)
class NFTAdmin(admin.ModelAdmin[models.NFT]):
    list_display = ("id", "name", "image")
    list_filter = ("attributes__attr_name",)
