from django.contrib import admin

from users.models import CustomUser, UserProfile


admin.site.register([CustomUser, UserProfile])
