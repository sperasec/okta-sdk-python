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

from openapi_client.models.o_auth2_scopes_mediation_policy_rule_condition import OAuth2ScopesMediationPolicyRuleCondition

class TestOAuth2ScopesMediationPolicyRuleCondition(unittest.TestCase):
    """OAuth2ScopesMediationPolicyRuleCondition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OAuth2ScopesMediationPolicyRuleCondition:
        """Test OAuth2ScopesMediationPolicyRuleCondition
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OAuth2ScopesMediationPolicyRuleCondition`
        """
        model = OAuth2ScopesMediationPolicyRuleCondition()
        if include_optional:
            return OAuth2ScopesMediationPolicyRuleCondition(
                include = [
                    ''
                    ]
            )
        else:
            return OAuth2ScopesMediationPolicyRuleCondition(
        )
        """

    def testOAuth2ScopesMediationPolicyRuleCondition(self):
        """Test OAuth2ScopesMediationPolicyRuleCondition"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()