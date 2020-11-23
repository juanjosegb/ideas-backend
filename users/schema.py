import graphene

from django.contrib.auth import get_user_model
from users.types import UserType


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = get_user_model()(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)


class ChangePassword(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        password = graphene.String(required=True)
        confirm = graphene.String(required=True)

    def mutate(self, info, password, confirm):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')
        if password != confirm:
            raise Exception('Password confirmation does not match!')
        user = get_user_model()
        user.set_password(password)
        user.save()

        return ChangePassword(user=user)

