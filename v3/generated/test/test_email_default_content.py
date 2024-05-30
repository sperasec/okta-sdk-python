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

from openapi_client.models.email_default_content import EmailDefaultContent

class TestEmailDefaultContent(unittest.TestCase):
    """EmailDefaultContent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EmailDefaultContent:
        """Test EmailDefaultContent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EmailDefaultContent`
        """
        model = EmailDefaultContent()
        if include_optional:
            return EmailDefaultContent(
                body = '',
                subject = '',
                links = openapi_client.models.email_default_content_all_of__links.EmailDefaultContent_allOf__links()
            )
        else:
            return EmailDefaultContent(
                body = '',
                subject = '',
        )
        """

    def testEmailDefaultContent(self):
        """Test EmailDefaultContent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
