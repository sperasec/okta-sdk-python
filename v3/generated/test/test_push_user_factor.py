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

from openapi_client.models.push_user_factor import PushUserFactor

class TestPushUserFactor(unittest.TestCase):
    """PushUserFactor unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PushUserFactor:
        """Test PushUserFactor
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PushUserFactor`
        """
        model = PushUserFactor()
        if include_optional:
            return PushUserFactor(
                expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                factor_result = 'CANCELLED',
                profile = openapi_client.models.push_user_factor_profile.PushUserFactorProfile(
                    credential_id = '', 
                    device_token = '', 
                    device_type = '', 
                    name = '', 
                    platform = '', 
                    version = '', )
            )
        else:
            return PushUserFactor(
        )
        """

    def testPushUserFactor(self):
        """Test PushUserFactor"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
