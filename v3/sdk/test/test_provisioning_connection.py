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

from openapi_client.models.provisioning_connection import ProvisioningConnection

class TestProvisioningConnection(unittest.TestCase):
    """ProvisioningConnection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProvisioningConnection:
        """Test ProvisioningConnection
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProvisioningConnection`
        """
        model = ProvisioningConnection()
        if include_optional:
            return ProvisioningConnection(
                auth_scheme = 'OAUTH2',
                profile = openapi_client.models.provisioning_connection_profile.ProvisioningConnectionProfile(),
                status = 'DISABLED',
                links = None
            )
        else:
            return ProvisioningConnection(
                auth_scheme = 'OAUTH2',
                status = 'DISABLED',
        )
        """

    def testProvisioningConnection(self):
        """Test ProvisioningConnection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()