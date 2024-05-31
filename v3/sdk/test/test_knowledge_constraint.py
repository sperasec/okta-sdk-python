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

from openapi_client.models.knowledge_constraint import KnowledgeConstraint

class TestKnowledgeConstraint(unittest.TestCase):
    """KnowledgeConstraint unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> KnowledgeConstraint:
        """Test KnowledgeConstraint
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `KnowledgeConstraint`
        """
        model = KnowledgeConstraint()
        if include_optional:
            return KnowledgeConstraint(
                methods = [
                    'PASSWORD'
                    ],
                reauthenticate_in = '',
                types = [
                    'SECURITY_KEY'
                    ],
                authentication_methods = [
                    openapi_client.models.authentication_method_object.AuthenticationMethodObject(
                        key = '', 
                        method = '', )
                    ],
                excluded_authentication_methods = [
                    openapi_client.models.authentication_method_object.AuthenticationMethodObject(
                        key = '', 
                        method = '', )
                    ],
                required = True
            )
        else:
            return KnowledgeConstraint(
        )
        """

    def testKnowledgeConstraint(self):
        """Test KnowledgeConstraint"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()