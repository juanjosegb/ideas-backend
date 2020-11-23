from graphene_django import DjangoObjectType

from ideas.models import Idea


class IdeaType(DjangoObjectType):
    class Meta:
        model = Idea
