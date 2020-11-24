import graphene
from graphql_jwt.decorators import login_required

from ideas.models import Idea
from ideas.types import IdeaType


class CreateIdea(graphene.Mutation):
    idea = graphene.Field(IdeaType)

    class Arguments:
        text = graphene.String(required=True)
        visibility = graphene.String(required=True)

    @login_required
    def mutate(self, info, text, visibility):
        creator = info.context.user
        idea = Idea(text=text, visibility=visibility, creator=creator)
        idea.save()

        return CreateIdea(idea=idea)


class UpdateIdea(graphene.Mutation):
    idea = graphene.Field(IdeaType)

    class Arguments:
        pk = graphene.ID()
        text = graphene.String(required=True)
        visibility = graphene.String(required=True)

    @login_required
    def mutate(self, info, pk, text, visibility):
        idea = Idea.objects.get(pk=pk)
        idea.text = text
        idea.visibility = visibility
        idea.save()

        return UpdateIdea(idea=idea)


class DeleteIdea(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        pk = graphene.ID()

    @login_required
    def mutate(self, info, pk):
        try:
            idea = Idea.objects.get(pk=pk)
            idea.delete()
        except Idea.DoesNotExist:
            return DeleteIdea(ok=False)
        return DeleteIdea(ok=True)
