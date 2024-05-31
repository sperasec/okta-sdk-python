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

from openapi_client.models.ui_schema_object import UISchemaObject

class TestUISchemaObject(unittest.TestCase):
    """UISchemaObject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UISchemaObject:
        """Test UISchemaObject
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UISchemaObject`
        """
        model = UISchemaObject()
        if include_optional:
            return UISchemaObject(
                button_label = 'Submit',
                elements = None,
                label = 'Sign in',
                type = ''
            )
        else:
            return UISchemaObject(
        )
        """

    def testUISchemaObject(self):
        """Test UISchemaObject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()