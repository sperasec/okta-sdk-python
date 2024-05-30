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

from openapi_client.models.profile_enrollment_policy_rule_action import ProfileEnrollmentPolicyRuleAction

class TestProfileEnrollmentPolicyRuleAction(unittest.TestCase):
    """ProfileEnrollmentPolicyRuleAction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProfileEnrollmentPolicyRuleAction:
        """Test ProfileEnrollmentPolicyRuleAction
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProfileEnrollmentPolicyRuleAction`
        """
        model = ProfileEnrollmentPolicyRuleAction()
        if include_optional:
            return ProfileEnrollmentPolicyRuleAction(
                access = '',
                activation_requirements = openapi_client.models.profile_enrollment_policy_rule_activation_requirement.ProfileEnrollmentPolicyRuleActivationRequirement(
                    email_verification = True, ),
                pre_registration_inline_hooks = [
                    openapi_client.models.pre_registration_inline_hook.PreRegistrationInlineHook(
                        inline_hook_id = '', )
                    ],
                profile_attributes = [
                    openapi_client.models.profile_enrollment_policy_rule_profile_attribute.ProfileEnrollmentPolicyRuleProfileAttribute(
                        label = '', 
                        name = '', 
                        required = True, )
                    ],
                progressive_profiling_action = 'ENABLED',
                target_group_ids = [
                    ''
                    ],
                unknown_user_action = 'DENY'
            )
        else:
            return ProfileEnrollmentPolicyRuleAction(
        )
        """

    def testProfileEnrollmentPolicyRuleAction(self):
        """Test ProfileEnrollmentPolicyRuleAction"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
