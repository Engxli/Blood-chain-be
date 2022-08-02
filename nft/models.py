from django.db import models

from users.models import UserProfile


class Attributes(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name + ": " + self.value

    class Meta:
        verbose_name_plural = "Attributes"


class NFT(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()
    attributes = models.ManyToManyField(Attributes, related_name="nft")

    def __str__(self) -> str:
        return self.name


class NFTMint(models.Model):
    ts = models.CharField(max_length=255)
    signed_message = models.CharField(max_length=255)
    signature_v = models.IntegerField()
    signature_r = models.CharField(max_length=255)
    signature_s = models.CharField(max_length=255)
    used = models.BooleanField(default=False)
    user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="nft_mint"
    )
