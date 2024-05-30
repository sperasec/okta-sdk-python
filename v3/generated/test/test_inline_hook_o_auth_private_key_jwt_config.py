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

from openapi_client.models.inline_hook_o_auth_private_key_jwt_config import InlineHookOAuthPrivateKeyJwtConfig

class TestInlineHookOAuthPrivateKeyJwtConfig(unittest.TestCase):
    """InlineHookOAuthPrivateKeyJwtConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InlineHookOAuthPrivateKeyJwtConfig:
        """Test InlineHookOAuthPrivateKeyJwtConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InlineHookOAuthPrivateKeyJwtConfig`
        """
        model = InlineHookOAuthPrivateKeyJwtConfig()
        if include_optional:
            return InlineHookOAuthPrivateKeyJwtConfig(
                hook_key_id = '',
                auth_type = '',
                client_id = '',
                scope = '',
                token_url = '',
                auth_scheme = openapi_client.models.inline_hook_channel_config_auth_scheme.InlineHookChannelConfigAuthScheme(
                    key = '', 
                    type = '', 
                    value = '', ),
                headers = [
                    openapi_client.models.inline_hook_channel_config_headers.InlineHookChannelConfigHeaders(
                        key = '', 
                        value = '', )
                    ],
                method = '',
                uri = ''
            )
        else:
            return InlineHookOAuthPrivateKeyJwtConfig(
        )
        """

    def testInlineHookOAuthPrivateKeyJwtConfig(self):
        """Test InlineHookOAuthPrivateKeyJwtConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
