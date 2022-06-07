# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v2.model.opsgenie_services_response import OpsgenieServicesResponse
from datadog_api_client.v2.model.opsgenie_service_response import OpsgenieServiceResponse
from datadog_api_client.v2.model.opsgenie_service_create_request import OpsgenieServiceCreateRequest
from datadog_api_client.v2.model.opsgenie_service_update_request import OpsgenieServiceUpdateRequest


class OpsgenieIntegrationApi:
    """
    Configure your `Datadog Opsgenie integration <https://docs.datadoghq.com/api/latest/opsgenie-integration>`_
    directly through the Datadog API.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._create_opsgenie_service_endpoint = _Endpoint(
            settings={
                "response_type": (OpsgenieServiceResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/opsgenie/services",
                "operation_id": "create_opsgenie_service",
                "http_method": "POST",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (OpsgenieServiceCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_opsgenie_service_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/opsgenie/services/{integration_service_id}",
                "operation_id": "delete_opsgenie_service",
                "http_method": "DELETE",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "integration_service_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "integration_service_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_opsgenie_service_endpoint = _Endpoint(
            settings={
                "response_type": (OpsgenieServiceResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/opsgenie/services/{integration_service_id}",
                "operation_id": "get_opsgenie_service",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "integration_service_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "integration_service_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_opsgenie_services_endpoint = _Endpoint(
            settings={
                "response_type": (OpsgenieServicesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/opsgenie/services",
                "operation_id": "list_opsgenie_services",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._update_opsgenie_service_endpoint = _Endpoint(
            settings={
                "response_type": (OpsgenieServiceResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/opsgenie/services/{integration_service_id}",
                "operation_id": "update_opsgenie_service",
                "http_method": "PATCH",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "integration_service_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "integration_service_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (OpsgenieServiceUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_opsgenie_service(self, body, **kwargs):
        """Create a new service object.

        Create a new service object in the Opsgenie integration.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.create_opsgenie_service(body, async_req=True)
        >>> result = thread.get()

        :param body: Opsgenie service payload
        :type body: OpsgenieServiceCreateRequest
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
        :rtype: OpsgenieServiceResponse
        """
        kwargs = self._create_opsgenie_service_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._create_opsgenie_service_endpoint.call_with_http_info(**kwargs)

    def delete_opsgenie_service(self, integration_service_id, **kwargs):
        """Delete a single service object.

        Delete a single service object in the Datadog Opsgenie integration.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.delete_opsgenie_service(integration_service_id, async_req=True)
        >>> result = thread.get()

        :param integration_service_id: The UUID of the service.
        :type integration_service_id: str
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
        kwargs = self._delete_opsgenie_service_endpoint.default_arguments(kwargs)
        kwargs["integration_service_id"] = integration_service_id

        return self._delete_opsgenie_service_endpoint.call_with_http_info(**kwargs)

    def get_opsgenie_service(self, integration_service_id, **kwargs):
        """Get a single service object.

        Get a single service from the Datadog Opsgenie integration.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.get_opsgenie_service(integration_service_id, async_req=True)
        >>> result = thread.get()

        :param integration_service_id: The UUID of the service.
        :type integration_service_id: str
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
        :rtype: OpsgenieServiceResponse
        """
        kwargs = self._get_opsgenie_service_endpoint.default_arguments(kwargs)
        kwargs["integration_service_id"] = integration_service_id

        return self._get_opsgenie_service_endpoint.call_with_http_info(**kwargs)

    def list_opsgenie_services(self, **kwargs):
        """Get all service objects.

        Get a list of all services from the Datadog Opsgenie integration.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_opsgenie_services(async_req=True)
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
        :rtype: OpsgenieServicesResponse
        """
        kwargs = self._list_opsgenie_services_endpoint.default_arguments(kwargs)
        return self._list_opsgenie_services_endpoint.call_with_http_info(**kwargs)

    def update_opsgenie_service(self, integration_service_id, body, **kwargs):
        """Update a single service object.

        Update a single service object in the Datadog Opsgenie integration.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.update_opsgenie_service(integration_service_id, body, async_req=True)
        >>> result = thread.get()

        :param integration_service_id: The UUID of the service.
        :type integration_service_id: str
        :param body: Opsgenie service payload.
        :type body: OpsgenieServiceUpdateRequest
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
        :rtype: OpsgenieServiceResponse
        """
        kwargs = self._update_opsgenie_service_endpoint.default_arguments(kwargs)
        kwargs["integration_service_id"] = integration_service_id

        kwargs["body"] = body

        return self._update_opsgenie_service_endpoint.call_with_http_info(**kwargs)
