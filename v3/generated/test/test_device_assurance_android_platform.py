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

from openapi_client.models.device_assurance_android_platform import DeviceAssuranceAndroidPlatform

class TestDeviceAssuranceAndroidPlatform(unittest.TestCase):
    """DeviceAssuranceAndroidPlatform unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceAssuranceAndroidPlatform:
        """Test DeviceAssuranceAndroidPlatform
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceAssuranceAndroidPlatform`
        """
        model = DeviceAssuranceAndroidPlatform()
        if include_optional:
            return DeviceAssuranceAndroidPlatform(
                disk_encryption_type = openapi_client.models.device_assurance_android_platform_all_of_disk_encryption_type.DeviceAssuranceAndroidPlatform_allOf_diskEncryptionType(
                    include = [
                        'ALL_INTERNAL_VOLUMES'
                        ], ),
                jailbreak = True,
                os_version = openapi_client.models.os_version.OSVersion(
                    minimum = '', ),
                screen_lock_type = openapi_client.models.device_assurance_android_platform_all_of_screen_lock_type.DeviceAssuranceAndroidPlatform_allOf_screenLockType(
                    include = [
                        'BIOMETRIC'
                        ], ),
                secure_hardware_present = True
            )
        else:
            return DeviceAssuranceAndroidPlatform(
        )
        """

    def testDeviceAssuranceAndroidPlatform(self):
        """Test DeviceAssuranceAndroidPlatform"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
