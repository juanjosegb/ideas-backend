import graphene
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from users.types import UserType


class Query(graphene.AbstractType):
    find_users = graphene.List(UserType)

    @login_required
    def resolve_find_users(self, info, text):
        return get_user_model().objects.filter(username__contains=text)

