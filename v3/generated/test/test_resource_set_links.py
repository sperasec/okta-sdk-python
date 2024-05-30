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

from openapi_client.models.resource_set_links import ResourceSetLinks

class TestResourceSetLinks(unittest.TestCase):
    """ResourceSetLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResourceSetLinks:
        """Test ResourceSetLinks
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResourceSetLinks`
        """
        model = ResourceSetLinks()
        if include_optional:
            return ResourceSetLinks(
                var_self = None,
                resources = openapi_client.models.link_object.Link Object(
                    hints = openapi_client.models.href_object_hints.HrefObject_hints(
                        allow = [
                            'DELETE'
                            ], ), 
                    href = '', 
                    name = '', 
                    type = '', ),
                bindings = openapi_client.models.link_object.Link Object(
                    hints = openapi_client.models.href_object_hints.HrefObject_hints(
                        allow = [
                            'DELETE'
                            ], ), 
                    href = '', 
                    name = '', 
                    type = '', )
            )
        else:
            return ResourceSetLinks(
        )
        """

    def testResourceSetLinks(self):
        """Test ResourceSetLinks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
