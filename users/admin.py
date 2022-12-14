from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from graphql_jwt.refresh_token.models import RefreshToken

from blood_requests.models import Request
from shared.admin import export_as_csv
from users import models


admin.site.unregister(Group)
admin.site.unregister(RefreshToken)


class RequestInline(admin.TabularInline[Request, models.UserProfile]):
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
    actions = (export_as_csv,)
