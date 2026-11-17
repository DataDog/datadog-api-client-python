# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.facet_info_response import FacetInfoResponse
from datadog_api_client.v2.model.facet_info_request import FacetInfoRequest
from datadog_api_client.v2.model.query_response import QueryResponse
from datadog_api_client.v2.model.query_account_request import QueryAccountRequest
from datadog_api_client.v2.model.segments_response import SegmentsResponse
from datadog_api_client.v2.model.segment_entity import SegmentEntity
from datadog_api_client.v2.model.segment_sort_column import SegmentSortColumn
from datadog_api_client.v2.model.query_sort_order import QuerySortOrder
from datadog_api_client.v2.model.segment_response import SegmentResponse
from datadog_api_client.v2.model.segment_create_request import SegmentCreateRequest
from datadog_api_client.v2.model.segment_delete_response import SegmentDeleteResponse
from datadog_api_client.v2.model.segment_update_request import SegmentUpdateRequest
from datadog_api_client.v2.model.segment_preview_response import SegmentPreviewResponse
from datadog_api_client.v2.model.segment_preview_request import SegmentPreviewRequest
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

        self._create_product_analytics_segment_endpoint = _Endpoint(
            settings={
                "response_type": (SegmentResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/product-analytics/segment",
                "operation_id": "create_product_analytics_segment",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (SegmentCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
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

        self._delete_product_analytics_segment_endpoint = _Endpoint(
            settings={
                "response_type": (SegmentDeleteResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/product-analytics/segment/{id}",
                "operation_id": "delete_product_analytics_segment",
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
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._delete_user_profile_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/product-analytics/users/{user_id}",
                "operation_id": "delete_user_profile",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "user_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "user_id",
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

        self._get_product_analytics_segment_endpoint = _Endpoint(
            settings={
                "response_type": (SegmentResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/product-analytics/segment/{id}",
                "operation_id": "get_product_analytics_segment",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "id",
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

        self._list_product_analytics_segments_endpoint = _Endpoint(
            settings={
                "response_type": (SegmentsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/product-analytics/segment",
                "operation_id": "list_product_analytics_segments",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_entity": {
                    "openapi_types": (SegmentEntity,),
                    "attribute": "filter[entity]",
                    "location": "query",
                },
                "filter_type": {
                    "openapi_types": (str,),
                    "attribute": "filter[type]",
                    "location": "query",
                },
                "filter_ids": {
                    "openapi_types": (str,),
                    "attribute": "filter[ids]",
                    "location": "query",
                },
                "filter_disabled": {
                    "openapi_types": (bool,),
                    "attribute": "filter[disabled]",
                    "location": "query",
                },
                "sort_column": {
                    "openapi_types": (SegmentSortColumn,),
                    "attribute": "sort[column]",
                    "location": "query",
                },
                "sort_order": {
                    "openapi_types": (QuerySortOrder,),
                    "attribute": "sort[order]",
                    "location": "query",
                },
                "limit": {
                    "validation": {
                        "inclusive_minimum": 0,
                    },
                    "openapi_types": (int,),
                    "attribute": "limit",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._preview_product_analytics_segment_endpoint = _Endpoint(
            settings={
                "response_type": (SegmentPreviewResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/product-analytics/segments/preview",
                "operation_id": "preview_product_analytics_segment",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (SegmentPreviewRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
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

        self._update_product_analytics_segment_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/product-analytics/segment/{id}",
                "operation_id": "update_product_analytics_segment",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (SegmentUpdateRequest,),
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

    def create_product_analytics_segment(
        self,
        body: SegmentCreateRequest,
    ) -> SegmentResponse:
        """Create a segment.

        Create a user or account segment. The ``data_query`` defines who belongs to the segment.
        Segment names must be unique in the organization.

        :type body: SegmentCreateRequest
        :rtype: SegmentResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_product_analytics_segment_endpoint.call_with_http_info(**kwargs)

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

    def delete_product_analytics_segment(
        self,
        id: str,
    ) -> SegmentDeleteResponse:
        """Delete a segment.

        Delete a segment. Segments created by users are deleted permanently.
        Segments created by Datadog, and segments based on an uploaded list, are disabled instead.

        :param id: ID of the segment.
        :type id: str
        :rtype: SegmentDeleteResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._delete_product_analytics_segment_endpoint.call_with_http_info(**kwargs)

    def delete_user_profile(
        self,
        user_id: str,
    ) -> None:
        """Delete a user profile.

        Delete a Product Analytics user profile.
        Deletion is asynchronous: the request is accepted and the profile is removed shortly after, usually within a few
        minutes.
        This only deletes the user profile. To delete the RUM events of the user, use the RUM data deletion API.

        :param user_id: The ID of the user to delete, as sent in the ``usr.id`` attribute.
        :type user_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["user_id"] = user_id

        return self._delete_user_profile_endpoint.call_with_http_info(**kwargs)

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

    def get_product_analytics_segment(
        self,
        id: str,
    ) -> SegmentResponse:
        """Get a segment.

        Get a segment by ID, including its definition.

        :param id: ID of the segment.
        :type id: str
        :rtype: SegmentResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._get_product_analytics_segment_endpoint.call_with_http_info(**kwargs)

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

    def list_product_analytics_segments(
        self,
        *,
        filter_entity: Union[SegmentEntity, UnsetType] = unset,
        filter_type: Union[str, UnsetType] = unset,
        filter_ids: Union[str, UnsetType] = unset,
        filter_disabled: Union[bool, UnsetType] = unset,
        sort_column: Union[SegmentSortColumn, UnsetType] = unset,
        sort_order: Union[QuerySortOrder, UnsetType] = unset,
        limit: Union[int, UnsetType] = unset,
    ) -> SegmentsResponse:
        """List segments.

        List the user and account segments of your organization. Disabled segments are left out unless
        ``filter[disabled]`` is ``false``.
        The list does not include segment definitions; get a segment by ID to see its ``data_query``.

        :param filter_entity: Return only segments of this entity kind. Other values are ignored.
        :type filter_entity: SegmentEntity, optional
        :param filter_type: Comma-separated segment kinds to return: ``event_platform`` , ``user_store`` , ``account_store`` , ``reference_table`` ,
            ``static`` , ``template`` , ``combination`` , ``journey`` , or ``retention``.
        :type filter_type: str, optional
        :param filter_ids: Comma-separated segment IDs to return, up to 1000.
        :type filter_ids: str, optional
        :param filter_disabled: Set to ``false`` to include disabled segments.
        :type filter_disabled: bool, optional
        :param sort_column: Column to sort by. Other values are ignored.
        :type sort_column: SegmentSortColumn, optional
        :param sort_order: Sort order. Only used with ``sort[column]``.
        :type sort_order: QuerySortOrder, optional
        :param limit: Maximum number of segments to return. Returns all segments when not set.
        :type limit: int, optional
        :rtype: SegmentsResponse
        """
        kwargs: Dict[str, Any] = {}
        if filter_entity is not unset:
            kwargs["filter_entity"] = filter_entity

        if filter_type is not unset:
            kwargs["filter_type"] = filter_type

        if filter_ids is not unset:
            kwargs["filter_ids"] = filter_ids

        if filter_disabled is not unset:
            kwargs["filter_disabled"] = filter_disabled

        if sort_column is not unset:
            kwargs["sort_column"] = sort_column

        if sort_order is not unset:
            kwargs["sort_order"] = sort_order

        if limit is not unset:
            kwargs["limit"] = limit

        return self._list_product_analytics_segments_endpoint.call_with_http_info(**kwargs)

    def preview_product_analytics_segment(
        self,
        body: SegmentPreviewRequest,
    ) -> SegmentPreviewResponse:
        """Preview a segment.

        Preview the users or accounts that match a segment definition, without saving it.
        Returns up to 1000 rows and the total number of matching entities.

        :type body: SegmentPreviewRequest
        :rtype: SegmentPreviewResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._preview_product_analytics_segment_endpoint.call_with_http_info(**kwargs)

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

    def update_product_analytics_segment(
        self,
        id: str,
        body: SegmentUpdateRequest,
    ) -> None:
        """Update a segment.

        Update a segment. Fields that are not set are left unchanged. The ``id`` in the body must match the one in the
        path.
        The response has no body; get the segment to see the result.

        :param id: ID of the segment.
        :type id: str
        :type body: SegmentUpdateRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        kwargs["body"] = body

        return self._update_product_analytics_segment_endpoint.call_with_http_info(**kwargs)
