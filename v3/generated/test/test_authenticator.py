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

from openapi_client.models.authenticator import Authenticator

class TestAuthenticator(unittest.TestCase):
    """Authenticator unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Authenticator:
        """Test Authenticator
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Authenticator`
        """
        model = Authenticator()
        if include_optional:
            return Authenticator(
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '',
                key = '',
                last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '',
                provider = openapi_client.models.authenticator_provider.AuthenticatorProvider(
                    configuration = openapi_client.models.authenticator_provider_configuration.AuthenticatorProviderConfiguration(
                        auth_port = 56, 
                        host_name = '', 
                        instance_id = '', 
                        shared_secret = '', 
                        user_name_template = openapi_client.models.authenticator_provider_configuration_user_name_template.AuthenticatorProviderConfigurationUserNameTemplate(
                            template = '', ), ), 
                    type = '', ),
                settings = openapi_client.models.authenticator_settings.AuthenticatorSettings(
                    allowed_for = 'any', 
                    app_instance_id = '', 
                    channel_binding = openapi_client.models.channel_binding.ChannelBinding(
                        required = 'ALWAYS', 
                        style = '', ), 
                    compliance = openapi_client.models.compliance.Compliance(
                        fips = 'OPTIONAL', ), 
                    token_lifetime_in_minutes = 56, 
                    user_verification = 'DISCOURAGED', ),
                status = 'ACTIVE',
                type = 'app',
                links = None
            )
        else:
            return Authenticator(
        )
        """

    def testAuthenticator(self):
        """Test Authenticator"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
