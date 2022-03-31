# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v1.model.webhooks_integration_custom_variable_response import (
    WebhooksIntegrationCustomVariableResponse,
)
from datadog_api_client.v1.model.webhooks_integration_custom_variable import WebhooksIntegrationCustomVariable
from datadog_api_client.v1.model.webhooks_integration_custom_variable_update_request import (
    WebhooksIntegrationCustomVariableUpdateRequest,
)
from datadog_api_client.v1.model.webhooks_integration import WebhooksIntegration
from datadog_api_client.v1.model.webhooks_integration_update_request import WebhooksIntegrationUpdateRequest


class WebhooksIntegrationApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._create_webhooks_integration_endpoint = _Endpoint(
            settings={
                "response_type": (WebhooksIntegration,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/integration/webhooks/configuration/webhooks",
                "operation_id": "create_webhooks_integration",
                "http_method": "POST",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (WebhooksIntegration,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_webhooks_integration_custom_variable_endpoint = _Endpoint(
            settings={
                "response_type": (WebhooksIntegrationCustomVariableResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/integration/webhooks/configuration/custom-variables",
                "operation_id": "create_webhooks_integration_custom_variable",
                "http_method": "POST",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (WebhooksIntegrationCustomVariable,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_webhooks_integration_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/integration/webhooks/configuration/webhooks/{webhook_name}",
                "operation_id": "delete_webhooks_integration",
                "http_method": "DELETE",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "webhook_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "webhook_name",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._delete_webhooks_integration_custom_variable_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name}",
                "operation_id": "delete_webhooks_integration_custom_variable",
                "http_method": "DELETE",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "custom_variable_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "custom_variable_name",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_webhooks_integration_endpoint = _Endpoint(
            settings={
                "response_type": (WebhooksIntegration,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/integration/webhooks/configuration/webhooks/{webhook_name}",
                "operation_id": "get_webhooks_integration",
                "http_method": "GET",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "webhook_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "webhook_name",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_webhooks_integration_custom_variable_endpoint = _Endpoint(
            settings={
                "response_type": (WebhooksIntegrationCustomVariableResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name}",
                "operation_id": "get_webhooks_integration_custom_variable",
                "http_method": "GET",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "custom_variable_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "custom_variable_name",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._update_webhooks_integration_endpoint = _Endpoint(
            settings={
                "response_type": (WebhooksIntegration,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/integration/webhooks/configuration/webhooks/{webhook_name}",
                "operation_id": "update_webhooks_integration",
                "http_method": "PUT",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "webhook_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "webhook_name",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (WebhooksIntegrationUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_webhooks_integration_custom_variable_endpoint = _Endpoint(
            settings={
                "response_type": (WebhooksIntegrationCustomVariableResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name}",
                "operation_id": "update_webhooks_integration_custom_variable",
                "http_method": "PUT",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "custom_variable_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "custom_variable_name",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (WebhooksIntegrationCustomVariableUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_webhooks_integration(self, body, **kwargs):
        """Create a webhooks integration.

        Creates an endpoint with the name `<WEBHOOK_NAME>`.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.create_webhooks_integration(body, async_req=True)
        >>> result = thread.get()

        :param body: Create a webhooks integration request body.
        :type body: WebhooksIntegration
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
        :rtype: WebhooksIntegration
        """
        kwargs = self._create_webhooks_integration_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._create_webhooks_integration_endpoint.call_with_http_info(**kwargs)

    def create_webhooks_integration_custom_variable(self, body, **kwargs):
        """Create a custom variable.

        Creates an endpoint with the name `<CUSTOM_VARIABLE_NAME>`.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.create_webhooks_integration_custom_variable(body, async_req=True)
        >>> result = thread.get()

        :param body: Define a custom variable request body.
        :type body: WebhooksIntegrationCustomVariable
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
        :rtype: WebhooksIntegrationCustomVariableResponse
        """
        kwargs = self._create_webhooks_integration_custom_variable_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._create_webhooks_integration_custom_variable_endpoint.call_with_http_info(**kwargs)

    def delete_webhooks_integration(self, webhook_name, **kwargs):
        """Delete a webhook.

        Deletes the endpoint with the name `<WEBHOOK NAME>`.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.delete_webhooks_integration(webhook_name, async_req=True)
        >>> result = thread.get()

        :param webhook_name: The name of the webhook.
        :type webhook_name: str
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
        :rtype: None
        """
        kwargs = self._delete_webhooks_integration_endpoint.default_arguments(kwargs)
        kwargs["webhook_name"] = webhook_name

        return self._delete_webhooks_integration_endpoint.call_with_http_info(**kwargs)

    def delete_webhooks_integration_custom_variable(self, custom_variable_name, **kwargs):
        """Delete a custom variable.

        Deletes the endpoint with the name `<CUSTOM_VARIABLE_NAME>`.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.delete_webhooks_integration_custom_variable(custom_variable_name, async_req=True)
        >>> result = thread.get()

        :param custom_variable_name: The name of the custom variable.
        :type custom_variable_name: str
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
        :rtype: None
        """
        kwargs = self._delete_webhooks_integration_custom_variable_endpoint.default_arguments(kwargs)
        kwargs["custom_variable_name"] = custom_variable_name

        return self._delete_webhooks_integration_custom_variable_endpoint.call_with_http_info(**kwargs)

    def get_webhooks_integration(self, webhook_name, **kwargs):
        """Get a webhook integration.

        Gets the content of the webhook with the name `<WEBHOOK_NAME>`.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.get_webhooks_integration(webhook_name, async_req=True)
        >>> result = thread.get()

        :param webhook_name: The name of the webhook.
        :type webhook_name: str
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
        :rtype: WebhooksIntegration
        """
        kwargs = self._get_webhooks_integration_endpoint.default_arguments(kwargs)
        kwargs["webhook_name"] = webhook_name

        return self._get_webhooks_integration_endpoint.call_with_http_info(**kwargs)

    def get_webhooks_integration_custom_variable(self, custom_variable_name, **kwargs):
        """Get a custom variable.

        Shows the content of the custom variable with the name `<CUSTOM_VARIABLE_NAME>`.

        If the custom variable is secret, the value does not return in the
        response payload.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.get_webhooks_integration_custom_variable(custom_variable_name, async_req=True)
        >>> result = thread.get()

        :param custom_variable_name: The name of the custom variable.
        :type custom_variable_name: str
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
        :rtype: WebhooksIntegrationCustomVariableResponse
        """
        kwargs = self._get_webhooks_integration_custom_variable_endpoint.default_arguments(kwargs)
        kwargs["custom_variable_name"] = custom_variable_name

        return self._get_webhooks_integration_custom_variable_endpoint.call_with_http_info(**kwargs)

    def update_webhooks_integration(self, webhook_name, body, **kwargs):
        """Update a webhook.

        Updates the endpoint with the name `<WEBHOOK_NAME>`.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.update_webhooks_integration(webhook_name, body, async_req=True)
        >>> result = thread.get()

        :param webhook_name: The name of the webhook.
        :type webhook_name: str
        :param body: Update an existing Datadog-Webhooks integration.
        :type body: WebhooksIntegrationUpdateRequest
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
        :rtype: WebhooksIntegration
        """
        kwargs = self._update_webhooks_integration_endpoint.default_arguments(kwargs)
        kwargs["webhook_name"] = webhook_name

        kwargs["body"] = body

        return self._update_webhooks_integration_endpoint.call_with_http_info(**kwargs)

    def update_webhooks_integration_custom_variable(self, custom_variable_name, body, **kwargs):
        """Update a custom variable.

        Updates the endpoint with the name `<CUSTOM_VARIABLE_NAME>`.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.update_webhooks_integration_custom_variable(custom_variable_name, body, async_req=True)
        >>> result = thread.get()

        :param custom_variable_name: The name of the custom variable.
        :type custom_variable_name: str
        :param body: Update an existing custom variable request body.
        :type body: WebhooksIntegrationCustomVariableUpdateRequest
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
        :rtype: WebhooksIntegrationCustomVariableResponse
        """
        kwargs = self._update_webhooks_integration_custom_variable_endpoint.default_arguments(kwargs)
        kwargs["custom_variable_name"] = custom_variable_name

        kwargs["body"] = body

        return self._update_webhooks_integration_custom_variable_endpoint.call_with_http_info(**kwargs)
