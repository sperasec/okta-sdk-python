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

from openapi_client.models.device_policy_rule_condition import DevicePolicyRuleCondition

class TestDevicePolicyRuleCondition(unittest.TestCase):
    """DevicePolicyRuleCondition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DevicePolicyRuleCondition:
        """Test DevicePolicyRuleCondition
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DevicePolicyRuleCondition`
        """
        model = DevicePolicyRuleCondition()
        if include_optional:
            return DevicePolicyRuleCondition(
                migrated = True,
                platform = openapi_client.models.device_policy_rule_condition_platform.DevicePolicyRuleConditionPlatform(
                    supported_mdm_frameworks = [
                        'AFW'
                        ], 
                    types = [
                        'ANDROID'
                        ], ),
                rooted = True,
                trust_level = 'ANY'
            )
        else:
            return DevicePolicyRuleCondition(
        )
        """

    def testDevicePolicyRuleCondition(self):
        """Test DevicePolicyRuleCondition"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()