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

from openapi_client.models.email_server_request import EmailServerRequest

class TestEmailServerRequest(unittest.TestCase):
    """EmailServerRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EmailServerRequest:
        """Test EmailServerRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EmailServerRequest`
        """
        model = EmailServerRequest()
        if include_optional:
            return EmailServerRequest(
                alias = '',
                enabled = True,
                host = '',
                port = 56,
                username = '',
                password = ''
            )
        else:
            return EmailServerRequest(
        )
        """

    def testEmailServerRequest(self):
        """Test EmailServerRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()