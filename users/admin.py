from typing import Any

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from blood_requests.models import Request
from users import models


class RequestInline(admin.TabularInline[Any, Any]):
    model = Request
    extra = 1


@admin.register(models.CustomUser)
class CustomUserAdmin(UserAdmin, admin.ModelAdmin[models.CustomUser]):
    pass


@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin[models.UserProfile]):
    list_display = ["user", "crypto_wallet", "phone", "blood_type"]
    list_filter = ["blood_type"]
    inlines = (RequestInline,)
