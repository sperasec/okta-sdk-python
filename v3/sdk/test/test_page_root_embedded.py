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

from openapi_client.models.page_root_embedded import PageRootEmbedded

class TestPageRootEmbedded(unittest.TestCase):
    """PageRootEmbedded unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PageRootEmbedded:
        """Test PageRootEmbedded
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PageRootEmbedded`
        """
        model = PageRootEmbedded()
        if include_optional:
            return PageRootEmbedded(
                default = openapi_client.models.customizable_page.CustomizablePage(
                    page_content = '', ),
                customized = openapi_client.models.customizable_page.CustomizablePage(
                    page_content = '', ),
                customized_url = '',
                preview = openapi_client.models.customizable_page.CustomizablePage(
                    page_content = '', ),
                preview_url = ''
            )
        else:
            return PageRootEmbedded(
        )
        """

    def testPageRootEmbedded(self):
        """Test PageRootEmbedded"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()