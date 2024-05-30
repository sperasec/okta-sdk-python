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

from openapi_client.models.o_auth2_scope import OAuth2Scope

class TestOAuth2Scope(unittest.TestCase):
    """OAuth2Scope unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OAuth2Scope:
        """Test OAuth2Scope
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OAuth2Scope`
        """
        model = OAuth2Scope()
        if include_optional:
            return OAuth2Scope(
                consent = 'ADMIN',
                default = True,
                description = '',
                display_name = '',
                id = '',
                metadata_publish = 'ALL_CLIENTS',
                name = '',
                system = True
            )
        else:
            return OAuth2Scope(
        )
        """

    def testOAuth2Scope(self):
        """Test OAuth2Scope"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
