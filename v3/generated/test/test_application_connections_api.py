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

from openapi_client.api.application_connections_api import ApplicationConnectionsApi


class TestApplicationConnectionsApi(unittest.TestCase):
    """ApplicationConnectionsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ApplicationConnectionsApi()

    def tearDown(self) -> None:
        pass

    def test_activate_default_provisioning_connection_for_application(self) -> None:
        """Test case for activate_default_provisioning_connection_for_application

        Activate the default Provisioning Connection
        """
        pass

    def test_deactivate_default_provisioning_connection_for_application(self) -> None:
        """Test case for deactivate_default_provisioning_connection_for_application

        Deactivate the default Provisioning Connection
        """
        pass

    def test_get_default_provisioning_connection_for_application(self) -> None:
        """Test case for get_default_provisioning_connection_for_application

        Retrieve the default Provisioning Connection
        """
        pass

    def test_update_default_provisioning_connection_for_application(self) -> None:
        """Test case for update_default_provisioning_connection_for_application

        Update the default Provisioning Connection
        """
        pass


if __name__ == '__main__':
    unittest.main()
