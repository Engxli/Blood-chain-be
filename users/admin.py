from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from shared.admin import export_as_csv
from users import models


@admin.register(models.CustomUser)
class CustomUserAdmin(UserAdmin, admin.ModelAdmin[models.CustomUser]):
    pass


@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin[models.UserProfile]):
    list_display = ["user", "crypto_wallet", "phone", "blood_type"]
    list_filter = ["blood_type"]
    actions = (export_as_csv,)
