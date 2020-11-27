import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField

from users.types import UserType


class Query(graphene.AbstractType):
    user = relay.Node.Field(UserType)
    all_users = DjangoFilterConnectionField(UserType)

