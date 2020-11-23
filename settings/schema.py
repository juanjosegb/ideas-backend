import graphene
import graphql_jwt

import ideas.mutations
import ideas.querys
import users.mutations
import users.querys


class Query(users.querys.Query, ideas.querys.Query, graphene.ObjectType):
    pass


class Mutation(users.mutations.Mutation, ideas.mutations.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

