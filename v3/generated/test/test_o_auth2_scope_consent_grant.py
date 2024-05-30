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

from openapi_client.models.o_auth2_scope_consent_grant import OAuth2ScopeConsentGrant

class TestOAuth2ScopeConsentGrant(unittest.TestCase):
    """OAuth2ScopeConsentGrant unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OAuth2ScopeConsentGrant:
        """Test OAuth2ScopeConsentGrant
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OAuth2ScopeConsentGrant`
        """
        model = OAuth2ScopeConsentGrant()
        if include_optional:
            return OAuth2ScopeConsentGrant(
                client_id = '0oafxqCAJWWGELFTYASJ',
                created = '2023-06-28T16:40:10Z',
                created_by = openapi_client.models.o_auth2_actor.OAuth2Actor(
                    id = '00uu3u0ujW1P6AfZC1d7', 
                    type = 'User', ),
                id = 'oagsebt2ltaSlR6t81d6',
                issuer = 'https://my_test_okta_org.oktapreview.com',
                last_updated = '2023-06-28T16:40:10Z',
                scope_id = 'okta.users.read',
                source = 'ADMIN',
                status = 'ACTIVE',
                user_id = '',
                embedded = openapi_client.models.o_auth2_scope_consent_grant__embedded.OAuth2ScopeConsentGrant__embedded(
                    scope = openapi_client.models.o_auth2_scope_consent_grant__embedded_scope.OAuth2ScopeConsentGrant__embedded_scope(
                        id = 'okta.users.read', ), ),
                links = None
            )
        else:
            return OAuth2ScopeConsentGrant(
                issuer = 'https://my_test_okta_org.oktapreview.com',
                scope_id = 'okta.users.read',
        )
        """

    def testOAuth2ScopeConsentGrant(self):
        """Test OAuth2ScopeConsentGrant"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
