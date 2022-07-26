from typing import Any, Optional

from django.contrib import admin
from django.db.models import QuerySet

from donations import models
from shared.utils import mark_donation_as_completed


class SubmitForReviewFilter(admin.SimpleListFilter):
    title: str = "pending approval"
    parameter_name: str = "pending_approval"

    def lookups(self, request: Any, model_admin: Any) -> list[tuple[Any, str]]:
        return [(True, "pending approval"), (False, "approved")]

    def _get_lookup(self) -> Optional[bool]:
        value = self.value()
        return value == "True" if value else None

    def queryset(
        self, request: Any, queryset: QuerySet[models.Donation]
    ) -> Optional[QuerySet[models.Donation]]:
        is_pending = self._get_lookup()
        if is_pending is None:
            return queryset
        status = (
            models.Donation.Status.PENDING
            if is_pending
            else models.Donation.Status.COMPLETE
        )
        return queryset.filter(image__isnull=False, status=status)


@admin.action(description="Mark selected donations as complete")
def mark_as_complete(
    modeladmin: admin.ModelAdmin[models.Donation],
    request: Any,
    queryset: QuerySet[models.Donation],
) -> None:
    for donation in queryset:
        mark_donation_as_completed(donation)


@admin.register(models.Donation)
class DonationAdmin(admin.ModelAdmin[models.Donation]):
    list_display = ("id", "donor", "image")
    list_display_links = ("id", "donor")
    list_filter = (SubmitForReviewFilter,)

    actions = (mark_as_complete,)
