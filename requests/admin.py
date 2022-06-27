from django.contrib import admin

from requests import models


@admin.register(models.Request)
class RequestAdmin(admin.ModelAdmin[models.Request]):
    pass
