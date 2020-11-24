import graphene
from django.contrib.auth import get_user_model

from users.types import UserType


class Query(graphene.AbstractType):
    users = graphene.List(UserType)

    def resolve_users(self, info):
        return get_user_model().objects.all()
