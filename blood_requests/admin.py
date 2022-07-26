from django.contrib import admin

from blood_requests import models


@admin.register(models.Request)
class RequestAdmin(admin.ModelAdmin[models.Request]):
    list_display = ["owner", "blood_type", "severity"]
    list_filter = ["blood_type", "severity"]
