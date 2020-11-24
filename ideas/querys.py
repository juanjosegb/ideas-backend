import graphene
from graphql_jwt.decorators import login_required

from ideas.models import Idea
from ideas.types import IdeaType


class Query(graphene.AbstractType):
    my_ideas = graphene.List(IdeaType)

    @login_required
    def resolve_my_ideas(self, info):
        creator = info.context.user
        return Idea.objects.filter(creator=creator).order_by('created_at')
