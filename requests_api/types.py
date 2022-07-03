import graphene
import graphene_django

<<<<<<< HEAD:requests/types.py
from requests import models
from shared.utils import get_graphene_enum
from users.types import UserProfileType


BloodTypeEnum = get_graphene_enum(models.Request.BloodType)
=======
from requests_api import models
from users.types import UserType
>>>>>>> origin/MAS-55-nft:requests_api/types.py


class RequestType(graphene_django.DjangoObjectType):
    owner = graphene.Field(UserProfileType)
    blood_type = graphene.Field(BloodTypeEnum)

    class Meta:
        model = models.Request_api
