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

from openapi_client.models.resource_set_binding_member import ResourceSetBindingMember

class TestResourceSetBindingMember(unittest.TestCase):
    """ResourceSetBindingMember unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResourceSetBindingMember:
        """Test ResourceSetBindingMember
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResourceSetBindingMember`
        """
        model = ResourceSetBindingMember()
        if include_optional:
            return ResourceSetBindingMember(
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '',
                last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                links = openapi_client.models.links_self.LinksSelf(
                    self = null, )
            )
        else:
            return ResourceSetBindingMember(
        )
        """

    def testResourceSetBindingMember(self):
        """Test ResourceSetBindingMember"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
