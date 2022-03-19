# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v2.model.authn_mappings_response import AuthNMappingsResponse
from datadog_api_client.v2.model.authn_mappings_sort import AuthNMappingsSort
from datadog_api_client.v2.model.authn_mapping_response import AuthNMappingResponse
from datadog_api_client.v2.model.authn_mapping_create_request import AuthNMappingCreateRequest
from datadog_api_client.v2.model.authn_mapping_update_request import AuthNMappingUpdateRequest


class AuthNMappingsApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._create_authn_mapping_endpoint = _Endpoint(
            settings={
                "response_type": (AuthNMappingResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/authn_mappings",
                "operation_id": "create_authn_mapping",
                "http_method": "POST",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (AuthNMappingCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_authn_mapping_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/authn_mappings/{authn_mapping_id}",
                "operation_id": "delete_authn_mapping",
                "http_method": "DELETE",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "authn_mapping_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "authn_mapping_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_authn_mapping_endpoint = _Endpoint(
            settings={
                "response_type": (AuthNMappingResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/authn_mappings/{authn_mapping_id}",
                "operation_id": "get_authn_mapping",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "authn_mapping_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "authn_mapping_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_authn_mappings_endpoint = _Endpoint(
            settings={
                "response_type": (AuthNMappingsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/authn_mappings",
                "operation_id": "list_authn_mappings",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "page_size": {
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "page_number": {
                    "openapi_types": (int,),
                    "attribute": "page[number]",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (AuthNMappingsSort,),
                    "attribute": "sort",
                    "location": "query",
                },
                "include": {
                    "openapi_types": ([str],),
                    "attribute": "include",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter": {
                    "openapi_types": (str,),
                    "attribute": "filter",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._update_authn_mapping_endpoint = _Endpoint(
            settings={
                "response_type": (AuthNMappingResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/authn_mappings/{authn_mapping_id}",
                "operation_id": "update_authn_mapping",
                "http_method": "PATCH",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "authn_mapping_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "authn_mapping_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (AuthNMappingUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_authn_mapping(self, body, **kwargs):
        """Create an AuthN Mapping.

        Create an AuthN Mapping.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.create_authn_mapping(body, async_req=True)
        >>> result = thread.get()

        :type body: AuthNMappingCreateRequest
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
        :rtype: AuthNMappingResponse
        """
        kwargs = self._create_authn_mapping_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._create_authn_mapping_endpoint.call_with_http_info(**kwargs)

    def delete_authn_mapping(self, authn_mapping_id, **kwargs):
        """Delete an AuthN Mapping.

        Delete an AuthN Mapping specified by AuthN Mapping UUID.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.delete_authn_mapping(authn_mapping_id, async_req=True)
        >>> result = thread.get()

        :param authn_mapping_id: The UUID of the AuthN Mapping.
        :type authn_mapping_id: str
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
        kwargs = self._delete_authn_mapping_endpoint.default_arguments(kwargs)
        kwargs["authn_mapping_id"] = authn_mapping_id

        return self._delete_authn_mapping_endpoint.call_with_http_info(**kwargs)

    def get_authn_mapping(self, authn_mapping_id, **kwargs):
        """Get an AuthN Mapping by UUID.

        Get an AuthN Mapping specified by the AuthN Mapping UUID.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.get_authn_mapping(authn_mapping_id, async_req=True)
        >>> result = thread.get()

        :param authn_mapping_id: The UUID of the AuthN Mapping.
        :type authn_mapping_id: str
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
        :rtype: AuthNMappingResponse
        """
        kwargs = self._get_authn_mapping_endpoint.default_arguments(kwargs)
        kwargs["authn_mapping_id"] = authn_mapping_id

        return self._get_authn_mapping_endpoint.call_with_http_info(**kwargs)

    def list_authn_mappings(self, **kwargs):
        """List all AuthN Mappings.

        List all AuthN Mappings in the org.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_authn_mappings(async_req=True)
        >>> result = thread.get()

        :param page_size: Size for a given page.
        :type page_size: int, optional
        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :param sort: Sort AuthN Mappings depending on the given field.
        :type sort: AuthNMappingsSort, optional
        :param include: Include additional information in the response.
        :type include: [str], optional
        :param filter: Filter all mappings by the given string.
        :type filter: str, optional
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
        :rtype: AuthNMappingsResponse
        """
        kwargs = self._list_authn_mappings_endpoint.default_arguments(kwargs)
        return self._list_authn_mappings_endpoint.call_with_http_info(**kwargs)

    def update_authn_mapping(self, authn_mapping_id, body, **kwargs):
        """Edit an AuthN Mapping.

        Edit an AuthN Mapping.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.update_authn_mapping(authn_mapping_id, body, async_req=True)
        >>> result = thread.get()

        :param authn_mapping_id: The UUID of the AuthN Mapping.
        :type authn_mapping_id: str
        :type body: AuthNMappingUpdateRequest
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
        :rtype: AuthNMappingResponse
        """
        kwargs = self._update_authn_mapping_endpoint.default_arguments(kwargs)
        kwargs["authn_mapping_id"] = authn_mapping_id

        kwargs["body"] = body

        return self._update_authn_mapping_endpoint.call_with_http_info(**kwargs)
