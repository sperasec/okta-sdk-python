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

from openapi_client.models.device_assurance_windows_platform_all_of_third_party_signal_providers import DeviceAssuranceWindowsPlatformAllOfThirdPartySignalProviders

class TestDeviceAssuranceWindowsPlatformAllOfThirdPartySignalProviders(unittest.TestCase):
    """DeviceAssuranceWindowsPlatformAllOfThirdPartySignalProviders unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceAssuranceWindowsPlatformAllOfThirdPartySignalProviders:
        """Test DeviceAssuranceWindowsPlatformAllOfThirdPartySignalProviders
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceAssuranceWindowsPlatformAllOfThirdPartySignalProviders`
        """
        model = DeviceAssuranceWindowsPlatformAllOfThirdPartySignalProviders()
        if include_optional:
            return DeviceAssuranceWindowsPlatformAllOfThirdPartySignalProviders(
                dtc = openapi_client.models.dtc_windows.DTCWindows(
                    browser_version = openapi_client.models.chrome_browser_version.ChromeBrowserVersion(
                        minimum = '', ), 
                    built_in_dns_client_enabled = True, 
                    chrome_remote_desktop_app_blocked = True, 
                    crowd_strike_agent_id = '', 
                    crowd_strike_customer_id = '', 
                    device_enrollment_domain = '', 
                    disk_enrypted = True, 
                    key_trust_level = 'CHROME_BROWSER_HW_KEY', 
                    os_firewall = True, 
                    os_version = openapi_client.models.os_version.OSVersion(
                        minimum = '', ), 
                    password_protection_warning_trigger = 'PHISHING_REUSE', 
                    realtime_url_check_mode = True, 
                    safe_browsing_protection_level = 'ENHANCED_PROTECTION', 
                    screen_lock_secured = True, 
                    secure_boot_enabled = True, 
                    site_isolation_enabled = True, 
                    third_party_blocking_enabled = True, 
                    windows_machine_domain = '', 
                    windows_user_domain = '', )
            )
        else:
            return DeviceAssuranceWindowsPlatformAllOfThirdPartySignalProviders(
        )
        """

    def testDeviceAssuranceWindowsPlatformAllOfThirdPartySignalProviders(self):
        """Test DeviceAssuranceWindowsPlatformAllOfThirdPartySignalProviders"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
