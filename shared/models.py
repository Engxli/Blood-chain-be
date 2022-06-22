from django.db import models


class TimestampMixin(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    modifiedAt = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
