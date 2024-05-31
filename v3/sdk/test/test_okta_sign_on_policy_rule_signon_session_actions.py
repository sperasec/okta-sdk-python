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

from openapi_client.models.okta_sign_on_policy_rule_signon_session_actions import OktaSignOnPolicyRuleSignonSessionActions

class TestOktaSignOnPolicyRuleSignonSessionActions(unittest.TestCase):
    """OktaSignOnPolicyRuleSignonSessionActions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OktaSignOnPolicyRuleSignonSessionActions:
        """Test OktaSignOnPolicyRuleSignonSessionActions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OktaSignOnPolicyRuleSignonSessionActions`
        """
        model = OktaSignOnPolicyRuleSignonSessionActions()
        if include_optional:
            return OktaSignOnPolicyRuleSignonSessionActions(
                max_session_idle_minutes = 56,
                max_session_lifetime_minutes = 56,
                use_persistent_cookie = True
            )
        else:
            return OktaSignOnPolicyRuleSignonSessionActions(
        )
        """

    def testOktaSignOnPolicyRuleSignonSessionActions(self):
        """Test OktaSignOnPolicyRuleSignonSessionActions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()