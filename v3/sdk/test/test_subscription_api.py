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

from openapi_client.api.subscription_api import SubscriptionApi


class TestSubscriptionApi(unittest.TestCase):
    """SubscriptionApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SubscriptionApi()

    def tearDown(self) -> None:
        pass

    def test_get_subscriptions_notification_type_role(self) -> None:
        """Test case for get_subscriptions_notification_type_role

        Retrieve a Subscription for a Role
        """
        pass

    def test_get_subscriptions_notification_type_user(self) -> None:
        """Test case for get_subscriptions_notification_type_user

        Retrieve a Subscription for a User
        """
        pass

    def test_list_subscriptions_role(self) -> None:
        """Test case for list_subscriptions_role

        List all Subscriptions for a Role
        """
        pass

    def test_list_subscriptions_user(self) -> None:
        """Test case for list_subscriptions_user

        List all Subscriptions for a User
        """
        pass

    def test_subscribe_by_notification_type_role(self) -> None:
        """Test case for subscribe_by_notification_type_role

        Subscribe a Role to a Specific Notification Type
        """
        pass

    def test_subscribe_by_notification_type_user(self) -> None:
        """Test case for subscribe_by_notification_type_user

        Subscribe a User to a Specific Notification Type
        """
        pass

    def test_unsubscribe_by_notification_type_role(self) -> None:
        """Test case for unsubscribe_by_notification_type_role

        Unsubscribe a Role from a Specific Notification Type
        """
        pass

    def test_unsubscribe_by_notification_type_user(self) -> None:
        """Test case for unsubscribe_by_notification_type_user

        Unsubscribe a User from a Specific Notification Type
        """
        pass


if __name__ == '__main__':
    unittest.main()