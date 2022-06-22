from django.contrib import admin

from requests import models


@admin.register(models.Request)
# pylint: disable=unsubscriptable-object
class RequestAdmin(admin.ModelAdmin[models.Request]):
    pass
