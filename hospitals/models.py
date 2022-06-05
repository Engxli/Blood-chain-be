from urllib import request
from django.db import models
from requests import Request

class Hospital(models.Model):
    name = models.CharField(max_length=50)
    request = models.ForeignKey(Request, related_name='hospital')
