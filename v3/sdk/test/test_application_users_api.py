# coding: utf-8

"""
    Okta Admin Management

    Allows customers to easily access the Okta Management APIs

    The version of the OpenAPI document: 5.1.0
    Contact: devex-public@okta.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.application_users_api import ApplicationUsersApi


class TestApplicationUsersApi(unittest.TestCase):
    """ApplicationUsersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ApplicationUsersApi()

    def tearDown(self) -> None:
        pass

    def test_assign_user_to_application(self) -> None:
        """Test case for assign_user_to_application

        Assign a User
        """
        pass

    def test_get_application_user(self) -> None:
        """Test case for get_application_user

        Retrieve an assigned User
        """
        pass

    def test_list_application_users(self) -> None:
        """Test case for list_application_users

        List all assigned Users
        """
        pass

    def test_unassign_user_from_application(self) -> None:
        """Test case for unassign_user_from_application

        Unassign an App User
        """
        pass

    def test_update_application_user(self) -> None:
        """Test case for update_application_user

        Update an App Profile for an assigned User
        """
        pass


if __name__ == '__main__':
    unittest.main()