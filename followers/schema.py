import graphene
from graphql_jwt.decorators import login_required

from followers.models import Follow
from followers.types import FollowType


class CreateFollower(graphene.Mutation):
    follow = graphene.Field(FollowType)

    class Arguments:
        user_id = graphene.ID()

    @login_required
    def mutate(self, info, user_id):
        follower = info.context.user
        follow = Follow(followed_id=user_id, follower=follower)
        follow.save()

        return CreateFollower(follow=follow)


class ApproveFollower(graphene.Mutation):
    follow = graphene.Field(FollowType)

    class Arguments:
        pk = graphene.ID()

    @login_required
    def mutate(self, info, pk):
        follow = Follow.objects.get(pk=pk)
        follow.approved = True
        follow.pending_request = False

        return ApproveFollower(follow=follow)


class DenyFollower(graphene.Mutation):
    follow = graphene.Field(FollowType)

    class Arguments:
        pk = graphene.ID()

    @login_required
    def mutate(self, info, pk):
        follow = Follow.objects.get(pk=pk)
        follow.approved = False
        follow.pending_request = False

        return ApproveFollower(follow=follow)


class DeleteFollow(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        pk = graphene.ID()

    @login_required
    def mutate(self, info, pk):
        try:
            follow = Follow.objects.get(pk=pk)
            follow.delete()
        except Follow.DoesNotExist:
            return DeleteFollow(ok=False)
        return DeleteFollow(ok=True)

