import graphene
from django.db.models import Q
from graphql_jwt.decorators import login_required

from followers.models import Follow
from ideas.models import Idea
from ideas.types import IdeaType


class Query(graphene.AbstractType):
    my_ideas = graphene.List(IdeaType)
    user_ideas = graphene.List(IdeaType)
    timeline_ideas = graphene.List(IdeaType)

    @login_required
    def resolve_my_ideas(self, info):
        creator = info.context.user
        return Idea.objects.filter(creator=creator).order_by('created_at')

    @login_required
    def resolve_user_ideas(self, info, user_id):
        follower = info.context.user
        isFollowed = Follow.objects.filter(follower=follower, followed=user_id, pending_request=False, approved=True).exists()
        if isFollowed:
            return Idea.objects.filter(Q(creator=user_id) | ~Q(visibility="PRIVATE")).order_by('created_at')
        else:
            return Idea.objects.filter(Q(creator=user_id, visibility="PUBLIC")).order_by('created_at')

    @login_required
    def resolve_timeline_ideas(self, info):
        user = info.context.user
        followedUsers = Follow.objects.filter(follower=user, pending_request=False, approved=True).values_list("followed")
        return Idea.objects.filter(Q(creator=user), Q(creator=followedUsers) | ~Q(visibility="PRIVATE")).order_by('created_at')
