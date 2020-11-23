import graphene

from ideas.models import Idea
from ideas.types import IdeaType


class CreateIdea(graphene.Mutation):
    idea = graphene.Field(IdeaType)

    class Arguments:
        text = graphene.String(required=True)
        visibility = graphene.String(required=True)

    def mutate(self, info, text, visibility):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')
        idea = Idea(text=text, visibility=visibility, creator=user)
        idea.save()

        return CreateIdea(idea=idea)


class UpdateIdea(graphene.Mutation):
    idea = graphene.Field(IdeaType)

    class Arguments:
        pk = graphene.ID()
        text = graphene.String(required=True)
        visibility = graphene.String(required=True)

    def mutate(self, info, pk, text, visibility):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')
        idea = Idea.objects.get(pk=pk)
        idea.text = text
        idea.visibility = visibility
        idea.save()

        return UpdateIdea(idea=idea)


class DeleteIdea(graphene.Mutation):
    idea = graphene.Field(IdeaType)

    class Arguments:
        pk = graphene.ID()

    def mutate(self, info, pk):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')
        idea = Idea.objects.get(pk=pk)
        idea.delete()

        return True
