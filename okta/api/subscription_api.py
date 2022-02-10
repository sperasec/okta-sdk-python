# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API  # noqa: E501

    OpenAPI spec version: 2.10.0
    Contact: devex-public@okta.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from okta.swagger_api_client import ApiClient


class Subscription(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_role_subscription_by_notification_type(self, role_type_or_role_id, notification_type, **kwargs):  # noqa: E501
        """Get subscriptions of a Custom Role with a specific notification type  # noqa: E501

        When roleType Get subscriptions of a Role with a specific notification type. Else when roleId Get subscription of a Custom Role with a specific notification type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_role_subscription_by_notification_type(role_type_or_role_id, notification_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role_type_or_role_id: (required)
        :param str notification_type: (required)
        :return: Subscription
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_role_subscription_by_notification_type_with_http_info(role_type_or_role_id, notification_type, **kwargs)  # noqa: E501
        else:
            (data) = self.get_role_subscription_by_notification_type_with_http_info(role_type_or_role_id, notification_type, **kwargs)  # noqa: E501
            return data

    def get_role_subscription_by_notification_type_with_http_info(self, role_type_or_role_id, notification_type, **kwargs):  # noqa: E501
        """Get subscriptions of a Custom Role with a specific notification type  # noqa: E501

        When roleType Get subscriptions of a Role with a specific notification type. Else when roleId Get subscription of a Custom Role with a specific notification type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_role_subscription_by_notification_type_with_http_info(role_type_or_role_id, notification_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role_type_or_role_id: (required)
        :param str notification_type: (required)
        :return: Subscription
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['role_type_or_role_id', 'notification_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_role_subscription_by_notification_type" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'role_type_or_role_id' is set
        if ('role_type_or_role_id' not in params or
                params['role_type_or_role_id'] is None):
            raise ValueError("Missing the required parameter `role_type_or_role_id` when calling `get_role_subscription_by_notification_type`")  # noqa: E501
        # verify the required parameter 'notification_type' is set
        if ('notification_type' not in params or
                params['notification_type'] is None):
            raise ValueError("Missing the required parameter `notification_type` when calling `get_role_subscription_by_notification_type`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'role_type_or_role_id' in params:
            path_params['roleTypeOrRoleId'] = params['role_type_or_role_id']  # noqa: E501
        if 'notification_type' in params:
            path_params['notificationType'] = params['notification_type']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_token', 'oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/roles/{roleTypeOrRoleId}/subscriptions/{notificationType}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Subscription',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_subscription_by_notification_type(self, user_id, notification_type, **kwargs):  # noqa: E501
        """Get the subscription of a User with a specific notification type  # noqa: E501

        Get the subscriptions of a User with a specific notification type. Only gets subscriptions for current user. An AccessDeniedException message is sent if requests are made from other users.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_subscription_by_notification_type(user_id, notification_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: (required)
        :param str notification_type: (required)
        :return: Subscription
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_subscription_by_notification_type_with_http_info(user_id, notification_type, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_subscription_by_notification_type_with_http_info(user_id, notification_type, **kwargs)  # noqa: E501
            return data

    def get_user_subscription_by_notification_type_with_http_info(self, user_id, notification_type, **kwargs):  # noqa: E501
        """Get the subscription of a User with a specific notification type  # noqa: E501

        Get the subscriptions of a User with a specific notification type. Only gets subscriptions for current user. An AccessDeniedException message is sent if requests are made from other users.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_subscription_by_notification_type_with_http_info(user_id, notification_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: (required)
        :param str notification_type: (required)
        :return: Subscription
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'notification_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_subscription_by_notification_type" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_user_subscription_by_notification_type`")  # noqa: E501
        # verify the required parameter 'notification_type' is set
        if ('notification_type' not in params or
                params['notification_type'] is None):
            raise ValueError("Missing the required parameter `notification_type` when calling `get_user_subscription_by_notification_type`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']  # noqa: E501
        if 'notification_type' in params:
            path_params['notificationType'] = params['notification_type']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_token', 'oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/users/{userId}/subscriptions/{notificationType}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Subscription',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_role_subscriptions(self, role_type_or_role_id, **kwargs):  # noqa: E501
        """List all subscriptions of a Custom Role  # noqa: E501

        When roleType List all subscriptions of a Role. Else when roleId List subscriptions of a Custom Role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_role_subscriptions(role_type_or_role_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role_type_or_role_id: (required)
        :return: list[Subscription]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_role_subscriptions_with_http_info(role_type_or_role_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_role_subscriptions_with_http_info(role_type_or_role_id, **kwargs)  # noqa: E501
            return data

    def list_role_subscriptions_with_http_info(self, role_type_or_role_id, **kwargs):  # noqa: E501
        """List all subscriptions of a Custom Role  # noqa: E501

        When roleType List all subscriptions of a Role. Else when roleId List subscriptions of a Custom Role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_role_subscriptions_with_http_info(role_type_or_role_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role_type_or_role_id: (required)
        :return: list[Subscription]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['role_type_or_role_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_role_subscriptions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'role_type_or_role_id' is set
        if ('role_type_or_role_id' not in params or
                params['role_type_or_role_id'] is None):
            raise ValueError("Missing the required parameter `role_type_or_role_id` when calling `list_role_subscriptions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'role_type_or_role_id' in params:
            path_params['roleTypeOrRoleId'] = params['role_type_or_role_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_token', 'oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/roles/{roleTypeOrRoleId}/subscriptions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Subscription]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_user_subscriptions(self, user_id, **kwargs):  # noqa: E501
        """List subscriptions of a User  # noqa: E501

        List subscriptions of a User. Only lists subscriptions for current user. An AccessDeniedException message is sent if requests are made from other users.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_subscriptions(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: (required)
        :return: list[Subscription]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_user_subscriptions_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_user_subscriptions_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def list_user_subscriptions_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """List subscriptions of a User  # noqa: E501

        List subscriptions of a User. Only lists subscriptions for current user. An AccessDeniedException message is sent if requests are made from other users.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_subscriptions_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: (required)
        :return: list[Subscription]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_user_subscriptions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `list_user_subscriptions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_token', 'oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/users/{userId}/subscriptions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Subscription]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def subscribe_role_subscription_by_notification_type(self, role_type_or_role_id, notification_type, **kwargs):  # noqa: E501
        """Subscribe a Custom Role to a specific notification type  # noqa: E501

        When roleType Subscribes a Role to a specific notification type. When you change the subscription status of a Role, it overrides the subscription of any individual user of that Role. Else when roleId Subscribes a Custom Role to a specific notification type. When you change the subscription status of a Custom Role, it overrides the subscription of any individual user of that Custom Role.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.subscribe_role_subscription_by_notification_type(role_type_or_role_id, notification_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role_type_or_role_id: (required)
        :param str notification_type: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.subscribe_role_subscription_by_notification_type_with_http_info(role_type_or_role_id, notification_type, **kwargs)  # noqa: E501
        else:
            (data) = self.subscribe_role_subscription_by_notification_type_with_http_info(role_type_or_role_id, notification_type, **kwargs)  # noqa: E501
            return data

    def subscribe_role_subscription_by_notification_type_with_http_info(self, role_type_or_role_id, notification_type, **kwargs):  # noqa: E501
        """Subscribe a Custom Role to a specific notification type  # noqa: E501

        When roleType Subscribes a Role to a specific notification type. When you change the subscription status of a Role, it overrides the subscription of any individual user of that Role. Else when roleId Subscribes a Custom Role to a specific notification type. When you change the subscription status of a Custom Role, it overrides the subscription of any individual user of that Custom Role.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.subscribe_role_subscription_by_notification_type_with_http_info(role_type_or_role_id, notification_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role_type_or_role_id: (required)
        :param str notification_type: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['role_type_or_role_id', 'notification_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method subscribe_role_subscription_by_notification_type" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'role_type_or_role_id' is set
        if ('role_type_or_role_id' not in params or
                params['role_type_or_role_id'] is None):
            raise ValueError("Missing the required parameter `role_type_or_role_id` when calling `subscribe_role_subscription_by_notification_type`")  # noqa: E501
        # verify the required parameter 'notification_type' is set
        if ('notification_type' not in params or
                params['notification_type'] is None):
            raise ValueError("Missing the required parameter `notification_type` when calling `subscribe_role_subscription_by_notification_type`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'role_type_or_role_id' in params:
            path_params['roleTypeOrRoleId'] = params['role_type_or_role_id']  # noqa: E501
        if 'notification_type' in params:
            path_params['notificationType'] = params['notification_type']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['api_token', 'oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/roles/{roleTypeOrRoleId}/subscriptions/{notificationType}/subscribe', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def subscribe_user_subscription_by_notification_type(self, user_id, notification_type, **kwargs):  # noqa: E501
        """Subscribe to a specific notification type  # noqa: E501

        Subscribes a User to a specific notification type. Only the current User can subscribe to a specific notification type. An AccessDeniedException message is sent if requests are made from other users.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.subscribe_user_subscription_by_notification_type(user_id, notification_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: (required)
        :param str notification_type: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.subscribe_user_subscription_by_notification_type_with_http_info(user_id, notification_type, **kwargs)  # noqa: E501
        else:
            (data) = self.subscribe_user_subscription_by_notification_type_with_http_info(user_id, notification_type, **kwargs)  # noqa: E501
            return data

    def subscribe_user_subscription_by_notification_type_with_http_info(self, user_id, notification_type, **kwargs):  # noqa: E501
        """Subscribe to a specific notification type  # noqa: E501

        Subscribes a User to a specific notification type. Only the current User can subscribe to a specific notification type. An AccessDeniedException message is sent if requests are made from other users.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.subscribe_user_subscription_by_notification_type_with_http_info(user_id, notification_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: (required)
        :param str notification_type: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'notification_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method subscribe_user_subscription_by_notification_type" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `subscribe_user_subscription_by_notification_type`")  # noqa: E501
        # verify the required parameter 'notification_type' is set
        if ('notification_type' not in params or
                params['notification_type'] is None):
            raise ValueError("Missing the required parameter `notification_type` when calling `subscribe_user_subscription_by_notification_type`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']  # noqa: E501
        if 'notification_type' in params:
            path_params['notificationType'] = params['notification_type']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['api_token', 'oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/users/{userId}/subscriptions/{notificationType}/subscribe', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def unsubscribe_role_subscription_by_notification_type(self, role_type_or_role_id, notification_type, **kwargs):  # noqa: E501
        """Unsubscribe a Custom Role from a specific notification type  # noqa: E501

        When roleType Unsubscribes a Role from a specific notification type. When you change the subscription status of a Role, it overrides the subscription of any individual user of that Role. Else when roleId Unsubscribes a Custom Role from a specific notification type. When you change the subscription status of a Custom Role, it overrides the subscription of any individual user of that Custom Role.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.unsubscribe_role_subscription_by_notification_type(role_type_or_role_id, notification_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role_type_or_role_id: (required)
        :param str notification_type: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.unsubscribe_role_subscription_by_notification_type_with_http_info(role_type_or_role_id, notification_type, **kwargs)  # noqa: E501
        else:
            (data) = self.unsubscribe_role_subscription_by_notification_type_with_http_info(role_type_or_role_id, notification_type, **kwargs)  # noqa: E501
            return data

    def unsubscribe_role_subscription_by_notification_type_with_http_info(self, role_type_or_role_id, notification_type, **kwargs):  # noqa: E501
        """Unsubscribe a Custom Role from a specific notification type  # noqa: E501

        When roleType Unsubscribes a Role from a specific notification type. When you change the subscription status of a Role, it overrides the subscription of any individual user of that Role. Else when roleId Unsubscribes a Custom Role from a specific notification type. When you change the subscription status of a Custom Role, it overrides the subscription of any individual user of that Custom Role.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.unsubscribe_role_subscription_by_notification_type_with_http_info(role_type_or_role_id, notification_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role_type_or_role_id: (required)
        :param str notification_type: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['role_type_or_role_id', 'notification_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method unsubscribe_role_subscription_by_notification_type" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'role_type_or_role_id' is set
        if ('role_type_or_role_id' not in params or
                params['role_type_or_role_id'] is None):
            raise ValueError("Missing the required parameter `role_type_or_role_id` when calling `unsubscribe_role_subscription_by_notification_type`")  # noqa: E501
        # verify the required parameter 'notification_type' is set
        if ('notification_type' not in params or
                params['notification_type'] is None):
            raise ValueError("Missing the required parameter `notification_type` when calling `unsubscribe_role_subscription_by_notification_type`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'role_type_or_role_id' in params:
            path_params['roleTypeOrRoleId'] = params['role_type_or_role_id']  # noqa: E501
        if 'notification_type' in params:
            path_params['notificationType'] = params['notification_type']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['api_token', 'oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/roles/{roleTypeOrRoleId}/subscriptions/{notificationType}/unsubscribe', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def unsubscribe_user_subscription_by_notification_type(self, user_id, notification_type, **kwargs):  # noqa: E501
        """Unsubscribe from a specific notification type  # noqa: E501

        Unsubscribes a User from a specific notification type. Only the current User can unsubscribe from a specific notification type. An AccessDeniedException message is sent if requests are made from other users.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.unsubscribe_user_subscription_by_notification_type(user_id, notification_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: (required)
        :param str notification_type: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.unsubscribe_user_subscription_by_notification_type_with_http_info(user_id, notification_type, **kwargs)  # noqa: E501
        else:
            (data) = self.unsubscribe_user_subscription_by_notification_type_with_http_info(user_id, notification_type, **kwargs)  # noqa: E501
            return data

    def unsubscribe_user_subscription_by_notification_type_with_http_info(self, user_id, notification_type, **kwargs):  # noqa: E501
        """Unsubscribe from a specific notification type  # noqa: E501

        Unsubscribes a User from a specific notification type. Only the current User can unsubscribe from a specific notification type. An AccessDeniedException message is sent if requests are made from other users.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.unsubscribe_user_subscription_by_notification_type_with_http_info(user_id, notification_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: (required)
        :param str notification_type: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'notification_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method unsubscribe_user_subscription_by_notification_type" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `unsubscribe_user_subscription_by_notification_type`")  # noqa: E501
        # verify the required parameter 'notification_type' is set
        if ('notification_type' not in params or
                params['notification_type'] is None):
            raise ValueError("Missing the required parameter `notification_type` when calling `unsubscribe_user_subscription_by_notification_type`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']  # noqa: E501
        if 'notification_type' in params:
            path_params['notificationType'] = params['notification_type']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['api_token', 'oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/users/{userId}/subscriptions/{notificationType}/unsubscribe', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)