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

from openapi_client.api.user_type_api import UserTypeApi


class TestUserTypeApi(unittest.TestCase):
    """UserTypeApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UserTypeApi()

    def tearDown(self) -> None:
        pass

    def test_create_user_type(self) -> None:
        """Test case for create_user_type

        Create a User Type
        """
        pass

    def test_delete_user_type(self) -> None:
        """Test case for delete_user_type

        Delete a User Type
        """
        pass

    def test_get_user_type(self) -> None:
        """Test case for get_user_type

        Retrieve a User Type
        """
        pass

    def test_list_user_types(self) -> None:
        """Test case for list_user_types

        List all User Types
        """
        pass

    def test_replace_user_type(self) -> None:
        """Test case for replace_user_type

        Replace a User Type
        """
        pass

    def test_update_user_type(self) -> None:
        """Test case for update_user_type

        Update a User Type
        """
        pass


if __name__ == '__main__':
    unittest.main()