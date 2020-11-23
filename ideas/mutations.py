import graphene

from ideas.schema import CreateIdea, UpdateIdea, DeleteIdea


class Mutation(graphene.ObjectType):
    create_idea = CreateIdea.Field()
    update_idea = UpdateIdea.Field()
    delete_idea = DeleteIdea.Field()

