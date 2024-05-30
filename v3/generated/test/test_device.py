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

from openapi_client.models.device import Device

class TestDevice(unittest.TestCase):
    """Device unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Device:
        """Test Device
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Device`
        """
        model = Device()
        if include_optional:
            return Device(
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '',
                last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                profile = openapi_client.models.device_profile.DeviceProfile(
                    disk_encryption_type = 'ALL_INTERNAL_VOLUMES', 
                    display_name = '0', 
                    imei = '012345678910111213', 
                    integrity_jailbreak = True, 
                    manufacturer = '', 
                    meid = '', 
                    model = '', 
                    os_version = '', 
                    platform = 'ANDROID', 
                    registered = True, 
                    secure_hardware_present = True, 
                    serial_number = '', 
                    sid = '', 
                    tpm_public_key_hash = '', 
                    udid = '', ),
                resource_alternate_id = '',
                resource_display_name = openapi_client.models.device_display_name.DeviceDisplayName(
                    sensitive = True, 
                    value = '', ),
                resource_id = '',
                resource_type = 'UDDevice',
                status = 'ACTIVE',
                links = None
            )
        else:
            return Device(
        )
        """

    def testDevice(self):
        """Test Device"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
