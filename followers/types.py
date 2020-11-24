from graphene_django import DjangoObjectType

from followers.models import Follow


class FollowType(DjangoObjectType):
    class Meta:
        model = Follow
