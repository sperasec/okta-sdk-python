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

from openapi_client.models.application_group_assignment import ApplicationGroupAssignment

class TestApplicationGroupAssignment(unittest.TestCase):
    """ApplicationGroupAssignment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApplicationGroupAssignment:
        """Test ApplicationGroupAssignment
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApplicationGroupAssignment`
        """
        model = ApplicationGroupAssignment()
        if include_optional:
            return ApplicationGroupAssignment(
                id = '',
                last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                priority = 56,
                profile = {
                    'key' : None
                    },
                embedded = {
                    'key' : None
                    },
                links = openapi_client.models.links_self.LinksSelf(
                    self = null, )
            )
        else:
            return ApplicationGroupAssignment(
        )
        """

    def testApplicationGroupAssignment(self):
        """Test ApplicationGroupAssignment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()