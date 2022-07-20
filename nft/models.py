from django.db import models


class AttributeName(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class Attributes(models.Model):
    attr_name = models.ForeignKey(AttributeName, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.attr_name.name + ": " + self.value


class NFT(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()
    attributes = models.ManyToManyField(Attributes, related_name="nft")

    def __str__(self) -> str:
        return self.name
