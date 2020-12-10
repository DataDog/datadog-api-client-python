# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import re  # noqa: F401
import sys  # noqa: F401

from datadog_api_client.v2.api_client import ApiClient, Endpoint
from datadog_api_client.v2.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from datadog_api_client.v2.model.api_error_response import APIErrorResponse
from datadog_api_client.v2.model.incident_service_create_request import IncidentServiceCreateRequest
from datadog_api_client.v2.model.incident_service_response import IncidentServiceResponse
from datadog_api_client.v2.model.incident_service_update_request import IncidentServiceUpdateRequest
from datadog_api_client.v2.model.incident_services_response import IncidentServicesResponse


class IncidentServicesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __create_incident_service(
            self,
            body,
            **kwargs
        ):
            """Create a new incident service  # noqa: E501

            Creates a new incident service.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_incident_service(body, async_req=True)
            >>> result = thread.get()

            Args:
                body (IncidentServiceCreateRequest): Incident Service Payload.

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
                IncidentServiceResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['body'] = \
                body
            return self.call_with_http_info(**kwargs)

        self.create_incident_service = Endpoint(
            settings={
                'response_type': (IncidentServiceResponse,),
                'auth': [
                    'apiKeyAuth',
                    'appKeyAuth'
                ],
                'endpoint_path': '/api/v2/services',
                'operation_id': 'create_incident_service',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'body',
                ],
                'required': [
                    'body',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'body':
                        (IncidentServiceCreateRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__create_incident_service
        )

        def __delete_incident_service(
            self,
            service_id,
            **kwargs
        ):
            """Delete an existing incident service  # noqa: E501

            Deletes an existing incident service.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_incident_service(service_id, async_req=True)
            >>> result = thread.get()

            Args:
                service_id (str): The ID of the incident service.

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
                None
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['service_id'] = \
                service_id
            return self.call_with_http_info(**kwargs)

        self.delete_incident_service = Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'apiKeyAuth',
                    'appKeyAuth'
                ],
                'endpoint_path': '/api/v2/services/{service_id}',
                'operation_id': 'delete_incident_service',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                ],
                'required': [
                    'service_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'service_id':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                },
                'location_map': {
                    'service_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__delete_incident_service
        )

        def __get_incident_service(
            self,
            service_id,
            **kwargs
        ):
            """Get details of an incident service  # noqa: E501

            Get details of an incident service. If the `include[users]` query parameter is provided, the included attribute will contain the users related to these incident services.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_incident_service(service_id, async_req=True)
            >>> result = thread.get()

            Args:
                service_id (str): The ID of the incident service.

            Keyword Args:
                include (str): Specifies which types of related objects should be included in the response.. [optional] if omitted the server will use the default value of "users"
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
                IncidentServiceResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['service_id'] = \
                service_id
            return self.call_with_http_info(**kwargs)

        self.get_incident_service = Endpoint(
            settings={
                'response_type': (IncidentServiceResponse,),
                'auth': [
                    'apiKeyAuth',
                    'appKeyAuth'
                ],
                'endpoint_path': '/api/v2/services/{service_id}',
                'operation_id': 'get_incident_service',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'include',
                ],
                'required': [
                    'service_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'include',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('include',): {

                        "USERS": "users"
                    },
                },
                'openapi_types': {
                    'service_id':
                        (str,),
                    'include':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'include': 'include',
                },
                'location_map': {
                    'service_id': 'path',
                    'include': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_incident_service
        )

        def __list_incident_services(
            self,
            **kwargs
        ):
            """Get a list of all incident services  # noqa: E501

            Get all incident services uploaded for the requesting user's organization. If the `include[users]` query parameter is provided, the included attribute will contain the users related to these incident services.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_incident_services(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                include (str): Specifies which types of related objects should be included in the response.. [optional] if omitted the server will use the default value of "users"
                page_size (int): Size for a given page.. [optional] if omitted the server will use the default value of 10
                page_offset (int): Specific offset to use as the beginning of the returned page.. [optional] if omitted the server will use the default value of 0
                filter (str): A search query that filters services by name.. [optional]
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
                IncidentServicesResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.list_incident_services = Endpoint(
            settings={
                'response_type': (IncidentServicesResponse,),
                'auth': [
                    'apiKeyAuth',
                    'appKeyAuth'
                ],
                'endpoint_path': '/api/v2/services',
                'operation_id': 'list_incident_services',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'include',
                    'page_size',
                    'page_offset',
                    'filter',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'include',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('include',): {

                        "USERS": "users"
                    },
                },
                'openapi_types': {
                    'include':
                        (str,),
                    'page_size':
                        (int,),
                    'page_offset':
                        (int,),
                    'filter':
                        (str,),
                },
                'attribute_map': {
                    'include': 'include',
                    'page_size': 'page[size]',
                    'page_offset': 'page[offset]',
                    'filter': 'filter',
                },
                'location_map': {
                    'include': 'query',
                    'page_size': 'query',
                    'page_offset': 'query',
                    'filter': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__list_incident_services
        )

        def __update_incident_service(
            self,
            service_id,
            body,
            **kwargs
        ):
            """Update an existing incident service  # noqa: E501

            Updates an existing incident service. Only provide the attributes which should be updated as this request is a partial update.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_incident_service(service_id, body, async_req=True)
            >>> result = thread.get()

            Args:
                service_id (str): The ID of the incident service.
                body (IncidentServiceUpdateRequest): Incident Service Payload.

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
                IncidentServiceResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['service_id'] = \
                service_id
            kwargs['body'] = \
                body
            return self.call_with_http_info(**kwargs)

        self.update_incident_service = Endpoint(
            settings={
                'response_type': (IncidentServiceResponse,),
                'auth': [
                    'apiKeyAuth',
                    'appKeyAuth'
                ],
                'endpoint_path': '/api/v2/services/{service_id}',
                'operation_id': 'update_incident_service',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'body',
                ],
                'required': [
                    'service_id',
                    'body',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'service_id':
                        (str,),
                    'body':
                        (IncidentServiceUpdateRequest,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                },
                'location_map': {
                    'service_id': 'path',
                    'body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__update_incident_service
        )
