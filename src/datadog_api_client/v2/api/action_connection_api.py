# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.list_app_key_registrations_response import ListAppKeyRegistrationsResponse
from datadog_api_client.v2.model.get_app_key_registration_response import GetAppKeyRegistrationResponse
from datadog_api_client.v2.model.register_app_key_response import RegisterAppKeyResponse
from datadog_api_client.v2.model.list_action_connections_response import ListActionConnectionsResponse
from datadog_api_client.v2.model.create_action_connection_response import CreateActionConnectionResponse
from datadog_api_client.v2.model.create_action_connection_request import CreateActionConnectionRequest
from datadog_api_client.v2.model.list_connection_groups_response import ListConnectionGroupsResponse
from datadog_api_client.v2.model.update_connection_group_response import UpdateConnectionGroupResponse
from datadog_api_client.v2.model.update_connection_group_request import UpdateConnectionGroupRequest
from datadog_api_client.v2.model.get_action_connection_response import GetActionConnectionResponse
from datadog_api_client.v2.model.update_action_connection_response import UpdateActionConnectionResponse
from datadog_api_client.v2.model.update_action_connection_request import UpdateActionConnectionRequest


class ActionConnectionApi:
    """
    Action connections extend your installed integrations and allow you to take action in your third-party systems
    (e.g. AWS, GitLab, and Statuspage) with Datadog’s Workflow Automation and App Builder products.

    Datadog’s Integrations automatically provide authentication for Slack, Microsoft Teams, PagerDuty, Opsgenie,
    JIRA, GitHub, and Statuspage. You do not need additional connections in order to access these tools within
    Workflow Automation and App Builder.

    We offer granular access control for editing and resolving connections.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_action_connection_endpoint = _Endpoint(
            settings={
                "response_type": (CreateActionConnectionResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/actions/connections",
                "operation_id": "create_action_connection",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CreateActionConnectionRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_action_connection_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/actions/connections/{connection_id}",
                "operation_id": "delete_action_connection",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "connection_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "connection_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_action_connection_endpoint = _Endpoint(
            settings={
                "response_type": (GetActionConnectionResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/actions/connections/{connection_id}",
                "operation_id": "get_action_connection",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "connection_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "connection_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_app_key_registration_endpoint = _Endpoint(
            settings={
                "response_type": (GetAppKeyRegistrationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/actions/app_key_registrations/{app_key_id}",
                "operation_id": "get_app_key_registration",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "app_key_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "app_key_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_action_connections_endpoint = _Endpoint(
            settings={
                "response_type": (ListActionConnectionsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/actions/connections",
                "operation_id": "list_action_connections",
                "http_method": "GET",
                "version": "v2",
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
                "filter_integration": {
                    "openapi_types": ([str],),
                    "attribute": "filter[integration]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_tags": {
                    "openapi_types": ([str],),
                    "attribute": "filter[tags]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_environment": {
                    "openapi_types": (str,),
                    "attribute": "filter[environment]",
                    "location": "query",
                },
                "filter_connection_ids": {
                    "openapi_types": ([str],),
                    "attribute": "filter[connection_ids]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_creator_ids": {
                    "openapi_types": ([str],),
                    "attribute": "filter[creator_ids]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_search": {
                    "openapi_types": (str,),
                    "attribute": "filter[search]",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": ([str],),
                    "attribute": "sort",
                    "location": "query",
                    "collection_format": "multi",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_app_key_registrations_endpoint = _Endpoint(
            settings={
                "response_type": (ListAppKeyRegistrationsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/actions/app_key_registrations",
                "operation_id": "list_app_key_registrations",
                "http_method": "GET",
                "version": "v2",
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
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_connection_groups_endpoint = _Endpoint(
            settings={
                "response_type": (ListConnectionGroupsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/actions/connections/groups",
                "operation_id": "list_connection_groups",
                "http_method": "GET",
                "version": "v2",
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
                "filter_integration": {
                    "openapi_types": ([str],),
                    "attribute": "filter[integration]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_environment": {
                    "openapi_types": (str,),
                    "attribute": "filter[environment]",
                    "location": "query",
                },
                "filter_connection_group_ids": {
                    "openapi_types": ([str],),
                    "attribute": "filter[connection_group_ids]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_creator_id": {
                    "openapi_types": (str,),
                    "attribute": "filter[creator_id]",
                    "location": "query",
                },
                "filter_creator_ids": {
                    "openapi_types": ([str],),
                    "attribute": "filter[creator_ids]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_search": {
                    "openapi_types": (str,),
                    "attribute": "filter[search]",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": ([str],),
                    "attribute": "sort",
                    "location": "query",
                    "collection_format": "multi",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._register_app_key_endpoint = _Endpoint(
            settings={
                "response_type": (RegisterAppKeyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/actions/app_key_registrations/{app_key_id}",
                "operation_id": "register_app_key",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "app_key_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "app_key_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._unregister_app_key_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/actions/app_key_registrations/{app_key_id}",
                "operation_id": "unregister_app_key",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "app_key_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "app_key_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._update_action_connection_endpoint = _Endpoint(
            settings={
                "response_type": (UpdateActionConnectionResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/actions/connections/{connection_id}",
                "operation_id": "update_action_connection",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "connection_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "connection_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (UpdateActionConnectionRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_connection_group_endpoint = _Endpoint(
            settings={
                "response_type": (UpdateConnectionGroupResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/actions/connections/groups/{connection_group_id}",
                "operation_id": "update_connection_group",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "connection_group_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "connection_group_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (UpdateConnectionGroupRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_action_connection(
        self,
        body: CreateActionConnectionRequest,
    ) -> CreateActionConnectionResponse:
        """Create a new Action Connection.

        Create a new Action Connection. This API requires a `registered application key <https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key>`_.

        :type body: CreateActionConnectionRequest
        :rtype: CreateActionConnectionResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_action_connection_endpoint.call_with_http_info(**kwargs)

    def delete_action_connection(
        self,
        connection_id: str,
    ) -> None:
        """Delete an existing Action Connection.

        Delete an existing Action Connection. This API requires a `registered application key <https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key>`_. Alternatively, you can configure these permissions `in the UI <https://docs.datadoghq.com/account_management/api-app-keys/#actions-api-access>`_.

        :param connection_id: The ID of the action connection
        :type connection_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["connection_id"] = connection_id

        return self._delete_action_connection_endpoint.call_with_http_info(**kwargs)

    def get_action_connection(
        self,
        connection_id: str,
    ) -> GetActionConnectionResponse:
        """Get an existing Action Connection.

        Get an existing Action Connection. This API requires a `registered application key <https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key>`_.

        :param connection_id: The ID of the action connection
        :type connection_id: str
        :rtype: GetActionConnectionResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["connection_id"] = connection_id

        return self._get_action_connection_endpoint.call_with_http_info(**kwargs)

    def get_app_key_registration(
        self,
        app_key_id: str,
    ) -> GetAppKeyRegistrationResponse:
        """Get an existing App Key Registration.

        Get an existing App Key Registration

        :param app_key_id: The ID of the app key
        :type app_key_id: str
        :rtype: GetAppKeyRegistrationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["app_key_id"] = app_key_id

        return self._get_app_key_registration_endpoint.call_with_http_info(**kwargs)

    def list_action_connections(
        self,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        filter_integration: Union[List[str], UnsetType] = unset,
        filter_tags: Union[List[str], UnsetType] = unset,
        filter_environment: Union[str, UnsetType] = unset,
        filter_connection_ids: Union[List[str], UnsetType] = unset,
        filter_creator_ids: Union[List[str], UnsetType] = unset,
        filter_search: Union[str, UnsetType] = unset,
        sort: Union[List[str], UnsetType] = unset,
    ) -> ListActionConnectionsResponse:
        """List action connections.

        List all action connections for the organization. This endpoint supports filtering by integration type, tags, environment, and search strings. Pagination is supported using page size and page number parameters.

        :param page_size: The number of connections to return per page.
        :type page_size: int, optional
        :param page_number: The page number to return.
        :type page_number: int, optional
        :param filter_integration: Filter by integration type.
        :type filter_integration: [str], optional
        :param filter_tags: Filter by tags.
        :type filter_tags: [str], optional
        :param filter_environment: Filter by environment.
        :type filter_environment: str, optional
        :param filter_connection_ids: Filter by connection IDs.
        :type filter_connection_ids: [str], optional
        :param filter_creator_ids: Filter by creator IDs.
        :type filter_creator_ids: [str], optional
        :param filter_search: Search string to filter connections.
        :type filter_search: str, optional
        :param sort: Sort parameters.
        :type sort: [str], optional
        :rtype: ListActionConnectionsResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if filter_integration is not unset:
            kwargs["filter_integration"] = filter_integration

        if filter_tags is not unset:
            kwargs["filter_tags"] = filter_tags

        if filter_environment is not unset:
            kwargs["filter_environment"] = filter_environment

        if filter_connection_ids is not unset:
            kwargs["filter_connection_ids"] = filter_connection_ids

        if filter_creator_ids is not unset:
            kwargs["filter_creator_ids"] = filter_creator_ids

        if filter_search is not unset:
            kwargs["filter_search"] = filter_search

        if sort is not unset:
            kwargs["sort"] = sort

        return self._list_action_connections_endpoint.call_with_http_info(**kwargs)

    def list_app_key_registrations(
        self,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
    ) -> ListAppKeyRegistrationsResponse:
        """List App Key Registrations.

        List App Key Registrations

        :param page_size: The number of App Key Registrations to return per page.
        :type page_size: int, optional
        :param page_number: The page number to return.
        :type page_number: int, optional
        :rtype: ListAppKeyRegistrationsResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        return self._list_app_key_registrations_endpoint.call_with_http_info(**kwargs)

    def list_connection_groups(
        self,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        filter_integration: Union[List[str], UnsetType] = unset,
        filter_environment: Union[str, UnsetType] = unset,
        filter_connection_group_ids: Union[List[str], UnsetType] = unset,
        filter_creator_id: Union[str, UnsetType] = unset,
        filter_creator_ids: Union[List[str], UnsetType] = unset,
        filter_search: Union[str, UnsetType] = unset,
        sort: Union[List[str], UnsetType] = unset,
    ) -> ListConnectionGroupsResponse:
        """List connection groups.

        List all connection groups for the organization. This endpoint supports filtering by integration type, environment, connection group IDs, and search strings. Pagination is supported using page size and page number parameters.

        :param page_size: The number of connection groups to return per page.
        :type page_size: int, optional
        :param page_number: The page number to return.
        :type page_number: int, optional
        :param filter_integration: Filter by integration type.
        :type filter_integration: [str], optional
        :param filter_environment: Filter by environment.
        :type filter_environment: str, optional
        :param filter_connection_group_ids: Filter by connection group IDs.
        :type filter_connection_group_ids: [str], optional
        :param filter_creator_id: Filter by creator ID.
        :type filter_creator_id: str, optional
        :param filter_creator_ids: Filter by creator IDs.
        :type filter_creator_ids: [str], optional
        :param filter_search: Search string to filter connection groups.
        :type filter_search: str, optional
        :param sort: Sort parameters.
        :type sort: [str], optional
        :rtype: ListConnectionGroupsResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if filter_integration is not unset:
            kwargs["filter_integration"] = filter_integration

        if filter_environment is not unset:
            kwargs["filter_environment"] = filter_environment

        if filter_connection_group_ids is not unset:
            kwargs["filter_connection_group_ids"] = filter_connection_group_ids

        if filter_creator_id is not unset:
            kwargs["filter_creator_id"] = filter_creator_id

        if filter_creator_ids is not unset:
            kwargs["filter_creator_ids"] = filter_creator_ids

        if filter_search is not unset:
            kwargs["filter_search"] = filter_search

        if sort is not unset:
            kwargs["sort"] = sort

        return self._list_connection_groups_endpoint.call_with_http_info(**kwargs)

    def register_app_key(
        self,
        app_key_id: str,
    ) -> RegisterAppKeyResponse:
        """Register a new App Key.

        Register a new App Key

        :param app_key_id: The ID of the app key
        :type app_key_id: str
        :rtype: RegisterAppKeyResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["app_key_id"] = app_key_id

        return self._register_app_key_endpoint.call_with_http_info(**kwargs)

    def unregister_app_key(
        self,
        app_key_id: str,
    ) -> None:
        """Unregister an App Key.

        Unregister an App Key

        :param app_key_id: The ID of the app key
        :type app_key_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["app_key_id"] = app_key_id

        return self._unregister_app_key_endpoint.call_with_http_info(**kwargs)

    def update_action_connection(
        self,
        connection_id: str,
        body: UpdateActionConnectionRequest,
    ) -> UpdateActionConnectionResponse:
        """Update an existing Action Connection.

        Update an existing Action Connection. This API requires a `registered application key <https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key>`_.

        :param connection_id: The ID of the action connection
        :type connection_id: str
        :param body: Update an existing Action Connection request body
        :type body: UpdateActionConnectionRequest
        :rtype: UpdateActionConnectionResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["connection_id"] = connection_id

        kwargs["body"] = body

        return self._update_action_connection_endpoint.call_with_http_info(**kwargs)

    def update_connection_group(
        self,
        connection_group_id: str,
        body: UpdateConnectionGroupRequest,
    ) -> UpdateConnectionGroupResponse:
        """Update a connection group.

        Update an existing connection group by ID. This endpoint allows updating the name, description, tag keys, integration type, connections, and policy attributes of a connection group.

        :param connection_group_id: The ID of the connection group.
        :type connection_group_id: str
        :type body: UpdateConnectionGroupRequest
        :rtype: UpdateConnectionGroupResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["connection_group_id"] = connection_group_id

        kwargs["body"] = body

        return self._update_connection_group_endpoint.call_with_http_info(**kwargs)
