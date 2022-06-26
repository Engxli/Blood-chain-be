from django.contrib import admin

from donations import models


@admin.register(models.Donation)
class DonationAdmin(admin.ModelAdmin[models.Donation]):
    pass
