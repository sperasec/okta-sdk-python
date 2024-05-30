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

from openapi_client.models.log_client import LogClient

class TestLogClient(unittest.TestCase):
    """LogClient unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LogClient:
        """Test LogClient
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LogClient`
        """
        model = LogClient()
        if include_optional:
            return LogClient(
                device = '',
                geographical_context = openapi_client.models.log_geographical_context.LogGeographicalContext(
                    city = '', 
                    country = '', 
                    geolocation = openapi_client.models.log_geolocation.LogGeolocation(
                        lat = 1.337, 
                        lon = 1.337, ), 
                    postal_code = '', 
                    state = '', ),
                id = '',
                ip_address = '',
                user_agent = openapi_client.models.log_user_agent.LogUserAgent(
                    browser = '', 
                    os = '', 
                    raw_user_agent = '', ),
                zone = ''
            )
        else:
            return LogClient(
        )
        """

    def testLogClient(self):
        """Test LogClient"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
