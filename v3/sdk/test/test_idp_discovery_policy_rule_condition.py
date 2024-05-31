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

from openapi_client.models.idp_discovery_policy_rule_condition import IdpDiscoveryPolicyRuleCondition

class TestIdpDiscoveryPolicyRuleCondition(unittest.TestCase):
    """IdpDiscoveryPolicyRuleCondition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdpDiscoveryPolicyRuleCondition:
        """Test IdpDiscoveryPolicyRuleCondition
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdpDiscoveryPolicyRuleCondition`
        """
        model = IdpDiscoveryPolicyRuleCondition()
        if include_optional:
            return IdpDiscoveryPolicyRuleCondition(
                app = openapi_client.models.app_and_instance_policy_rule_condition.AppAndInstancePolicyRuleCondition(
                    exclude = [
                        openapi_client.models.app_and_instance_condition_evaluator_app_or_instance.AppAndInstanceConditionEvaluatorAppOrInstance(
                            id = '', 
                            name = '', 
                            type = 'APP', )
                        ], 
                    include = [
                        openapi_client.models.app_and_instance_condition_evaluator_app_or_instance.AppAndInstanceConditionEvaluatorAppOrInstance(
                            id = '', 
                            name = '', )
                        ], ),
                network = openapi_client.models.policy_network_condition.PolicyNetworkCondition(
                    connection = 'ANYWHERE', 
                    exclude = [
                        ''
                        ], 
                    include = [
                        ''
                        ], ),
                user_identifier = openapi_client.models.user_identifier_policy_rule_condition.UserIdentifierPolicyRuleCondition(
                    attribute = '', 
                    patterns = [
                        openapi_client.models.user_identifier_condition_evaluator_pattern.UserIdentifierConditionEvaluatorPattern(
                            match_type = 'CONTAINS', 
                            value = '', )
                        ], 
                    type = 'ATTRIBUTE', ),
                platform = openapi_client.models.platform_policy_rule_condition.PlatformPolicyRuleCondition(
                    exclude = [
                        openapi_client.models.platform_condition_evaluator_platform.PlatformConditionEvaluatorPlatform(
                            os = openapi_client.models.platform_condition_evaluator_platform_operating_system.PlatformConditionEvaluatorPlatformOperatingSystem(
                                expression = '', 
                                type = 'ANDROID', 
                                version = openapi_client.models.platform_condition_evaluator_platform_operating_system_version.PlatformConditionEvaluatorPlatformOperatingSystemVersion(
                                    match_type = 'EXPRESSION', 
                                    value = '', ), ), 
                            type = 'ANY', )
                        ], 
                    include = [
                        openapi_client.models.platform_condition_evaluator_platform.PlatformConditionEvaluatorPlatform()
                        ], )
            )
        else:
            return IdpDiscoveryPolicyRuleCondition(
        )
        """

    def testIdpDiscoveryPolicyRuleCondition(self):
        """Test IdpDiscoveryPolicyRuleCondition"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()