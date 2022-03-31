# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v1.model.aws_account_delete_request import AWSAccountDeleteRequest
from datadog_api_client.v1.model.aws_account_list_response import AWSAccountListResponse
from datadog_api_client.v1.model.aws_account_create_response import AWSAccountCreateResponse
from datadog_api_client.v1.model.aws_account import AWSAccount
from datadog_api_client.v1.model.aws_tag_filter_delete_request import AWSTagFilterDeleteRequest
from datadog_api_client.v1.model.aws_tag_filter_list_response import AWSTagFilterListResponse
from datadog_api_client.v1.model.aws_tag_filter_create_request import AWSTagFilterCreateRequest


class AWSIntegrationApi:
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
                "version": "v1",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (AWSAccount,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_aws_tag_filter_endpoint = _Endpoint(
            settings={
                "response_type": (dict,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/integration/aws/filtering",
                "operation_id": "create_aws_tag_filter",
                "http_method": "POST",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (AWSTagFilterCreateRequest,),
                    "location": "body",
                },
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
                "version": "v1",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (AWSAccount,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_aws_account_endpoint = _Endpoint(
            settings={
                "response_type": (dict,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/integration/aws",
                "operation_id": "delete_aws_account",
                "http_method": "DELETE",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (AWSAccountDeleteRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_aws_tag_filter_endpoint = _Endpoint(
            settings={
                "response_type": (dict,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/integration/aws/filtering",
                "operation_id": "delete_aws_tag_filter",
                "http_method": "DELETE",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (AWSTagFilterDeleteRequest,),
                    "location": "body",
                },
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
                "version": "v1",
                "servers": None,
            },
            params_map={},
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
                "version": "v1",
                "servers": None,
            },
            params_map={
                "account_id": {
                    "openapi_types": (str,),
                    "attribute": "account_id",
                    "location": "query",
                },
                "role_name": {
                    "openapi_types": (str,),
                    "attribute": "role_name",
                    "location": "query",
                },
                "access_key_id": {
                    "openapi_types": (str,),
                    "attribute": "access_key_id",
                    "location": "query",
                },
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
                "version": "v1",
                "servers": None,
            },
            params_map={
                "account_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "account_id",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._update_aws_account_endpoint = _Endpoint(
            settings={
                "response_type": (dict,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/integration/aws",
                "operation_id": "update_aws_account",
                "http_method": "PUT",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "account_id": {
                    "openapi_types": (str,),
                    "attribute": "account_id",
                    "location": "query",
                },
                "role_name": {
                    "openapi_types": (str,),
                    "attribute": "role_name",
                    "location": "query",
                },
                "access_key_id": {
                    "openapi_types": (str,),
                    "attribute": "access_key_id",
                    "location": "query",
                },
                "body": {
                    "required": True,
                    "openapi_types": (AWSAccount,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_aws_account(self, body, **kwargs):
        """Create an AWS integration.

        Create a Datadog-Amazon Web Services integration.
        Using the `POST` method updates your integration configuration
        by adding your new configuration to the existing one in your Datadog organization.
        A unique AWS Account ID for role based authentication.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.create_aws_account(body, async_req=True)
        >>> result = thread.get()

        :param body: AWS Request Object
        :type body: AWSAccount
        :param _return_http_data_only: Response data without head status
            code and headers. Default is True.
        :type _return_http_data_only: bool
        :param _preload_content: If False, the urllib3.HTTPResponse object
            will be returned without reading/decoding response data.
            Default is True.
        :type _preload_content: bool
        :param _request_timeout: Timeout setting for this request. If one
            number provided, it will be total request timeout. It can also be a
            pair (tuple) of (connection, read) timeouts.  Default is None.
        :type _request_timeout: float/tuple
        :param _check_input_type: Specifies if type checking should be done one
            the data sent to the server. Default is True.
        :type _check_input_type: bool
        :param _check_return_type: Specifies if type checking should be done
            one the data received from the server. Default is True.
        :type _check_return_type: bool
        :param _host_index: Specifies the index of the server that we want to
            use. Default is read from the configuration.
        :type _host_index: int/None
        :param async_req: Execute request asynchronously.
        :type async_req: bool

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: AWSAccountCreateResponse
        """
        kwargs = self._create_aws_account_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._create_aws_account_endpoint.call_with_http_info(**kwargs)

    def create_aws_tag_filter(self, body, **kwargs):
        """Set an AWS tag filter.

        Set an AWS tag filter.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.create_aws_tag_filter(body, async_req=True)
        >>> result = thread.get()

        :param body: Set an AWS tag filter using an `aws_account_identifier`, `namespace`, and filtering string.
            Namespace options are `application_elb`, `elb`, `lambda`, `network_elb`, `rds`, `sqs`, and `custom`.
        :type body: AWSTagFilterCreateRequest
        :param _return_http_data_only: Response data without head status
            code and headers. Default is True.
        :type _return_http_data_only: bool
        :param _preload_content: If False, the urllib3.HTTPResponse object
            will be returned without reading/decoding response data.
            Default is True.
        :type _preload_content: bool
        :param _request_timeout: Timeout setting for this request. If one
            number provided, it will be total request timeout. It can also be a
            pair (tuple) of (connection, read) timeouts.  Default is None.
        :type _request_timeout: float/tuple
        :param _check_input_type: Specifies if type checking should be done one
            the data sent to the server. Default is True.
        :type _check_input_type: bool
        :param _check_return_type: Specifies if type checking should be done
            one the data received from the server. Default is True.
        :type _check_return_type: bool
        :param _host_index: Specifies the index of the server that we want to
            use. Default is read from the configuration.
        :type _host_index: int/None
        :param async_req: Execute request asynchronously.
        :type async_req: bool

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: dict
        """
        kwargs = self._create_aws_tag_filter_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._create_aws_tag_filter_endpoint.call_with_http_info(**kwargs)

    def create_new_aws_external_id(self, body, **kwargs):
        """Generate a new external ID.

        Generate a new AWS external ID for a given AWS account ID and role name pair.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.create_new_aws_external_id(body, async_req=True)
        >>> result = thread.get()

        :param body: Your Datadog role delegation name.
            For more information about your AWS account Role name,
            see the [Datadog AWS integration configuration info](https://docs.datadoghq.com/integrations/amazon_web_services/#setup).
        :type body: AWSAccount
        :param _return_http_data_only: Response data without head status
            code and headers. Default is True.
        :type _return_http_data_only: bool
        :param _preload_content: If False, the urllib3.HTTPResponse object
            will be returned without reading/decoding response data.
            Default is True.
        :type _preload_content: bool
        :param _request_timeout: Timeout setting for this request. If one
            number provided, it will be total request timeout. It can also be a
            pair (tuple) of (connection, read) timeouts.  Default is None.
        :type _request_timeout: float/tuple
        :param _check_input_type: Specifies if type checking should be done one
            the data sent to the server. Default is True.
        :type _check_input_type: bool
        :param _check_return_type: Specifies if type checking should be done
            one the data received from the server. Default is True.
        :type _check_return_type: bool
        :param _host_index: Specifies the index of the server that we want to
            use. Default is read from the configuration.
        :type _host_index: int/None
        :param async_req: Execute request asynchronously.
        :type async_req: bool

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: AWSAccountCreateResponse
        """
        kwargs = self._create_new_aws_external_id_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._create_new_aws_external_id_endpoint.call_with_http_info(**kwargs)

    def delete_aws_account(self, body, **kwargs):
        """Delete an AWS integration.

        Delete a Datadog-AWS integration matching the specified `account_id` and `role_name parameters`.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.delete_aws_account(body, async_req=True)
        >>> result = thread.get()

        :param body: AWS request object
        :type body: AWSAccountDeleteRequest
        :param _return_http_data_only: Response data without head status
            code and headers. Default is True.
        :type _return_http_data_only: bool
        :param _preload_content: If False, the urllib3.HTTPResponse object
            will be returned without reading/decoding response data.
            Default is True.
        :type _preload_content: bool
        :param _request_timeout: Timeout setting for this request. If one
            number provided, it will be total request timeout. It can also be a
            pair (tuple) of (connection, read) timeouts.  Default is None.
        :type _request_timeout: float/tuple
        :param _check_input_type: Specifies if type checking should be done one
            the data sent to the server. Default is True.
        :type _check_input_type: bool
        :param _check_return_type: Specifies if type checking should be done
            one the data received from the server. Default is True.
        :type _check_return_type: bool
        :param _host_index: Specifies the index of the server that we want to
            use. Default is read from the configuration.
        :type _host_index: int/None
        :param async_req: Execute request asynchronously.
        :type async_req: bool

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: dict
        """
        kwargs = self._delete_aws_account_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._delete_aws_account_endpoint.call_with_http_info(**kwargs)

    def delete_aws_tag_filter(self, body, **kwargs):
        """Delete a tag filtering entry.

        Delete a tag filtering entry.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.delete_aws_tag_filter(body, async_req=True)
        >>> result = thread.get()

        :param body: Delete a tag filtering entry for a given AWS account and `dd-aws` namespace.
        :type body: AWSTagFilterDeleteRequest
        :param _return_http_data_only: Response data without head status
            code and headers. Default is True.
        :type _return_http_data_only: bool
        :param _preload_content: If False, the urllib3.HTTPResponse object
            will be returned without reading/decoding response data.
            Default is True.
        :type _preload_content: bool
        :param _request_timeout: Timeout setting for this request. If one
            number provided, it will be total request timeout. It can also be a
            pair (tuple) of (connection, read) timeouts.  Default is None.
        :type _request_timeout: float/tuple
        :param _check_input_type: Specifies if type checking should be done one
            the data sent to the server. Default is True.
        :type _check_input_type: bool
        :param _check_return_type: Specifies if type checking should be done
            one the data received from the server. Default is True.
        :type _check_return_type: bool
        :param _host_index: Specifies the index of the server that we want to
            use. Default is read from the configuration.
        :type _host_index: int/None
        :param async_req: Execute request asynchronously.
        :type async_req: bool

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: dict
        """
        kwargs = self._delete_aws_tag_filter_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._delete_aws_tag_filter_endpoint.call_with_http_info(**kwargs)

    def list_available_aws_namespaces(self, **kwargs):
        """List namespace rules.

        List all namespace rules for a given Datadog-AWS integration. This endpoint takes no arguments.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_available_aws_namespaces(async_req=True)
        >>> result = thread.get()

        :param _return_http_data_only: Response data without head status
            code and headers. Default is True.
        :type _return_http_data_only: bool
        :param _preload_content: If False, the urllib3.HTTPResponse object
            will be returned without reading/decoding response data.
            Default is True.
        :type _preload_content: bool
        :param _request_timeout: Timeout setting for this request. If one
            number provided, it will be total request timeout. It can also be a
            pair (tuple) of (connection, read) timeouts.  Default is None.
        :type _request_timeout: float/tuple
        :param _check_input_type: Specifies if type checking should be done one
            the data sent to the server. Default is True.
        :type _check_input_type: bool
        :param _check_return_type: Specifies if type checking should be done
            one the data received from the server. Default is True.
        :type _check_return_type: bool
        :param _host_index: Specifies the index of the server that we want to
            use. Default is read from the configuration.
        :type _host_index: int/None
        :param async_req: Execute request asynchronously.
        :type async_req: bool

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: [str]
        """
        kwargs = self._list_available_aws_namespaces_endpoint.default_arguments(kwargs)
        return self._list_available_aws_namespaces_endpoint.call_with_http_info(**kwargs)

    def list_aws_accounts(self, **kwargs):
        """List all AWS integrations.

        List all Datadog-AWS integrations available in your Datadog organization.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_aws_accounts(async_req=True)
        >>> result = thread.get()

        :param account_id: Only return AWS accounts that matches this `account_id`.
        :type account_id: str, optional
        :param role_name: Only return AWS accounts that matches this role_name.
        :type role_name: str, optional
        :param access_key_id: Only return AWS accounts that matches this `access_key_id`.
        :type access_key_id: str, optional
        :param _return_http_data_only: Response data without head status
            code and headers. Default is True.
        :type _return_http_data_only: bool
        :param _preload_content: If False, the urllib3.HTTPResponse object
            will be returned without reading/decoding response data.
            Default is True.
        :type _preload_content: bool
        :param _request_timeout: Timeout setting for this request. If one
            number provided, it will be total request timeout. It can also be a
            pair (tuple) of (connection, read) timeouts.  Default is None.
        :type _request_timeout: float/tuple
        :param _check_input_type: Specifies if type checking should be done one
            the data sent to the server. Default is True.
        :type _check_input_type: bool
        :param _check_return_type: Specifies if type checking should be done
            one the data received from the server. Default is True.
        :type _check_return_type: bool
        :param _host_index: Specifies the index of the server that we want to
            use. Default is read from the configuration.
        :type _host_index: int/None
        :param async_req: Execute request asynchronously.
        :type async_req: bool

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: AWSAccountListResponse
        """
        kwargs = self._list_aws_accounts_endpoint.default_arguments(kwargs)
        return self._list_aws_accounts_endpoint.call_with_http_info(**kwargs)

    def list_aws_tag_filters(self, account_id, **kwargs):
        """Get all AWS tag filters.

        Get all AWS tag filters.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_aws_tag_filters(account_id, async_req=True)
        >>> result = thread.get()

        :param account_id: Only return AWS filters that matches this `account_id`.
        :type account_id: str
        :param _return_http_data_only: Response data without head status
            code and headers. Default is True.
        :type _return_http_data_only: bool
        :param _preload_content: If False, the urllib3.HTTPResponse object
            will be returned without reading/decoding response data.
            Default is True.
        :type _preload_content: bool
        :param _request_timeout: Timeout setting for this request. If one
            number provided, it will be total request timeout. It can also be a
            pair (tuple) of (connection, read) timeouts.  Default is None.
        :type _request_timeout: float/tuple
        :param _check_input_type: Specifies if type checking should be done one
            the data sent to the server. Default is True.
        :type _check_input_type: bool
        :param _check_return_type: Specifies if type checking should be done
            one the data received from the server. Default is True.
        :type _check_return_type: bool
        :param _host_index: Specifies the index of the server that we want to
            use. Default is read from the configuration.
        :type _host_index: int/None
        :param async_req: Execute request asynchronously.
        :type async_req: bool

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: AWSTagFilterListResponse
        """
        kwargs = self._list_aws_tag_filters_endpoint.default_arguments(kwargs)
        kwargs["account_id"] = account_id

        return self._list_aws_tag_filters_endpoint.call_with_http_info(**kwargs)

    def update_aws_account(self, body, **kwargs):
        """Update an AWS integration.

        Update a Datadog-Amazon Web Services integration.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.update_aws_account(body, async_req=True)
        >>> result = thread.get()

        :param body: AWS request object
        :type body: AWSAccount
        :param account_id: Only return AWS accounts that matches this `account_id`.
        :type account_id: str, optional
        :param role_name: Only return AWS accounts that match this `role_name`.
            Required if `account_id` is specified.
        :type role_name: str, optional
        :param access_key_id: Only return AWS accounts that matches this `access_key_id`.
            Required if none of the other two options are specified.
        :type access_key_id: str, optional
        :param _return_http_data_only: Response data without head status
            code and headers. Default is True.
        :type _return_http_data_only: bool
        :param _preload_content: If False, the urllib3.HTTPResponse object
            will be returned without reading/decoding response data.
            Default is True.
        :type _preload_content: bool
        :param _request_timeout: Timeout setting for this request. If one
            number provided, it will be total request timeout. It can also be a
            pair (tuple) of (connection, read) timeouts.  Default is None.
        :type _request_timeout: float/tuple
        :param _check_input_type: Specifies if type checking should be done one
            the data sent to the server. Default is True.
        :type _check_input_type: bool
        :param _check_return_type: Specifies if type checking should be done
            one the data received from the server. Default is True.
        :type _check_return_type: bool
        :param _host_index: Specifies the index of the server that we want to
            use. Default is read from the configuration.
        :type _host_index: int/None
        :param async_req: Execute request asynchronously.
        :type async_req: bool

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: dict
        """
        kwargs = self._update_aws_account_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._update_aws_account_endpoint.call_with_http_info(**kwargs)
