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

from openapi_client.models.policy_subject import PolicySubject

class TestPolicySubject(unittest.TestCase):
    """PolicySubject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PolicySubject:
        """Test PolicySubject
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PolicySubject`
        """
        model = PolicySubject()
        if include_optional:
            return PolicySubject(
                filter = '',
                format = [
                    ''
                    ],
                match_attribute = '',
                match_type = 'CUSTOM_ATTRIBUTE',
                user_name_template = openapi_client.models.policy_user_name_template.PolicyUserNameTemplate(
                    template = '', )
            )
        else:
            return PolicySubject(
        )
        """

    def testPolicySubject(self):
        """Test PolicySubject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()