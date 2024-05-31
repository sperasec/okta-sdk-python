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

from openapi_client.models.identity_provider_policy import IdentityProviderPolicy

class TestIdentityProviderPolicy(unittest.TestCase):
    """IdentityProviderPolicy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdentityProviderPolicy:
        """Test IdentityProviderPolicy
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdentityProviderPolicy`
        """
        model = IdentityProviderPolicy()
        if include_optional:
            return IdentityProviderPolicy(
                account_link = openapi_client.models.policy_account_link.PolicyAccountLink(
                    action = 'AUTO', 
                    filter = openapi_client.models.policy_account_link_filter.PolicyAccountLinkFilter(
                        groups = openapi_client.models.policy_account_link_filter_groups.PolicyAccountLinkFilterGroups(
                            include = [
                                ''
                                ], ), ), ),
                map_amr_claims = True,
                max_clock_skew = 56,
                provisioning = openapi_client.models.provisioning.Provisioning(
                    action = 'AUTO', 
                    conditions = openapi_client.models.provisioning_conditions.ProvisioningConditions(
                        deprovisioned = openapi_client.models.provisioning_deprovisioned_condition.ProvisioningDeprovisionedCondition(), 
                        suspended = openapi_client.models.provisioning_suspended_condition.ProvisioningSuspendedCondition(), ), 
                    groups = openapi_client.models.provisioning_groups.ProvisioningGroups(
                        assignments = [
                            ''
                            ], 
                        filter = [
                            ''
                            ], 
                        source_attribute_name = '', ), 
                    profile_master = True, ),
                subject = openapi_client.models.policy_subject.PolicySubject(
                    filter = '', 
                    format = [
                        ''
                        ], 
                    match_attribute = '', 
                    match_type = 'CUSTOM_ATTRIBUTE', 
                    user_name_template = openapi_client.models.policy_user_name_template.PolicyUserNameTemplate(
                        template = '', ), )
            )
        else:
            return IdentityProviderPolicy(
        )
        """

    def testIdentityProviderPolicy(self):
        """Test IdentityProviderPolicy"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()