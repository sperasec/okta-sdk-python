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

from openapi_client.api.attack_protection_api import AttackProtectionApi


class TestAttackProtectionApi(unittest.TestCase):
    """AttackProtectionApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AttackProtectionApi()

    def tearDown(self) -> None:
        pass

    def test_get_user_lockout_settings(self) -> None:
        """Test case for get_user_lockout_settings

        Retrieve the User Lockout Settings
        """
        pass

    def test_replace_user_lockout_settings(self) -> None:
        """Test case for replace_user_lockout_settings

        Replace the User Lockout Settings
        """
        pass


if __name__ == '__main__':
    unittest.main()
