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

from openapi_client.models.log_event import LogEvent

class TestLogEvent(unittest.TestCase):
    """LogEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LogEvent:
        """Test LogEvent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LogEvent`
        """
        model = LogEvent()
        if include_optional:
            return LogEvent(
                actor = openapi_client.models.log_actor.LogActor(
                    alternate_id = '', 
                    detail_entry = {
                        'key' : None
                        }, 
                    display_name = '', 
                    id = '', 
                    type = '', ),
                authentication_context = openapi_client.models.log_authentication_context.LogAuthenticationContext(
                    authentication_provider = 'ACTIVE_DIRECTORY', 
                    authentication_step = 56, 
                    credential_provider = 'DUO', 
                    credential_type = 'ASSERTION', 
                    external_session_id = '', 
                    interface = '', 
                    issuer = openapi_client.models.log_issuer.LogIssuer(
                        id = '', 
                        type = '', ), ),
                client = openapi_client.models.log_client.LogClient(
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
                    zone = '', ),
                debug_context = openapi_client.models.log_debug_context.LogDebugContext(
                    debug_data = {
                        'key' : None
                        }, ),
                display_message = '',
                event_type = '',
                legacy_event_type = '',
                outcome = openapi_client.models.log_outcome.LogOutcome(
                    reason = '', 
                    result = '', ),
                published = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                request = openapi_client.models.log_request.LogRequest(
                    ip_chain = [
                        openapi_client.models.log_ip_address.LogIpAddress(
                            geographical_context = openapi_client.models.log_geographical_context.LogGeographicalContext(
                                city = '', 
                                country = '', 
                                geolocation = openapi_client.models.log_geolocation.LogGeolocation(
                                    lat = 1.337, 
                                    lon = 1.337, ), 
                                postal_code = '', 
                                state = '', ), 
                            ip = '', 
                            source = '', 
                            version = '', )
                        ], ),
                security_context = openapi_client.models.log_security_context.LogSecurityContext(
                    as_number = 56, 
                    as_org = '', 
                    domain = '', 
                    isp = '', 
                    is_proxy = True, ),
                severity = 'DEBUG',
                target = [
                    openapi_client.models.log_target.LogTarget(
                        alternate_id = '', 
                        detail_entry = {
                            'key' : None
                            }, 
                        display_name = '', 
                        id = '', 
                        type = '', )
                    ],
                transaction = openapi_client.models.log_transaction.LogTransaction(
                    detail = {
                        'key' : None
                        }, 
                    id = '', 
                    type = '', ),
                uuid = '',
                version = ''
            )
        else:
            return LogEvent(
        )
        """

    def testLogEvent(self):
        """Test LogEvent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()