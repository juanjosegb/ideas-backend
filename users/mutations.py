import graphene

from users.schema import CreateUser, ChangePassword


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    change_password = ChangePassword.Field()