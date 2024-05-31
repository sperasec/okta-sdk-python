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

from openapi_client.models.application_layout import ApplicationLayout

class TestApplicationLayout(unittest.TestCase):
    """ApplicationLayout unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApplicationLayout:
        """Test ApplicationLayout
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApplicationLayout`
        """
        model = ApplicationLayout()
        if include_optional:
            return ApplicationLayout(
                elements = [
                    {
                        'key' : null
                        }
                    ],
                label = '',
                options = {
                    'key' : null
                    },
                rule = openapi_client.models.application_layout_rule.ApplicationLayout_rule(
                    effect = '', 
                    condition = openapi_client.models.application_layout_rule_condition.ApplicationLayoutRuleCondition(
                        schema = {
                            'key' : null
                            }, 
                        scope = '', ), ),
                scope = '',
                type = ''
            )
        else:
            return ApplicationLayout(
        )
        """

    def testApplicationLayout(self):
        """Test ApplicationLayout"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()