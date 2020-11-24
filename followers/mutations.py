import graphene

from followers.schema import CreateFollower, DeleteFollow, ApproveFollower, DenyFollower


class Mutation(graphene.ObjectType):
    create_follower = CreateFollower.Field()
    delete_follow = DeleteFollow.Field()
    approve_follower = ApproveFollower.Field()
    deny_follower = DenyFollower.Field()

