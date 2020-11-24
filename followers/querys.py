import graphene
from graphql_jwt.decorators import login_required

from followers.models import Follow
from followers.types import FollowType


class Query(graphene.AbstractType):
    my_followers = graphene.List(FollowType)
    my_followed = graphene.List(FollowType)
    my_follower_requests = graphene.List(FollowType)

    @login_required
    def resolve_my_followers(self, info):
        user = info.context.user
        return Follow.objects.filter(followed=user, pending_request=False, approved=True)

    @login_required
    def resolve_my_followed(self, info):
        user = info.context.user
        return Follow.objects.filter(follower=user, pending_request=False, approved=True)

    @login_required
    def resolve_my_follower_requests(self, info):
        user = info.context.user
        return Follow.objects.filter(followed=user, pending_request=True)
