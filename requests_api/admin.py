from django.contrib import admin

from requests_api import models


@admin.register(models.Request)
class RequestAdmin(admin.ModelAdmin[models.Request]):
    pass
