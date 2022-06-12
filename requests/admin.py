from django.contrib import admin

from requests import models


@admin.register(models.Request)
class AuthorAdmin(admin.ModelAdmin):
    pass
