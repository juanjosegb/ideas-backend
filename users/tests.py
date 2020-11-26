import json
from unittest import TestCase
import graphene

from users import mutations


class ManagementUserTest(TestCase):

    def setUp(self):
        super().setUp()
        self.mutation = """
            mutation {
                createUser(username: username_test, email: email_test, password: password_test) {
                    user {
                        id
                        username
                        email
                        password
                    }
                }
            }
        """

    def test_create_member_mutation(self):
        schema = graphene.Schema(mutation=mutations.CreateUser)
        result = schema.execute(self.mutation)
        self.assertIsNone(result.errors)