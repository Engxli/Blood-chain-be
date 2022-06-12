from django.db import models


class Hospital(models.Model):
    name = models.CharField(max_length=50)
