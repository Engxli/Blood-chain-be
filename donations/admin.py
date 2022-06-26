from django.contrib import admin

from donations.models import Donation


# Register your models here.
@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin[Donation]):
    pass
