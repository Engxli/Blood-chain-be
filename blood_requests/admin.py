from typing import Any

from django.contrib import admin
from django.db.models import QuerySet

from blood_requests import models
from donations.models import Donation


class DonationInline(admin.TabularInline[Any, Any]):
    model = Donation
    extra = 1


@admin.action(description="Mark selected requests as complete")
def mark_as_complete(
    modeladmin: admin.ModelAdmin[models.Request],
    request: Any,
    queryset: QuerySet[models.Request],
) -> None:
    queryset.update(status=2)


@admin.register(models.Request)
class RequestAdmin(admin.ModelAdmin[models.Request]):
    list_display = ["owner", "blood_type", "severity", "status"]
    list_filter = ["blood_type", "severity", "status"]
    actions = [mark_as_complete]
    inlines = (DonationInline,)
