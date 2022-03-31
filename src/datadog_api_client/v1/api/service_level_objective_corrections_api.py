# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v1.model.slo_correction_list_response import SLOCorrectionListResponse
from datadog_api_client.v1.model.slo_correction_response import SLOCorrectionResponse
from datadog_api_client.v1.model.slo_correction_create_request import SLOCorrectionCreateRequest
from datadog_api_client.v1.model.slo_correction_update_request import SLOCorrectionUpdateRequest


class ServiceLevelObjectiveCorrectionsApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._create_slo_correction_endpoint = _Endpoint(
            settings={
                "response_type": (SLOCorrectionResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/slo/correction",
                "operation_id": "create_slo_correction",
                "http_method": "POST",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (SLOCorrectionCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_slo_correction_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/slo/correction/{slo_correction_id}",
                "operation_id": "delete_slo_correction",
                "http_method": "DELETE",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "slo_correction_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "slo_correction_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_slo_correction_endpoint = _Endpoint(
            settings={
                "response_type": (SLOCorrectionResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/slo/correction/{slo_correction_id}",
                "operation_id": "get_slo_correction",
                "http_method": "GET",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "slo_correction_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "slo_correction_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_slo_correction_endpoint = _Endpoint(
            settings={
                "response_type": (SLOCorrectionListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/slo/correction",
                "operation_id": "list_slo_correction",
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

        self._update_slo_correction_endpoint = _Endpoint(
            settings={
                "response_type": (SLOCorrectionResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/slo/correction/{slo_correction_id}",
                "operation_id": "update_slo_correction",
                "http_method": "PATCH",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "slo_correction_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "slo_correction_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (SLOCorrectionUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_slo_correction(self, body, **kwargs):
        """Create an SLO correction.

        Create an SLO Correction.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.create_slo_correction(body, async_req=True)
        >>> result = thread.get()

        :param body: Create an SLO Correction
        :type body: SLOCorrectionCreateRequest
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
        :rtype: SLOCorrectionResponse
        """
        kwargs = self._create_slo_correction_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._create_slo_correction_endpoint.call_with_http_info(**kwargs)

    def delete_slo_correction(self, slo_correction_id, **kwargs):
        """Delete an SLO correction.

        Permanently delete the specified SLO correction object.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.delete_slo_correction(slo_correction_id, async_req=True)
        >>> result = thread.get()

        :param slo_correction_id: The ID of the SLO correction object.
        :type slo_correction_id: str
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
        kwargs = self._delete_slo_correction_endpoint.default_arguments(kwargs)
        kwargs["slo_correction_id"] = slo_correction_id

        return self._delete_slo_correction_endpoint.call_with_http_info(**kwargs)

    def get_slo_correction(self, slo_correction_id, **kwargs):
        """Get an SLO correction for an SLO.

        Get an SLO correction.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.get_slo_correction(slo_correction_id, async_req=True)
        >>> result = thread.get()

        :param slo_correction_id: The ID of the SLO correction object.
        :type slo_correction_id: str
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
        :rtype: SLOCorrectionResponse
        """
        kwargs = self._get_slo_correction_endpoint.default_arguments(kwargs)
        kwargs["slo_correction_id"] = slo_correction_id

        return self._get_slo_correction_endpoint.call_with_http_info(**kwargs)

    def list_slo_correction(self, **kwargs):
        """Get all SLO corrections.

        Get all Service Level Objective corrections.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_slo_correction(async_req=True)
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
        :rtype: SLOCorrectionListResponse
        """
        kwargs = self._list_slo_correction_endpoint.default_arguments(kwargs)
        return self._list_slo_correction_endpoint.call_with_http_info(**kwargs)

    def update_slo_correction(self, slo_correction_id, body, **kwargs):
        """Update an SLO correction.

        Update the specified SLO correction object object.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.update_slo_correction(slo_correction_id, body, async_req=True)
        >>> result = thread.get()

        :param slo_correction_id: The ID of the SLO correction object.
        :type slo_correction_id: str
        :param body: The edited SLO correction object.
        :type body: SLOCorrectionUpdateRequest
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
        :rtype: SLOCorrectionResponse
        """
        kwargs = self._update_slo_correction_endpoint.default_arguments(kwargs)
        kwargs["slo_correction_id"] = slo_correction_id

        kwargs["body"] = body

        return self._update_slo_correction_endpoint.call_with_http_info(**kwargs)
