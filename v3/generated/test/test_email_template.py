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

from openapi_client.models.email_template import EmailTemplate

class TestEmailTemplate(unittest.TestCase):
    """EmailTemplate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EmailTemplate:
        """Test EmailTemplate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EmailTemplate`
        """
        model = EmailTemplate()
        if include_optional:
            return EmailTemplate(
                name = '',
                embedded = openapi_client.models.email_template__embedded.EmailTemplate__embedded(
                    settings = openapi_client.models.email_settings.EmailSettings(
                        recipients = 'ALL_USERS', ), 
                    customization_count = 56, ),
                links = None
            )
        else:
            return EmailTemplate(
        )
        """

    def testEmailTemplate(self):
        """Test EmailTemplate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
