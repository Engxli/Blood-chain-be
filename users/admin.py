from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users import models


@admin.register(models.CustomUser)
class CustomUserAdmin(UserAdmin, admin.ModelAdmin[models.CustomUser]):
    pass


@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin[models.UserProfile]):
    pass
