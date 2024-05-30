# coding: utf-8

"""
    Okta Admin Management

    Allows customers to easily access the Okta Management APIs

    The version of the OpenAPI document: 5.1.0
    Contact: devex-public@okta.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from datetime import datetime
from pydantic import StrictInt, StrictStr
from typing import Optional
from openapi_client.models.log_event import LogEvent

from openapi_client.api_client import ApiClient, RequestSerialized
from openapi_client.api_response import ApiResponse
from openapi_client.rest import RESTResponseType


class SystemLogApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def list_log_events(
        self,
        since: Optional[datetime] = None,
        until: Optional[datetime] = None,
        filter: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
        limit: Optional[StrictInt] = None,
        sort_order: Optional[StrictStr] = None,
        after: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> List[LogEvent]:
        """List all System Log Events

        Lists all system log events. The Okta System Log API provides read access to your organization’s system log. This API provides more functionality than the Events API

        :param since:
        :type since: datetime
        :param until:
        :type until: datetime
        :param filter:
        :type filter: str
        :param q:
        :type q: str
        :param limit:
        :type limit: int
        :param sort_order:
        :type sort_order: str
        :param after:
        :type after: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_log_events_serialize(
            since=since,
            until=until,
            filter=filter,
            q=q,
            limit=limit,
            sort_order=sort_order,
            after=after,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[LogEvent]",
            '403': "Error",
            '429': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def list_log_events_with_http_info(
        self,
        since: Optional[datetime] = None,
        until: Optional[datetime] = None,
        filter: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
        limit: Optional[StrictInt] = None,
        sort_order: Optional[StrictStr] = None,
        after: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[List[LogEvent]]:
        """List all System Log Events

        Lists all system log events. The Okta System Log API provides read access to your organization’s system log. This API provides more functionality than the Events API

        :param since:
        :type since: datetime
        :param until:
        :type until: datetime
        :param filter:
        :type filter: str
        :param q:
        :type q: str
        :param limit:
        :type limit: int
        :param sort_order:
        :type sort_order: str
        :param after:
        :type after: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_log_events_serialize(
            since=since,
            until=until,
            filter=filter,
            q=q,
            limit=limit,
            sort_order=sort_order,
            after=after,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[LogEvent]",
            '403': "Error",
            '429': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def list_log_events_without_preload_content(
        self,
        since: Optional[datetime] = None,
        until: Optional[datetime] = None,
        filter: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
        limit: Optional[StrictInt] = None,
        sort_order: Optional[StrictStr] = None,
        after: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """List all System Log Events

        Lists all system log events. The Okta System Log API provides read access to your organization’s system log. This API provides more functionality than the Events API

        :param since:
        :type since: datetime
        :param until:
        :type until: datetime
        :param filter:
        :type filter: str
        :param q:
        :type q: str
        :param limit:
        :type limit: int
        :param sort_order:
        :type sort_order: str
        :param after:
        :type after: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_log_events_serialize(
            since=since,
            until=until,
            filter=filter,
            q=q,
            limit=limit,
            sort_order=sort_order,
            after=after,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[LogEvent]",
            '403': "Error",
            '429': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _list_log_events_serialize(
        self,
        since,
        until,
        filter,
        q,
        limit,
        sort_order,
        after,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if since is not None:
            if isinstance(since, datetime):
                _query_params.append(
                    (
                        'since',
                        since.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('since', since))
            
        if until is not None:
            if isinstance(until, datetime):
                _query_params.append(
                    (
                        'until',
                        until.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('until', until))
            
        if filter is not None:
            
            _query_params.append(('filter', filter))
            
        if q is not None:
            
            _query_params.append(('q', q))
            
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        if sort_order is not None:
            
            _query_params.append(('sortOrder', sort_order))
            
        if after is not None:
            
            _query_params.append(('after', after))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
            'apiToken', 
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/logs',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


