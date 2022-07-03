from django.contrib import admin

from requests_api import models


@admin.register(models.Request_api)
# pylint: disable=unsubscriptable-object
class RequestAdmin(admin.ModelAdmin[models.Request_api]):
    pass
