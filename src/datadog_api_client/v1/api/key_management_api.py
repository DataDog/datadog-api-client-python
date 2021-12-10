# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import re  # noqa: F401

from datadog_api_client.v1.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v1.model_utils import (  # noqa: F401
    date,
    datetime,
    file_type,
    none_type,
)
from datadog_api_client.v1.model.api_error_response import APIErrorResponse
from datadog_api_client.v1.model.api_key import ApiKey
from datadog_api_client.v1.model.api_key_list_response import ApiKeyListResponse
from datadog_api_client.v1.model.api_key_response import ApiKeyResponse
from datadog_api_client.v1.model.application_key import ApplicationKey
from datadog_api_client.v1.model.application_key_list_response import ApplicationKeyListResponse
from datadog_api_client.v1.model.application_key_response import ApplicationKeyResponse


class KeyManagementApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._create_api_key_endpoint = _Endpoint(
            settings={
                "response_type": (ApiKeyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/api_key",
                "operation_id": "create_api_key",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ApiKey,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_application_key_endpoint = _Endpoint(
            settings={
                "response_type": (ApplicationKeyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/application_key",
                "operation_id": "create_application_key",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ApplicationKey,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_api_key_endpoint = _Endpoint(
            settings={
                "response_type": (ApiKeyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/api_key/{key}",
                "operation_id": "delete_api_key",
                "http_method": "DELETE",
                "servers": None,
            },
            params_map={
                "key": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "key",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._delete_application_key_endpoint = _Endpoint(
            settings={
                "response_type": (ApplicationKeyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/application_key/{key}",
                "operation_id": "delete_application_key",
                "http_method": "DELETE",
                "servers": None,
            },
            params_map={
                "key": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "key",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_api_key_endpoint = _Endpoint(
            settings={
                "response_type": (ApiKeyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/api_key/{key}",
                "operation_id": "get_api_key",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "key": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "key",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_application_key_endpoint = _Endpoint(
            settings={
                "response_type": (ApplicationKeyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/application_key/{key}",
                "operation_id": "get_application_key",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "key": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "key",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_api_keys_endpoint = _Endpoint(
            settings={
                "response_type": (ApiKeyListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/api_key",
                "operation_id": "list_api_keys",
                "http_method": "GET",
                "servers": None,
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_application_keys_endpoint = _Endpoint(
            settings={
                "response_type": (ApplicationKeyListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/application_key",
                "operation_id": "list_application_keys",
                "http_method": "GET",
                "servers": None,
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._update_api_key_endpoint = _Endpoint(
            settings={
                "response_type": (ApiKeyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/api_key/{key}",
                "operation_id": "update_api_key",
                "http_method": "PUT",
                "servers": None,
            },
            params_map={
                "key": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "key",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ApiKey,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_application_key_endpoint = _Endpoint(
            settings={
                "response_type": (ApplicationKeyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/application_key/{key}",
                "operation_id": "update_application_key",
                "http_method": "PUT",
                "servers": None,
            },
            params_map={
                "key": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "key",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ApplicationKey,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_api_key(self, body, **kwargs):
        """Create an API key

        Creates an API key with a given name.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.create_api_key(body, async_req=True)
        >>> result = thread.get()

        Args:
            body (ApiKey):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (float/tuple): timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ApiKeyResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._create_api_key_endpoint.default_arguments(kwargs)
        kwargs["body"] = body
        return self._create_api_key_endpoint.call_with_http_info(**kwargs)

    def create_application_key(self, body, **kwargs):
        """Create an application key

        Create an application key with a given name.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.create_application_key(body, async_req=True)
        >>> result = thread.get()

        Args:
            body (ApplicationKey):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (float/tuple): timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ApplicationKeyResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._create_application_key_endpoint.default_arguments(kwargs)
        kwargs["body"] = body
        return self._create_application_key_endpoint.call_with_http_info(**kwargs)

    def delete_api_key(self, key, **kwargs):
        """Delete an API key

        Delete a given API key.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.delete_api_key(key, async_req=True)
        >>> result = thread.get()

        Args:
            key (str): The specific API key you are working with.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (float/tuple): timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ApiKeyResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._delete_api_key_endpoint.default_arguments(kwargs)
        kwargs["key"] = key
        return self._delete_api_key_endpoint.call_with_http_info(**kwargs)

    def delete_application_key(self, key, **kwargs):
        """Delete an application key

        Delete a given application key.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.delete_application_key(key, async_req=True)
        >>> result = thread.get()

        Args:
            key (str): The specific APP key you are working with.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (float/tuple): timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ApplicationKeyResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._delete_application_key_endpoint.default_arguments(kwargs)
        kwargs["key"] = key
        return self._delete_application_key_endpoint.call_with_http_info(**kwargs)

    def get_api_key(self, key, **kwargs):
        """Get API key

        Get a given API key.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.get_api_key(key, async_req=True)
        >>> result = thread.get()

        Args:
            key (str): The specific API key you are working with.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (float/tuple): timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ApiKeyResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._get_api_key_endpoint.default_arguments(kwargs)
        kwargs["key"] = key
        return self._get_api_key_endpoint.call_with_http_info(**kwargs)

    def get_application_key(self, key, **kwargs):
        """Get an application key

        Get a given application key.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.get_application_key(key, async_req=True)
        >>> result = thread.get()

        Args:
            key (str): The specific APP key you are working with.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (float/tuple): timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ApplicationKeyResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._get_application_key_endpoint.default_arguments(kwargs)
        kwargs["key"] = key
        return self._get_application_key_endpoint.call_with_http_info(**kwargs)

    def list_api_keys(self, **kwargs):
        """Get all API keys

        Get all API keys available for your account.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_api_keys(async_req=True)
        >>> result = thread.get()

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (float/tuple): timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ApiKeyListResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._list_api_keys_endpoint.default_arguments(kwargs)
        return self._list_api_keys_endpoint.call_with_http_info(**kwargs)

    def list_application_keys(self, **kwargs):
        """Get all application keys

        Get all application keys available for your Datadog account.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_application_keys(async_req=True)
        >>> result = thread.get()

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (float/tuple): timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ApplicationKeyListResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._list_application_keys_endpoint.default_arguments(kwargs)
        return self._list_application_keys_endpoint.call_with_http_info(**kwargs)

    def update_api_key(self, key, body, **kwargs):
        """Edit an API key

        Edit an API key name.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.update_api_key(key, body, async_req=True)
        >>> result = thread.get()

        Args:
            key (str): The specific API key you are working with.
            body (ApiKey):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (float/tuple): timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ApiKeyResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._update_api_key_endpoint.default_arguments(kwargs)
        kwargs["key"] = key
        kwargs["body"] = body
        return self._update_api_key_endpoint.call_with_http_info(**kwargs)

    def update_application_key(self, key, body, **kwargs):
        """Edit an application key

        Edit an application key name.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.update_application_key(key, body, async_req=True)
        >>> result = thread.get()

        Args:
            key (str): The specific APP key you are working with.
            body (ApplicationKey):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (float/tuple): timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ApplicationKeyResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._update_application_key_endpoint.default_arguments(kwargs)
        kwargs["key"] = key
        kwargs["body"] = body
        return self._update_application_key_endpoint.call_with_http_info(**kwargs)
