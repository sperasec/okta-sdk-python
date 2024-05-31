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

from openapi_client.models.multifactor_enrollment_policy_settings import MultifactorEnrollmentPolicySettings

class TestMultifactorEnrollmentPolicySettings(unittest.TestCase):
    """MultifactorEnrollmentPolicySettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MultifactorEnrollmentPolicySettings:
        """Test MultifactorEnrollmentPolicySettings
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MultifactorEnrollmentPolicySettings`
        """
        model = MultifactorEnrollmentPolicySettings()
        if include_optional:
            return MultifactorEnrollmentPolicySettings(
                authenticators = [
                    openapi_client.models.multifactor_enrollment_policy_authenticator_settings.MultifactorEnrollmentPolicyAuthenticatorSettings(
                        constraints = openapi_client.models.multifactor_enrollment_policy_authenticator_settings_constraints.MultifactorEnrollmentPolicyAuthenticatorSettings_constraints(
                            aaguid_groups = [
                                ''
                                ], ), 
                        enroll = openapi_client.models.multifactor_enrollment_policy_authenticator_settings_enroll.MultifactorEnrollmentPolicyAuthenticatorSettings_enroll(
                            self = 'NOT_ALLOWED', ), 
                        key = 'custom_app', )
                    ],
                type = 'AUTHENTICATORS'
            )
        else:
            return MultifactorEnrollmentPolicySettings(
        )
        """

    def testMultifactorEnrollmentPolicySettings(self):
        """Test MultifactorEnrollmentPolicySettings"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()