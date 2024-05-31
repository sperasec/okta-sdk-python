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

from openapi_client.models.log_authentication_context import LogAuthenticationContext

class TestLogAuthenticationContext(unittest.TestCase):
    """LogAuthenticationContext unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LogAuthenticationContext:
        """Test LogAuthenticationContext
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LogAuthenticationContext`
        """
        model = LogAuthenticationContext()
        if include_optional:
            return LogAuthenticationContext(
                authentication_provider = 'ACTIVE_DIRECTORY',
                authentication_step = 56,
                credential_provider = 'DUO',
                credential_type = 'ASSERTION',
                external_session_id = '',
                interface = '',
                issuer = openapi_client.models.log_issuer.LogIssuer(
                    id = '', 
                    type = '', )
            )
        else:
            return LogAuthenticationContext(
        )
        """

    def testLogAuthenticationContext(self):
        """Test LogAuthenticationContext"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()