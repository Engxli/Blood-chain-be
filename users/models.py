from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="profile",
        unique=True,
    )
    crypto_wallet = models.CharField(null=True, blank=True, max_length=35)
    phone = models.CharField(max_length=8, null=True, blank=True)

    def __str__(self) -> str:
        return self.user.email

    class Meta:
        verbose_name = "Profile"
