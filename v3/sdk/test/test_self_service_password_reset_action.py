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

from openapi_client.models.self_service_password_reset_action import SelfServicePasswordResetAction

class TestSelfServicePasswordResetAction(unittest.TestCase):
    """SelfServicePasswordResetAction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SelfServicePasswordResetAction:
        """Test SelfServicePasswordResetAction
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SelfServicePasswordResetAction`
        """
        model = SelfServicePasswordResetAction()
        if include_optional:
            return SelfServicePasswordResetAction(
                access = 'ALLOW',
                type = 'selfServicePasswordReset',
                requirement = openapi_client.models.sspr_requirement.SsprRequirement(
                    primary = openapi_client.models.sspr_primary_requirement.SsprPrimaryRequirement(
                        methods = [
                            'push'
                            ], 
                        method_constraints = [
                            openapi_client.models.authenticator_method_constraint.AuthenticatorMethodConstraint(
                                method = 'otp', 
                                allowed_authenticators = [
                                    openapi_client.models.authenticator_identity.AuthenticatorIdentity(
                                        key = '', )
                                    ], )
                            ], ), 
                    step_up = openapi_client.models.sspr_step_up_requirement.SsprStepUpRequirement(
                        required = True, ), )
            )
        else:
            return SelfServicePasswordResetAction(
        )
        """

    def testSelfServicePasswordResetAction(self):
        """Test SelfServicePasswordResetAction"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()