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

from openapi_client.models.auto_login_application_settings_sign_on import AutoLoginApplicationSettingsSignOn

class TestAutoLoginApplicationSettingsSignOn(unittest.TestCase):
    """AutoLoginApplicationSettingsSignOn unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AutoLoginApplicationSettingsSignOn:
        """Test AutoLoginApplicationSettingsSignOn
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AutoLoginApplicationSettingsSignOn`
        """
        model = AutoLoginApplicationSettingsSignOn()
        if include_optional:
            return AutoLoginApplicationSettingsSignOn(
                login_url = '',
                redirect_url = ''
            )
        else:
            return AutoLoginApplicationSettingsSignOn(
        )
        """

    def testAutoLoginApplicationSettingsSignOn(self):
        """Test AutoLoginApplicationSettingsSignOn"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()