# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import re  # noqa: F401
import sys  # noqa: F401

from datadog_api_client.v1.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v1.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)
from datadog_api_client.v1.model.api_error_response import APIErrorResponse
from datadog_api_client.v1.model.aws_account import AWSAccount
from datadog_api_client.v1.model.aws_account_create_response import AWSAccountCreateResponse
from datadog_api_client.v1.model.aws_account_list_response import AWSAccountListResponse
from datadog_api_client.v1.model.aws_tag_filter_create_request import AWSTagFilterCreateRequest
from datadog_api_client.v1.model.aws_tag_filter_delete_request import AWSTagFilterDeleteRequest
from datadog_api_client.v1.model.aws_tag_filter_list_response import AWSTagFilterListResponse


class AWSIntegrationApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._create_aws_account_endpoint = _Endpoint(
            settings={
                "response_type": (AWSAccountCreateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/integration/aws",
                "operation_id": "create_aws_account",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "body",
                ],
                "required": [
                    "body",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "body": (AWSAccount,),
                },
                "attribute_map": {},
                "location_map": {
                    "body": "body",
                },
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_aws_tag_filter_endpoint = _Endpoint(
            settings={
                "response_type": ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/integration/aws/filtering",
                "operation_id": "create_aws_tag_filter",
                "http_method": "POST",
                "servers": [
                    {
                        "url": "https://{subdomain}.{site}",
                        "description": "No description provided",
                        "variables": {
                            "site": {
                                "description": "The regional site for our customers.",
                                "default_value": "datadoghq.com",
                                "enum_values": ["datadoghq.com"],
                            },
                            "subdomain": {
                                "description": "The subdomain where the API is deployed.",
                                "default_value": "api",
                            },
                        },
                    },
                    {
                        "url": "{protocol}://{name}",
                        "description": "No description provided",
                        "variables": {
                            "name": {
                                "description": "Full site DNS name.",
                                "default_value": "api.datadoghq.com",
                            },
                            "protocol": {
                                "description": "The protocol for accessing the API.",
                                "default_value": "https",
                            },
                        },
                    },
                    {
                        "url": "https://{subdomain}.{site}",
                        "description": "No description provided",
                        "variables": {
                            "site": {
                                "description": "Any Datadog deployment.",
                                "default_value": "datadoghq.com",
                            },
                            "subdomain": {
                                "description": "The subdomain where the API is deployed.",
                                "default_value": "api",
                            },
                        },
                    },
                ],
            },
            params_map={
                "all": [
                    "body",
                ],
                "required": [
                    "body",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "body": (AWSTagFilterCreateRequest,),
                },
                "attribute_map": {},
                "location_map": {
                    "body": "body",
                },
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_new_aws_external_id_endpoint = _Endpoint(
            settings={
                "response_type": (AWSAccountCreateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/integration/aws/generate_new_external_id",
                "operation_id": "create_new_aws_external_id",
                "http_method": "PUT",
                "servers": None,
            },
            params_map={
                "all": [
                    "body",
                ],
                "required": [
                    "body",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "body": (AWSAccount,),
                },
                "attribute_map": {},
                "location_map": {
                    "body": "body",
                },
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_aws_account_endpoint = _Endpoint(
            settings={
                "response_type": ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/integration/aws",
                "operation_id": "delete_aws_account",
                "http_method": "DELETE",
                "servers": None,
            },
            params_map={
                "all": [
                    "body",
                ],
                "required": [
                    "body",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "body": (AWSAccount,),
                },
                "attribute_map": {},
                "location_map": {
                    "body": "body",
                },
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_aws_tag_filter_endpoint = _Endpoint(
            settings={
                "response_type": ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/integration/aws/filtering",
                "operation_id": "delete_aws_tag_filter",
                "http_method": "DELETE",
                "servers": [
                    {
                        "url": "https://{subdomain}.{site}",
                        "description": "No description provided",
                        "variables": {
                            "site": {
                                "description": "The regional site for our customers.",
                                "default_value": "datadoghq.com",
                                "enum_values": ["datadoghq.com"],
                            },
                            "subdomain": {
                                "description": "The subdomain where the API is deployed.",
                                "default_value": "api",
                            },
                        },
                    },
                    {
                        "url": "{protocol}://{name}",
                        "description": "No description provided",
                        "variables": {
                            "name": {
                                "description": "Full site DNS name.",
                                "default_value": "api.datadoghq.com",
                            },
                            "protocol": {
                                "description": "The protocol for accessing the API.",
                                "default_value": "https",
                            },
                        },
                    },
                    {
                        "url": "https://{subdomain}.{site}",
                        "description": "No description provided",
                        "variables": {
                            "site": {
                                "description": "Any Datadog deployment.",
                                "default_value": "datadoghq.com",
                            },
                            "subdomain": {
                                "description": "The subdomain where the API is deployed.",
                                "default_value": "api",
                            },
                        },
                    },
                ],
            },
            params_map={
                "all": [
                    "body",
                ],
                "required": [
                    "body",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "body": (AWSTagFilterDeleteRequest,),
                },
                "attribute_map": {},
                "location_map": {
                    "body": "body",
                },
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._list_available_aws_namespaces_endpoint = _Endpoint(
            settings={
                "response_type": ([str],),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/integration/aws/available_namespace_rules",
                "operation_id": "list_available_aws_namespaces",
                "http_method": "GET",
                "servers": None,
            },
            params_map={"all": [], "required": [], "nullable": [], "enum": [], "validation": []},
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {},
                "attribute_map": {},
                "location_map": {},
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_aws_accounts_endpoint = _Endpoint(
            settings={
                "response_type": (AWSAccountListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/integration/aws",
                "operation_id": "list_aws_accounts",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "account_id",
                    "role_name",
                    "access_key_id",
                ],
                "required": [],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "account_id": (str,),
                    "role_name": (str,),
                    "access_key_id": (str,),
                },
                "attribute_map": {
                    "account_id": "account_id",
                    "role_name": "role_name",
                    "access_key_id": "access_key_id",
                },
                "location_map": {
                    "account_id": "query",
                    "role_name": "query",
                    "access_key_id": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_aws_tag_filters_endpoint = _Endpoint(
            settings={
                "response_type": (AWSTagFilterListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/integration/aws/filtering",
                "operation_id": "list_aws_tag_filters",
                "http_method": "GET",
                "servers": [
                    {
                        "url": "https://{subdomain}.{site}",
                        "description": "No description provided",
                        "variables": {
                            "site": {
                                "description": "The regional site for our customers.",
                                "default_value": "datadoghq.com",
                                "enum_values": ["datadoghq.com"],
                            },
                            "subdomain": {
                                "description": "The subdomain where the API is deployed.",
                                "default_value": "api",
                            },
                        },
                    },
                    {
                        "url": "{protocol}://{name}",
                        "description": "No description provided",
                        "variables": {
                            "name": {
                                "description": "Full site DNS name.",
                                "default_value": "api.datadoghq.com",
                            },
                            "protocol": {
                                "description": "The protocol for accessing the API.",
                                "default_value": "https",
                            },
                        },
                    },
                    {
                        "url": "https://{subdomain}.{site}",
                        "description": "No description provided",
                        "variables": {
                            "site": {
                                "description": "Any Datadog deployment.",
                                "default_value": "datadoghq.com",
                            },
                            "subdomain": {
                                "description": "The subdomain where the API is deployed.",
                                "default_value": "api",
                            },
                        },
                    },
                ],
            },
            params_map={
                "all": [
                    "account_id",
                ],
                "required": [
                    "account_id",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "account_id": (str,),
                },
                "attribute_map": {
                    "account_id": "account_id",
                },
                "location_map": {
                    "account_id": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._update_aws_account_endpoint = _Endpoint(
            settings={
                "response_type": ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/integration/aws",
                "operation_id": "update_aws_account",
                "http_method": "PUT",
                "servers": None,
            },
            params_map={
                "all": [
                    "body",
                    "account_id",
                    "role_name",
                    "access_key_id",
                ],
                "required": [
                    "body",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "body": (AWSAccount,),
                    "account_id": (str,),
                    "role_name": (str,),
                    "access_key_id": (str,),
                },
                "attribute_map": {
                    "account_id": "account_id",
                    "role_name": "role_name",
                    "access_key_id": "access_key_id",
                },
                "location_map": {
                    "body": "body",
                    "account_id": "query",
                    "role_name": "query",
                    "access_key_id": "query",
                },
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_aws_account(self, body, **kwargs):
        """Create an AWS integration  # noqa: E501

        Create a Datadog-Amazon Web Services integration. Using the `POST` method updates your integration configuration by adding your new configuration to the existing one in your Datadog organization. A unique AWS Account ID for role based authentication.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_aws_account(body, async_req=True)
        >>> result = thread.get()

        Args:
            body (AWSAccount): AWS Request Object

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
            AWSAccountCreateResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._create_aws_account_endpoint.default_arguments(kwargs)
        kwargs["body"] = body
        return self._create_aws_account_endpoint.call_with_http_info(**kwargs)

    def create_aws_tag_filter(self, body, **kwargs):
        """Set an AWS tag filter  # noqa: E501

        Set an AWS tag filter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_aws_tag_filter(body, async_req=True)
        >>> result = thread.get()

        Args:
            body (AWSTagFilterCreateRequest): Set an AWS tag filter using an `aws_account_identifier`, `namespace`, and filtering string. Namespace options are `application_elb`, `elb`, `lambda`, `network_elb`, `rds`, `sqs`, and `custom`.

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
            {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._create_aws_tag_filter_endpoint.default_arguments(kwargs)
        kwargs["body"] = body
        return self._create_aws_tag_filter_endpoint.call_with_http_info(**kwargs)

    def create_new_aws_external_id(self, body, **kwargs):
        """Generate a new external ID  # noqa: E501

        Generate a new AWS external ID for a given AWS account ID and role name pair.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_new_aws_external_id(body, async_req=True)
        >>> result = thread.get()

        Args:
            body (AWSAccount): Your Datadog role delegation name. For more information about your AWS account Role name, see the [Datadog AWS integration configuration info](https://github.com/DataDog/documentation/blob/master/integrations/amazon_web_services/#installation).

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
            AWSAccountCreateResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._create_new_aws_external_id_endpoint.default_arguments(kwargs)
        kwargs["body"] = body
        return self._create_new_aws_external_id_endpoint.call_with_http_info(**kwargs)

    def delete_aws_account(self, body, **kwargs):
        """Delete an AWS integration  # noqa: E501

        Delete a Datadog-AWS integration matching the specified `account_id` and `role_name parameters`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_aws_account(body, async_req=True)
        >>> result = thread.get()

        Args:
            body (AWSAccount): AWS request object

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
            {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._delete_aws_account_endpoint.default_arguments(kwargs)
        kwargs["body"] = body
        return self._delete_aws_account_endpoint.call_with_http_info(**kwargs)

    def delete_aws_tag_filter(self, body, **kwargs):
        """Delete a tag filtering entry  # noqa: E501

        Delete a tag filtering entry.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_aws_tag_filter(body, async_req=True)
        >>> result = thread.get()

        Args:
            body (AWSTagFilterDeleteRequest): Delete a tag filtering entry for a given AWS account and `dd-aws` namespace.

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
            {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._delete_aws_tag_filter_endpoint.default_arguments(kwargs)
        kwargs["body"] = body
        return self._delete_aws_tag_filter_endpoint.call_with_http_info(**kwargs)

    def list_available_aws_namespaces(self, **kwargs):
        """List namespace rules  # noqa: E501

        List all namespace rules for a given Datadog-AWS integration. This endpoint takes no arguments.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_available_aws_namespaces(async_req=True)
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
            [str]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._list_available_aws_namespaces_endpoint.default_arguments(kwargs)
        return self._list_available_aws_namespaces_endpoint.call_with_http_info(**kwargs)

    def list_aws_accounts(self, **kwargs):
        """List all AWS integrations  # noqa: E501

        List all Datadog-AWS integrations available in your Datadog organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_aws_accounts(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            account_id (str): Only return AWS accounts that matches this `account_id`.. [optional]
            role_name (str): Only return AWS accounts that matches this role_name.. [optional]
            access_key_id (str): Only return AWS accounts that matches this `access_key_id`.. [optional]
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
            AWSAccountListResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._list_aws_accounts_endpoint.default_arguments(kwargs)
        return self._list_aws_accounts_endpoint.call_with_http_info(**kwargs)

    def list_aws_tag_filters(self, account_id, **kwargs):
        """Get all AWS tag filters  # noqa: E501

        Get all AWS tag filters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_aws_tag_filters(account_id, async_req=True)
        >>> result = thread.get()

        Args:
            account_id (str): Only return AWS filters that matches this `account_id`.

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
            AWSTagFilterListResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._list_aws_tag_filters_endpoint.default_arguments(kwargs)
        kwargs["account_id"] = account_id
        return self._list_aws_tag_filters_endpoint.call_with_http_info(**kwargs)

    def update_aws_account(self, body, **kwargs):
        """Update an AWS integration  # noqa: E501

        Update a Datadog-Amazon Web Services integration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_aws_account(body, async_req=True)
        >>> result = thread.get()

        Args:
            body (AWSAccount): AWS request object

        Keyword Args:
            account_id (str): Only return AWS accounts that matches this `account_id`.. [optional]
            role_name (str): Only return AWS accounts that match this `role_name`. Required if `account_id` is specified.. [optional]
            access_key_id (str): Only return AWS accounts that matches this `access_key_id`. Required if none of the other two options are specified.. [optional]
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
            {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._update_aws_account_endpoint.default_arguments(kwargs)
        kwargs["body"] = body
        return self._update_aws_account_endpoint.call_with_http_info(**kwargs)
