# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import re  # noqa: F401

from datadog_api_client.v2.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v2.model_utils import (  # noqa: F401
    date,
    datetime,
    file_type,
    none_type,
)
from datadog_api_client.v2.model.api_error_response import APIErrorResponse
from datadog_api_client.v2.model.incident_create_request import IncidentCreateRequest
from datadog_api_client.v2.model.incident_related_object import IncidentRelatedObject
from datadog_api_client.v2.model.incident_response import IncidentResponse
from datadog_api_client.v2.model.incident_update_request import IncidentUpdateRequest
from datadog_api_client.v2.model.incidents_response import IncidentsResponse


class IncidentsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._create_incident_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentResponse,),
                "auth": ["AuthZ", "apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/incidents",
                "operation_id": "create_incident",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (IncidentCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_incident_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["AuthZ", "apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/incidents/{incident_id}",
                "operation_id": "delete_incident",
                "http_method": "DELETE",
                "servers": None,
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_incident_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentResponse,),
                "auth": ["AuthZ", "apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/incidents/{incident_id}",
                "operation_id": "get_incident",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": ([IncidentRelatedObject],),
                    "attribute": "include",
                    "location": "query",
                    "collection_format": "csv",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_incidents_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentsResponse,),
                "auth": ["AuthZ", "apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/incidents",
                "operation_id": "list_incidents",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "include": {
                    "openapi_types": ([IncidentRelatedObject],),
                    "attribute": "include",
                    "location": "query",
                    "collection_format": "csv",
                },
                "page_size": {
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "page_offset": {
                    "openapi_types": (int,),
                    "attribute": "page[offset]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._update_incident_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentResponse,),
                "auth": ["AuthZ", "apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/incidents/{incident_id}",
                "operation_id": "update_incident",
                "http_method": "PATCH",
                "servers": None,
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_incident(self, body, **kwargs):
        """Create an incident

        Create an incident.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.create_incident(body, async_req=True)
        >>> result = thread.get()

        Args:
            body (IncidentCreateRequest): Incident payload.

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
            IncidentResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._create_incident_endpoint.default_arguments(kwargs)
        kwargs["body"] = body
        return self._create_incident_endpoint.call_with_http_info(**kwargs)

    def delete_incident(self, incident_id, **kwargs):
        """Delete an existing incident

        Deletes an existing incident from the users organization.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.delete_incident(incident_id, async_req=True)
        >>> result = thread.get()

        Args:
            incident_id (str): The UUID the incident.

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
        kwargs = self._delete_incident_endpoint.default_arguments(kwargs)
        kwargs["incident_id"] = incident_id
        return self._delete_incident_endpoint.call_with_http_info(**kwargs)

    def get_incident(self, incident_id, **kwargs):
        """Get the details of an incident

        Get the details of an incident by `incident_id`.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.get_incident(incident_id, async_req=True)
        >>> result = thread.get()

        Args:
            incident_id (str): The UUID the incident.

        Keyword Args:
            include ([IncidentRelatedObject]): [optional] Specifies which types of related objects should be included in the response.
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
            IncidentResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._get_incident_endpoint.default_arguments(kwargs)
        kwargs["incident_id"] = incident_id
        return self._get_incident_endpoint.call_with_http_info(**kwargs)

    def list_incidents(self, **kwargs):
        """Get a list of incidents

        Get all incidents for the user's organization.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_incidents(async_req=True)
        >>> result = thread.get()

        Keyword Args:
            include ([IncidentRelatedObject]): [optional] Specifies which types of related objects should be included in the response.
            page_size (int): [optional] Size for a given page. If omitted the server will use the default value of 10.
            page_offset (int): [optional] Specific offset to use as the beginning of the returned page. If omitted the server will use the default value of 0.
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
            IncidentsResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._list_incidents_endpoint.default_arguments(kwargs)
        return self._list_incidents_endpoint.call_with_http_info(**kwargs)

    def update_incident(self, incident_id, body, **kwargs):
        """Update an existing incident

        Updates an incident. Provide only the attributes that should be updated as this request is a partial update.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.update_incident(incident_id, body, async_req=True)
        >>> result = thread.get()

        Args:
            incident_id (str): The UUID the incident.
            body (IncidentUpdateRequest): Incident Payload.

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
            IncidentResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._update_incident_endpoint.default_arguments(kwargs)
        kwargs["incident_id"] = incident_id
        kwargs["body"] = body
        return self._update_incident_endpoint.call_with_http_info(**kwargs)
