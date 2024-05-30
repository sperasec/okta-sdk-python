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

from openapi_client.models.org_okta_communication_setting import OrgOktaCommunicationSetting

class TestOrgOktaCommunicationSetting(unittest.TestCase):
    """OrgOktaCommunicationSetting unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrgOktaCommunicationSetting:
        """Test OrgOktaCommunicationSetting
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrgOktaCommunicationSetting`
        """
        model = OrgOktaCommunicationSetting()
        if include_optional:
            return OrgOktaCommunicationSetting(
                opt_out_email_users = True,
                links = openapi_client.models.links_self.LinksSelf(
                    self = null, )
            )
        else:
            return OrgOktaCommunicationSetting(
        )
        """

    def testOrgOktaCommunicationSetting(self):
        """Test OrgOktaCommunicationSetting"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
