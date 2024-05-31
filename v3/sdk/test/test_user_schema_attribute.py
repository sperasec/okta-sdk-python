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

from openapi_client.models.user_schema_attribute import UserSchemaAttribute

class TestUserSchemaAttribute(unittest.TestCase):
    """UserSchemaAttribute unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserSchemaAttribute:
        """Test UserSchemaAttribute
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserSchemaAttribute`
        """
        model = UserSchemaAttribute()
        if include_optional:
            return UserSchemaAttribute(
                description = '',
                enum = [
                    ''
                    ],
                external_name = '',
                external_namespace = '',
                items = openapi_client.models.user_schema_attribute_items.UserSchemaAttributeItems(
                    enum = [
                        ''
                        ], 
                    one_of = [
                        openapi_client.models.user_schema_attribute_enum.UserSchemaAttributeEnum(
                            const = '', 
                            title = '', )
                        ], 
                    type = '', ),
                master = openapi_client.models.user_schema_attribute_master.UserSchemaAttributeMaster(
                    priority = [
                        openapi_client.models.user_schema_attribute_master_priority.UserSchemaAttributeMasterPriority(
                            type = '', 
                            value = '', )
                        ], 
                    type = 'OKTA', ),
                max_length = 56,
                min_length = 56,
                mutability = '',
                one_of = [
                    openapi_client.models.user_schema_attribute_enum.UserSchemaAttributeEnum(
                        const = '', 
                        title = '', )
                    ],
                pattern = '',
                permissions = [
                    openapi_client.models.user_schema_attribute_permission.UserSchemaAttributePermission(
                        action = '', 
                        principal = '', )
                    ],
                required = True,
                scope = 'NONE',
                title = '',
                type = 'array',
                union = 'DISABLE',
                unique = ''
            )
        else:
            return UserSchemaAttribute(
        )
        """

    def testUserSchemaAttribute(self):
        """Test UserSchemaAttribute"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()