# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v2.model.incident_teams_response import IncidentTeamsResponse
from datadog_api_client.v2.model.incident_related_object import IncidentRelatedObject
from datadog_api_client.v2.model.incident_team_response import IncidentTeamResponse
from datadog_api_client.v2.model.incident_team_create_request import IncidentTeamCreateRequest
from datadog_api_client.v2.model.incident_team_update_request import IncidentTeamUpdateRequest


class IncidentTeamsApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._create_incident_team_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentTeamResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/teams",
                "operation_id": "create_incident_team",
                "http_method": "POST",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (IncidentTeamCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_incident_team_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/teams/{team_id}",
                "operation_id": "delete_incident_team",
                "http_method": "DELETE",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "team_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "team_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_incident_team_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentTeamResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/teams/{team_id}",
                "operation_id": "get_incident_team",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "team_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "team_id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": (IncidentRelatedObject,),
                    "attribute": "include",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_incident_teams_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentTeamsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/teams",
                "operation_id": "list_incident_teams",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "include": {
                    "openapi_types": (IncidentRelatedObject,),
                    "attribute": "include",
                    "location": "query",
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

        self._update_incident_team_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentTeamResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/teams/{team_id}",
                "operation_id": "update_incident_team",
                "http_method": "PATCH",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "team_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "team_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentTeamUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_incident_team(self, body, **kwargs):
        """Create a new incident team.

        Creates a new incident team.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.create_incident_team(body, async_req=True)
        >>> result = thread.get()

        :param body: Incident Team Payload.
        :type body: IncidentTeamCreateRequest
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
        :rtype: IncidentTeamResponse
        """
        kwargs = self._create_incident_team_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._create_incident_team_endpoint.call_with_http_info(**kwargs)

    def delete_incident_team(self, team_id, **kwargs):
        """Delete an existing incident team.

        Deletes an existing incident team.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.delete_incident_team(team_id, async_req=True)
        >>> result = thread.get()

        :param team_id: The ID of the incident team.
        :type team_id: str
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
        kwargs = self._delete_incident_team_endpoint.default_arguments(kwargs)
        kwargs["team_id"] = team_id

        return self._delete_incident_team_endpoint.call_with_http_info(**kwargs)

    def get_incident_team(self, team_id, **kwargs):
        """Get details of an incident team.

        Get details of an incident team. If the `include[users]` query parameter is provided,
        the included attribute will contain the users related to these incident teams.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.get_incident_team(team_id, async_req=True)
        >>> result = thread.get()

        :param team_id: The ID of the incident team.
        :type team_id: str
        :param include: Specifies which types of related objects should be included in the response.
        :type include: IncidentRelatedObject, optional
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
        :rtype: IncidentTeamResponse
        """
        kwargs = self._get_incident_team_endpoint.default_arguments(kwargs)
        kwargs["team_id"] = team_id

        return self._get_incident_team_endpoint.call_with_http_info(**kwargs)

    def list_incident_teams(self, **kwargs):
        """Get a list of all incident teams.

        Get all incident teams for the requesting user's organization. If the `include[users]` query parameter is provided, the included attribute will contain the users related to these incident teams.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_incident_teams(async_req=True)
        >>> result = thread.get()

        :param include: Specifies which types of related objects should be included in the response.
        :type include: IncidentRelatedObject, optional
        :param page_size: Size for a given page.
        :type page_size: int, optional
        :param page_offset: Specific offset to use as the beginning of the returned page.
        :type page_offset: int, optional
        :param filter: A search query that filters teams by name.
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
        :rtype: IncidentTeamsResponse
        """
        kwargs = self._list_incident_teams_endpoint.default_arguments(kwargs)
        return self._list_incident_teams_endpoint.call_with_http_info(**kwargs)

    def update_incident_team(self, team_id, body, **kwargs):
        """Update an existing incident team.

        Updates an existing incident team. Only provide the attributes which should be updated as this request is a partial update.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.update_incident_team(team_id, body, async_req=True)
        >>> result = thread.get()

        :param team_id: The ID of the incident team.
        :type team_id: str
        :param body: Incident Team Payload.
        :type body: IncidentTeamUpdateRequest
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
        :rtype: IncidentTeamResponse
        """
        kwargs = self._update_incident_team_endpoint.default_arguments(kwargs)
        kwargs["team_id"] = team_id

        kwargs["body"] = body

        return self._update_incident_team_endpoint.call_with_http_info(**kwargs)
