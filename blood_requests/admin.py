from django.contrib import admin

from blood_requests import models


@admin.register(models.Request)
class RequestAdmin(admin.ModelAdmin[models.Request]):
    pass
