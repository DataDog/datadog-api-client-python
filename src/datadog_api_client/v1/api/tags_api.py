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
from datadog_api_client.v1.model.host_tags import HostTags
from datadog_api_client.v1.model.tag_to_hosts import TagToHosts


class TagsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._create_host_tags_endpoint = _Endpoint(
            settings={
                "response_type": (HostTags,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/tags/hosts/{host_name}",
                "operation_id": "create_host_tags",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "host_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "host_name",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (HostTags,),
                    "location": "body",
                },
                "source": {
                    "openapi_types": (str,),
                    "attribute": "source",
                    "location": "query",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_host_tags_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/tags/hosts/{host_name}",
                "operation_id": "delete_host_tags",
                "http_method": "DELETE",
                "servers": None,
            },
            params_map={
                "host_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "host_name",
                    "location": "path",
                },
                "source": {
                    "openapi_types": (str,),
                    "attribute": "source",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_host_tags_endpoint = _Endpoint(
            settings={
                "response_type": (HostTags,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/tags/hosts/{host_name}",
                "operation_id": "get_host_tags",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "host_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "host_name",
                    "location": "path",
                },
                "source": {
                    "openapi_types": (str,),
                    "attribute": "source",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_host_tags_endpoint = _Endpoint(
            settings={
                "response_type": (TagToHosts,),
                "auth": ["AuthZ", "apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/tags/hosts",
                "operation_id": "list_host_tags",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "source": {
                    "openapi_types": (str,),
                    "attribute": "source",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._update_host_tags_endpoint = _Endpoint(
            settings={
                "response_type": (HostTags,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/tags/hosts/{host_name}",
                "operation_id": "update_host_tags",
                "http_method": "PUT",
                "servers": None,
            },
            params_map={
                "host_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "host_name",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (HostTags,),
                    "location": "body",
                },
                "source": {
                    "openapi_types": (str,),
                    "attribute": "source",
                    "location": "query",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_host_tags(self, host_name, body, **kwargs):
        """Add tags to a host

        This endpoint allows you to add new tags to a host, optionally specifying where these tags come from.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.create_host_tags(host_name, body, async_req=True)
        >>> result = thread.get()

        Args:
            host_name (str): This endpoint allows you to add new tags to a host, optionally specifying where the tags came from.
            body (HostTags): Update host tags request body.

        Keyword Args:
            source (str): [optional] The source of the tags. [Complete list of source attribute values](https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value).
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
            HostTags
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._create_host_tags_endpoint.default_arguments(kwargs)
        kwargs["host_name"] = host_name
        kwargs["body"] = body
        return self._create_host_tags_endpoint.call_with_http_info(**kwargs)

    def delete_host_tags(self, host_name, **kwargs):
        """Remove host tags

        This endpoint allows you to remove all user-assigned tags for a single host.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.delete_host_tags(host_name, async_req=True)
        >>> result = thread.get()

        Args:
            host_name (str): This endpoint allows you to remove all user-assigned tags for a single host.

        Keyword Args:
            source (str): [optional] The source of the tags (for example chef, puppet). [Complete list of source attribute values](https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value).
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
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._delete_host_tags_endpoint.default_arguments(kwargs)
        kwargs["host_name"] = host_name
        return self._delete_host_tags_endpoint.call_with_http_info(**kwargs)

    def get_host_tags(self, host_name, **kwargs):
        """Get host tags

        Return the list of tags that apply to a given host.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.get_host_tags(host_name, async_req=True)
        >>> result = thread.get()

        Args:
            host_name (str): When specified, filters list of tags to those tags with the specified source.

        Keyword Args:
            source (str): [optional] Source to filter.
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
            HostTags
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._get_host_tags_endpoint.default_arguments(kwargs)
        kwargs["host_name"] = host_name
        return self._get_host_tags_endpoint.call_with_http_info(**kwargs)

    def list_host_tags(self, **kwargs):
        """Get Tags

        Return a mapping of tags to hosts for your whole infrastructure.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_host_tags(async_req=True)
        >>> result = thread.get()

        Keyword Args:
            source (str): [optional] When specified, filters host list to those tags with the specified source.
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
            TagToHosts
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._list_host_tags_endpoint.default_arguments(kwargs)
        return self._list_host_tags_endpoint.call_with_http_info(**kwargs)

    def update_host_tags(self, host_name, body, **kwargs):
        """Update host tags

        This endpoint allows you to update/replace all tags in an integration source with those supplied in the request.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.update_host_tags(host_name, body, async_req=True)
        >>> result = thread.get()

        Args:
            host_name (str): This endpoint allows you to update/replace all in an integration source with those supplied in the request.
            body (HostTags): Add tags to host

        Keyword Args:
            source (str): [optional] The source of the tags (for example chef, puppet). [Complete list of source attribute values](https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value)
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
            HostTags
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._update_host_tags_endpoint.default_arguments(kwargs)
        kwargs["host_name"] = host_name
        kwargs["body"] = body
        return self._update_host_tags_endpoint.call_with_http_info(**kwargs)
