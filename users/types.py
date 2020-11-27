from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
from graphene import relay


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()
        filter_fields = {
            'username': ['icontains']
        }
        interfaces = (relay.Node,)
