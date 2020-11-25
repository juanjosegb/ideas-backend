from graphene_django.utils import GraphQLTestCase


class ManagementUserTestCase(GraphQLTestCase):

    def test_create_member_mutation(self):
        graphql = '''
            mutation createUser($username: String, $email: String, $password: String) {
                createUser(username: $username, email: $email, password: $password) {
                    user {
                        id
                        username
                        email
                        password
                    }
                }
            }
        '''

        response = self.query(
            graphql,
            op_name='createUser',
            variables={'username': 'username', 'email': 'email', 'password': 'password'},
        )
        self.assertResponseNoErrors(response)

