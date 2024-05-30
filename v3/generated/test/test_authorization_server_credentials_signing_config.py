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

from openapi_client.models.authorization_server_credentials_signing_config import AuthorizationServerCredentialsSigningConfig

class TestAuthorizationServerCredentialsSigningConfig(unittest.TestCase):
    """AuthorizationServerCredentialsSigningConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AuthorizationServerCredentialsSigningConfig:
        """Test AuthorizationServerCredentialsSigningConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AuthorizationServerCredentialsSigningConfig`
        """
        model = AuthorizationServerCredentialsSigningConfig()
        if include_optional:
            return AuthorizationServerCredentialsSigningConfig(
                kid = '',
                last_rotated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                next_rotation = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                rotation_mode = 'AUTO',
                use = 'sig'
            )
        else:
            return AuthorizationServerCredentialsSigningConfig(
        )
        """

    def testAuthorizationServerCredentialsSigningConfig(self):
        """Test AuthorizationServerCredentialsSigningConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
