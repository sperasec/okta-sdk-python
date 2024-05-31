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

from openapi_client.models.o_auth2_scope_consent_grant_embedded import OAuth2ScopeConsentGrantEmbedded

class TestOAuth2ScopeConsentGrantEmbedded(unittest.TestCase):
    """OAuth2ScopeConsentGrantEmbedded unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OAuth2ScopeConsentGrantEmbedded:
        """Test OAuth2ScopeConsentGrantEmbedded
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OAuth2ScopeConsentGrantEmbedded`
        """
        model = OAuth2ScopeConsentGrantEmbedded()
        if include_optional:
            return OAuth2ScopeConsentGrantEmbedded(
                scope = openapi_client.models.o_auth2_scope_consent_grant__embedded_scope.OAuth2ScopeConsentGrant__embedded_scope(
                    id = 'okta.users.read', )
            )
        else:
            return OAuth2ScopeConsentGrantEmbedded(
        )
        """

    def testOAuth2ScopeConsentGrantEmbedded(self):
        """Test OAuth2ScopeConsentGrantEmbedded"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()