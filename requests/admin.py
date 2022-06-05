from django.contrib import admin

# Register your models here.
from requests import models


to_register = [
    models.Request,
]

admin.site.register(to_register)
