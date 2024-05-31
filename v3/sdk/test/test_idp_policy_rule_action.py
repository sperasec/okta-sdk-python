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

from openapi_client.models.idp_policy_rule_action import IdpPolicyRuleAction

class TestIdpPolicyRuleAction(unittest.TestCase):
    """IdpPolicyRuleAction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdpPolicyRuleAction:
        """Test IdpPolicyRuleAction
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdpPolicyRuleAction`
        """
        model = IdpPolicyRuleAction()
        if include_optional:
            return IdpPolicyRuleAction(
                idp = openapi_client.models.idp_policy_rule_action_idp.IdpPolicyRuleAction_idp(
                    providers = [
                        openapi_client.models.idp_policy_rule_action_provider.IdpPolicyRuleActionProvider(
                            id = '', 
                            name = '', 
                            type = 'AgentlessDSSO', )
                        ], 
                    idp_selection_type = 'DYNAMIC', 
                    match_criteria = [
                        openapi_client.models.idp_policy_rule_action_match_criteria.IdpPolicyRuleActionMatchCriteria(
                            provider_expression = '', 
                            property_name = '', )
                        ], )
            )
        else:
            return IdpPolicyRuleAction(
        )
        """

    def testIdpPolicyRuleAction(self):
        """Test IdpPolicyRuleAction"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()