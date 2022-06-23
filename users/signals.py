# pylint: disable=unused-argument
from typing import TYPE_CHECKING, Any, Type

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import UserProfile


if TYPE_CHECKING:
    from users.models import CustomUser


User = get_user_model()


@receiver(post_save, sender=User)
def create_profile(
    sender: Type["CustomUser"],
    instance: "CustomUser",
    created: bool,
    **kwargs: Any,
) -> None:
    if created:
        UserProfile.objects.create(user=instance)
