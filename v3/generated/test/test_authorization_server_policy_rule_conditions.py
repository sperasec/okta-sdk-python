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

from openapi_client.models.authorization_server_policy_rule_conditions import AuthorizationServerPolicyRuleConditions

class TestAuthorizationServerPolicyRuleConditions(unittest.TestCase):
    """AuthorizationServerPolicyRuleConditions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AuthorizationServerPolicyRuleConditions:
        """Test AuthorizationServerPolicyRuleConditions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AuthorizationServerPolicyRuleConditions`
        """
        model = AuthorizationServerPolicyRuleConditions()
        if include_optional:
            return AuthorizationServerPolicyRuleConditions(
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
                apps = openapi_client.models.app_instance_policy_rule_condition.AppInstancePolicyRuleCondition(
                    exclude = [
                        ''
                        ], 
                    include = [
                        ''
                        ], ),
                auth_context = openapi_client.models.policy_rule_auth_context_condition.PolicyRuleAuthContextCondition(
                    auth_type = 'ANY', ),
                auth_provider = openapi_client.models.password_policy_authentication_provider_condition.PasswordPolicyAuthenticationProviderCondition(
                    include = [
                        ''
                        ], 
                    provider = 'ACTIVE_DIRECTORY', ),
                before_scheduled_action = openapi_client.models.before_scheduled_action_policy_rule_condition.BeforeScheduledActionPolicyRuleCondition(
                    duration = openapi_client.models.duration.Duration(
                        number = 56, 
                        unit = '', ), 
                    lifecycle_action = openapi_client.models.scheduled_user_lifecycle_action.ScheduledUserLifecycleAction(
                        status = 'ACTIVATING', ), ),
                clients = openapi_client.models.client_policy_condition.ClientPolicyCondition(
                    include = [
                        ''
                        ], ),
                context = None,
                device = openapi_client.models.device_policy_rule_condition.DevicePolicyRuleCondition(
                    migrated = True, 
                    platform = openapi_client.models.device_policy_rule_condition_platform.DevicePolicyRuleConditionPlatform(
                        supported_mdm_frameworks = [
                            'AFW'
                            ], 
                        types = [
                            'ANDROID'
                            ], ), 
                    rooted = True, 
                    trust_level = 'ANY', ),
                grant_types = openapi_client.models.grant_type_policy_rule_condition.GrantTypePolicyRuleCondition(
                    include = [
                        ''
                        ], ),
                groups = openapi_client.models.group_policy_rule_condition.GroupPolicyRuleCondition(
                    exclude = [
                        ''
                        ], 
                    include = [
                        ''
                        ], ),
                identity_provider = openapi_client.models.identity_provider_policy_rule_condition.IdentityProviderPolicyRuleCondition(
                    idp_ids = [
                        ''
                        ], 
                    provider = 'ANY', ),
                mdm_enrollment = openapi_client.models.mdm_enrollment_policy_rule_condition.MDMEnrollmentPolicyRuleCondition(
                    block_non_safe_android = True, 
                    enrollment = 'ANY_OR_NONE', ),
                network = openapi_client.models.policy_network_condition.PolicyNetworkCondition(
                    connection = 'ANYWHERE', 
                    exclude = [
                        ''
                        ], 
                    include = [
                        ''
                        ], ),
                people = openapi_client.models.policy_people_condition.PolicyPeopleCondition(
                    groups = openapi_client.models.group_condition.GroupCondition(
                        exclude = [
                            ''
                            ], 
                        include = [
                            ''
                            ], ), 
                    users = openapi_client.models.user_condition.UserCondition(), ),
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
                        ], ),
                risk = openapi_client.models.risk_policy_rule_condition.RiskPolicyRuleCondition(
                    behaviors = [
                        ''
                        ], ),
                risk_score = openapi_client.models.risk_score_policy_rule_condition.RiskScorePolicyRuleCondition(
                    level = '', ),
                scopes = openapi_client.models.o_auth2_scopes_mediation_policy_rule_condition.OAuth2ScopesMediationPolicyRuleCondition(
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
                users = openapi_client.models.user_policy_rule_condition.UserPolicyRuleCondition(
                    exclude = [
                        ''
                        ], 
                    inactivity = openapi_client.models.inactivity_policy_rule_condition.InactivityPolicyRuleCondition(
                        number = 56, 
                        unit = '', ), 
                    include = [
                        ''
                        ], 
                    lifecycle_expiration = openapi_client.models.lifecycle_expiration_policy_rule_condition.LifecycleExpirationPolicyRuleCondition(
                        lifecycle_status = '', 
                        number = 56, 
                        unit = '', ), 
                    password_expiration = openapi_client.models.password_expiration_policy_rule_condition.PasswordExpirationPolicyRuleCondition(
                        number = 56, 
                        unit = '', ), 
                    user_lifecycle_attribute = openapi_client.models.user_lifecycle_attribute_policy_rule_condition.UserLifecycleAttributePolicyRuleCondition(
                        attribute_name = '', 
                        matching_value = '', ), ),
                user_status = openapi_client.models.user_status_policy_rule_condition.UserStatusPolicyRuleCondition(
                    value = 'ACTIVATING', )
            )
        else:
            return AuthorizationServerPolicyRuleConditions(
        )
        """

    def testAuthorizationServerPolicyRuleConditions(self):
        """Test AuthorizationServerPolicyRuleConditions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
