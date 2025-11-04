# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.facet_info_response import FacetInfoResponse
from datadog_api_client.v2.model.facet_info_request import FacetInfoRequest
from datadog_api_client.v2.model.query_response import QueryResponse
from datadog_api_client.v2.model.query_account_request import QueryAccountRequest
from datadog_api_client.v2.model.query_event_filtered_users_request import QueryEventFilteredUsersRequest
from datadog_api_client.v2.model.query_users_request import QueryUsersRequest
from datadog_api_client.v2.model.get_mapping_response import GetMappingResponse
from datadog_api_client.v2.model.create_connection_request import CreateConnectionRequest
from datadog_api_client.v2.model.update_connection_request import UpdateConnectionRequest
from datadog_api_client.v2.model.list_connections_response import ListConnectionsResponse


class RumAudienceManagementApi:
    """
    Auto-generated tag Rum Audience Management
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_connection_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/product-analytics/{entity}/mapping/connection",
                "operation_id": "create_connection",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "entity": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "entity",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CreateConnectionRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_connection_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/product-analytics/{entity}/mapping/connection/{id}",
                "operation_id": "delete_connection",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "id",
                    "location": "path",
                },
                "entity": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "entity",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_account_facet_info_endpoint = _Endpoint(
            settings={
                "response_type": (FacetInfoResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/product-analytics/accounts/facet_info",
                "operation_id": "get_account_facet_info",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (FacetInfoRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._get_mapping_endpoint = _Endpoint(
            settings={
                "response_type": (GetMappingResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/product-analytics/{entity}/mapping",
                "operation_id": "get_mapping",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "entity": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "entity",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_user_facet_info_endpoint = _Endpoint(
            settings={
                "response_type": (FacetInfoResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/product-analytics/users/facet_info",
                "operation_id": "get_user_facet_info",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (FacetInfoRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._list_connections_endpoint = _Endpoint(
            settings={
                "response_type": (ListConnectionsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/product-analytics/{entity}/mapping/connections",
                "operation_id": "list_connections",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "entity": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "entity",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._query_accounts_endpoint = _Endpoint(
            settings={
                "response_type": (QueryResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/product-analytics/accounts/query",
                "operation_id": "query_accounts",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (QueryAccountRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._query_event_filtered_users_endpoint = _Endpoint(
            settings={
                "response_type": (QueryResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/product-analytics/users/event_filtered_query",
                "operation_id": "query_event_filtered_users",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (QueryEventFilteredUsersRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._query_users_endpoint = _Endpoint(
            settings={
                "response_type": (QueryResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/product-analytics/users/query",
                "operation_id": "query_users",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (QueryUsersRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_connection_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/product-analytics/{entity}/mapping/connection",
                "operation_id": "update_connection",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "entity": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "entity",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (UpdateConnectionRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_connection(
        self,
        entity: str,
        body: CreateConnectionRequest,
    ) -> None:
        """Create connection.

        Create a new data connection and its fields for an entity

        :param entity: The entity for which to create the connection
        :type entity: str
        :type body: CreateConnectionRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["entity"] = entity

        kwargs["body"] = body

        return self._create_connection_endpoint.call_with_http_info(**kwargs)

    def delete_connection(
        self,
        id: str,
        entity: str,
    ) -> None:
        """Delete connection.

        Delete an existing data connection for an entity

        :param id: The connection ID to delete
        :type id: str
        :param entity: The entity for which to delete the connection
        :type entity: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        kwargs["entity"] = entity

        return self._delete_connection_endpoint.call_with_http_info(**kwargs)

    def get_account_facet_info(
        self,
        body: FacetInfoRequest,
    ) -> FacetInfoResponse:
        """Get account facet info.

        Get facet information for account attributes including possible values and counts

        :type body: FacetInfoRequest
        :rtype: FacetInfoResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._get_account_facet_info_endpoint.call_with_http_info(**kwargs)

    def get_mapping(
        self,
        entity: str,
    ) -> GetMappingResponse:
        """Get mapping.

        Get entity mapping configuration including all available attributes and their properties

        :param entity: The entity for which to get the mapping
        :type entity: str
        :rtype: GetMappingResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["entity"] = entity

        return self._get_mapping_endpoint.call_with_http_info(**kwargs)

    def get_user_facet_info(
        self,
        body: FacetInfoRequest,
    ) -> FacetInfoResponse:
        """Get user facet info.

        Get facet information for user attributes including possible values and counts

        :type body: FacetInfoRequest
        :rtype: FacetInfoResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._get_user_facet_info_endpoint.call_with_http_info(**kwargs)

    def list_connections(
        self,
        entity: str,
    ) -> ListConnectionsResponse:
        """List connections.

        List all data connections for an entity

        :param entity: The entity for which to list connections
        :type entity: str
        :rtype: ListConnectionsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["entity"] = entity

        return self._list_connections_endpoint.call_with_http_info(**kwargs)

    def query_accounts(
        self,
        body: QueryAccountRequest,
    ) -> QueryResponse:
        """Query accounts.

        Query accounts with flexible filtering by account properties

        :type body: QueryAccountRequest
        :rtype: QueryResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._query_accounts_endpoint.call_with_http_info(**kwargs)

    def query_event_filtered_users(
        self,
        body: QueryEventFilteredUsersRequest,
    ) -> QueryResponse:
        """Query event filtered users.

        Query users filtered by both user properties and event platform data

        :type body: QueryEventFilteredUsersRequest
        :rtype: QueryResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._query_event_filtered_users_endpoint.call_with_http_info(**kwargs)

    def query_users(
        self,
        body: QueryUsersRequest,
    ) -> QueryResponse:
        """Query users.

        Query users with flexible filtering by user properties, with optional wildcard search

        :type body: QueryUsersRequest
        :rtype: QueryResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._query_users_endpoint.call_with_http_info(**kwargs)

    def update_connection(
        self,
        entity: str,
        body: UpdateConnectionRequest,
    ) -> None:
        """Update connection.

        Update an existing data connection by adding, updating, or deleting fields

        :param entity: The entity for which to update the connection
        :type entity: str
        :type body: UpdateConnectionRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["entity"] = entity

        kwargs["body"] = body

        return self._update_connection_endpoint.call_with_http_info(**kwargs)
