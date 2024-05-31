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

from openapi_client.models.simulate_policy_body import SimulatePolicyBody

class TestSimulatePolicyBody(unittest.TestCase):
    """SimulatePolicyBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SimulatePolicyBody:
        """Test SimulatePolicyBody
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SimulatePolicyBody`
        """
        model = SimulatePolicyBody()
        if include_optional:
            return SimulatePolicyBody(
                policy_types = [
                    'ACCESS_POLICY'
                    ],
                app_instance = '',
                policy_context = openapi_client.models.policy_context.PolicyContext(
                    user = openapi_client.models.policy_context_user.PolicyContext_user(
                        id = '', ), 
                    groups = openapi_client.models.policy_context_groups.PolicyContext_groups(
                        ids = [
                            ''
                            ], ), 
                    risk = openapi_client.models.policy_context_risk.PolicyContext_risk(
                        level = 'LOW', ), 
                    ip = '', 
                    zones = openapi_client.models.policy_context_zones.PolicyContext_zones(), 
                    device = openapi_client.models.policy_context_device.PolicyContext_device(
                        platform = '', 
                        registered = True, 
                        managed = True, ), )
            )
        else:
            return SimulatePolicyBody(
                app_instance = '',
        )
        """

    def testSimulatePolicyBody(self):
        """Test SimulatePolicyBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()