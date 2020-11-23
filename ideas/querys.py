import graphene

from ideas.models import Idea
from ideas.types import IdeaType


class Query(graphene.AbstractType):
    my_ideas = graphene.List(IdeaType)

    def resolve_my_ideas(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')
        return Idea.objects.filter(creator=user).order_by('created_at')
