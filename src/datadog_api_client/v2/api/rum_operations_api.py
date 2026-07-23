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
    UUID,
)
from datadog_api_client.v2.model.rum_operation_response import RUMOperationResponse
from datadog_api_client.v2.model.rum_operation_create_request import RUMOperationCreateRequest
from datadog_api_client.v2.model.rum_operations_list_response import RUMOperationsListResponse
from datadog_api_client.v2.model.rum_operation_strong_links_list_response import RUMOperationStrongLinksListResponse
from datadog_api_client.v2.model.rum_operation_strong_link_response import RUMOperationStrongLinkResponse
from datadog_api_client.v2.model.rum_operation_strong_link_create_request import RUMOperationStrongLinkCreateRequest
from datadog_api_client.v2.model.rum_operation_strong_link_update_request import RUMOperationStrongLinkUpdateRequest
from datadog_api_client.v2.model.rum_operation_update_request import RUMOperationUpdateRequest


class RUMOperationsApi:
    """
    Manage `RUM Operations <https://docs.datadoghq.com/real_user_monitoring/>`_ , business
    transactions detected from RUM events through a configurable journey, and their strong links
    to features. See the `RUM & Session Replay page <https://docs.datadoghq.com/real_user_monitoring/>`_
    for more information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_rum_operation_endpoint = _Endpoint(
            settings={
                "response_type": (RUMOperationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/operations",
                "operation_id": "create_rum_operation",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (RUMOperationCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_rum_operation_strong_link_endpoint = _Endpoint(
            settings={
                "response_type": (RUMOperationStrongLinkResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/operations/strong_links",
                "operation_id": "create_rum_operation_strong_link",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (RUMOperationStrongLinkCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_rum_operation_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/operations/{operation_id}",
                "operation_id": "delete_rum_operation",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "operation_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "operation_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_rum_operation_strong_link_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/operations/strong_links/{operation_id}/{feature_id}",
                "operation_id": "delete_rum_operation_strong_link",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "operation_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "operation_id",
                    "location": "path",
                },
                "feature_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "feature_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_rum_operation_endpoint = _Endpoint(
            settings={
                "response_type": (RUMOperationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/operations/{operation_id}",
                "operation_id": "get_rum_operation",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "operation_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "operation_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_rum_operation_by_name_endpoint = _Endpoint(
            settings={
                "response_type": (RUMOperationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/operations/by-name/{name}",
                "operation_id": "get_rum_operation_by_name",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "name",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_rum_operations_endpoint = _Endpoint(
            settings={
                "response_type": (RUMOperationsListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/operations/search",
                "operation_id": "list_rum_operations",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "query": {
                    "openapi_types": (str,),
                    "attribute": "query",
                    "location": "query",
                },
                "page_offset": {
                    "validation": {
                        "inclusive_minimum": 0,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[offset]",
                    "location": "query",
                },
                "page_limit": {
                    "validation": {
                        "inclusive_maximum": 100,
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[limit]",
                    "location": "query",
                },
                "creator": {
                    "openapi_types": (str,),
                    "attribute": "creator",
                    "location": "query",
                },
                "team": {
                    "openapi_types": (str,),
                    "attribute": "team",
                    "location": "query",
                },
                "feature_id": {
                    "openapi_types": (str,),
                    "attribute": "feature_id",
                    "location": "query",
                },
                "application_id": {
                    "openapi_types": (UUID,),
                    "attribute": "application_id",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_rum_operation_strong_links_endpoint = _Endpoint(
            settings={
                "response_type": (RUMOperationStrongLinksListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/operations/strong_links",
                "operation_id": "list_rum_operation_strong_links",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "operation_id": {
                    "openapi_types": (str,),
                    "attribute": "operation_id",
                    "location": "query",
                },
                "feature_id": {
                    "openapi_types": (str,),
                    "attribute": "feature_id",
                    "location": "query",
                },
                "page_offset": {
                    "validation": {
                        "inclusive_minimum": 0,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[offset]",
                    "location": "query",
                },
                "page_limit": {
                    "validation": {
                        "inclusive_maximum": 200,
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[limit]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_rum_operation_endpoint = _Endpoint(
            settings={
                "response_type": (RUMOperationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/operations/{operation_id}",
                "operation_id": "update_rum_operation",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "operation_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "operation_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (RUMOperationUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_rum_operation_strong_link_endpoint = _Endpoint(
            settings={
                "response_type": (RUMOperationStrongLinkResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/operations/strong_links/{operation_id}/{feature_id}",
                "operation_id": "update_rum_operation_strong_link",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "operation_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "operation_id",
                    "location": "path",
                },
                "feature_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "feature_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (RUMOperationStrongLinkUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_rum_operation(
        self,
        body: RUMOperationCreateRequest,
    ) -> RUMOperationResponse:
        """Create a RUM operation.

        Create a new RUM operation, defining the journey used to detect it from RUM events.

        :type body: RUMOperationCreateRequest
        :rtype: RUMOperationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_rum_operation_endpoint.call_with_http_info(**kwargs)

    def create_rum_operation_strong_link(
        self,
        body: RUMOperationStrongLinkCreateRequest,
    ) -> RUMOperationStrongLinkResponse:
        """Create a RUM operation strong link.

        Create a strong link between a RUM operation and a feature, confirming that the feature
        belongs to the operation. The operation can be identified by ``operation_id`` or ``operation_name`` ;
        if ``operation_name`` does not match an existing operation, a stub operation is created.

        :type body: RUMOperationStrongLinkCreateRequest
        :rtype: RUMOperationStrongLinkResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_rum_operation_strong_link_endpoint.call_with_http_info(**kwargs)

    def delete_rum_operation(
        self,
        operation_id: str,
    ) -> None:
        """Delete a RUM operation.

        Delete a RUM operation.

        :param operation_id: The unique identifier of the RUM operation to delete.
        :type operation_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["operation_id"] = operation_id

        return self._delete_rum_operation_endpoint.call_with_http_info(**kwargs)

    def delete_rum_operation_strong_link(
        self,
        operation_id: str,
        feature_id: str,
    ) -> None:
        """Delete a RUM operation strong link.

        Delete the strong link between a RUM operation and a feature.

        :param operation_id: The unique identifier of the RUM operation.
        :type operation_id: str
        :param feature_id: The unique identifier of the feature.
        :type feature_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["operation_id"] = operation_id

        kwargs["feature_id"] = feature_id

        return self._delete_rum_operation_strong_link_endpoint.call_with_http_info(**kwargs)

    def get_rum_operation(
        self,
        operation_id: str,
    ) -> RUMOperationResponse:
        """Get a RUM operation.

        Retrieve a specific RUM operation by its unique identifier.

        :param operation_id: The unique identifier of the RUM operation.
        :type operation_id: str
        :rtype: RUMOperationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["operation_id"] = operation_id

        return self._get_rum_operation_endpoint.call_with_http_info(**kwargs)

    def get_rum_operation_by_name(
        self,
        name: str,
    ) -> RUMOperationResponse:
        """Get a RUM operation by name.

        Retrieve a specific RUM operation by its unique name.

        :param name: The unique name of the RUM operation.
        :type name: str
        :rtype: RUMOperationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["name"] = name

        return self._get_rum_operation_by_name_endpoint.call_with_http_info(**kwargs)

    def list_rum_operations(
        self,
        *,
        query: Union[str, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
        creator: Union[str, UnsetType] = unset,
        team: Union[str, UnsetType] = unset,
        feature_id: Union[str, UnsetType] = unset,
        application_id: Union[UUID, UnsetType] = unset,
    ) -> RUMOperationsListResponse:
        """Search RUM operations.

        Search RUM operations for your organization. Supports filtering by query, creator, team, feature, and application.

        :param query: A search query to filter operations by name.
        :type query: str, optional
        :param page_offset: Offset for pagination.
        :type page_offset: int, optional
        :param page_limit: Number of items per page. Maximum of 100.
        :type page_limit: int, optional
        :param creator: Filter operations by the email of their creator.
        :type creator: str, optional
        :param team: Filter operations by team. Accepts a comma-separated list of teams.
        :type team: str, optional
        :param feature_id: Filter operations by feature ID. Accepts a comma-separated list of feature IDs.
        :type feature_id: str, optional
        :param application_id: Filter operations by RUM application ID.
        :type application_id: UUID, optional
        :rtype: RUMOperationsListResponse
        """
        kwargs: Dict[str, Any] = {}
        if query is not unset:
            kwargs["query"] = query

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        if creator is not unset:
            kwargs["creator"] = creator

        if team is not unset:
            kwargs["team"] = team

        if feature_id is not unset:
            kwargs["feature_id"] = feature_id

        if application_id is not unset:
            kwargs["application_id"] = application_id

        return self._list_rum_operations_endpoint.call_with_http_info(**kwargs)

    def list_rum_operation_strong_links(
        self,
        *,
        operation_id: Union[str, UnsetType] = unset,
        feature_id: Union[str, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
    ) -> RUMOperationStrongLinksListResponse:
        """List RUM operation strong links.

        List strong links between RUM operations and features. A strong link confirms that a feature
        belongs to an operation. Provide ``operation_id`` , ``feature_id`` , or both to filter results;
        at least one is required.

        :param operation_id: Filter strong links by RUM operation ID.
        :type operation_id: str, optional
        :param feature_id: Filter strong links by feature ID.
        :type feature_id: str, optional
        :param page_offset: Offset for pagination.
        :type page_offset: int, optional
        :param page_limit: Number of items per page. Maximum of 200.
        :type page_limit: int, optional
        :rtype: RUMOperationStrongLinksListResponse
        """
        kwargs: Dict[str, Any] = {}
        if operation_id is not unset:
            kwargs["operation_id"] = operation_id

        if feature_id is not unset:
            kwargs["feature_id"] = feature_id

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        return self._list_rum_operation_strong_links_endpoint.call_with_http_info(**kwargs)

    def update_rum_operation(
        self,
        operation_id: str,
        body: RUMOperationUpdateRequest,
    ) -> RUMOperationResponse:
        """Update a RUM operation.

        Update an existing RUM operation. Fields omitted from the request body keep their existing value,
        with the exception of ``journey_rum`` , which is required and fully replaced on every update.

        :param operation_id: The unique identifier of the RUM operation to update.
        :type operation_id: str
        :type body: RUMOperationUpdateRequest
        :rtype: RUMOperationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["operation_id"] = operation_id

        kwargs["body"] = body

        return self._update_rum_operation_endpoint.call_with_http_info(**kwargs)

    def update_rum_operation_strong_link(
        self,
        operation_id: str,
        feature_id: str,
        body: RUMOperationStrongLinkUpdateRequest,
    ) -> RUMOperationStrongLinkResponse:
        """Update a RUM operation strong link.

        Update the status of a strong link between a RUM operation and a feature.

        :param operation_id: The unique identifier of the RUM operation.
        :type operation_id: str
        :param feature_id: The unique identifier of the feature.
        :type feature_id: str
        :type body: RUMOperationStrongLinkUpdateRequest
        :rtype: RUMOperationStrongLinkResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["operation_id"] = operation_id

        kwargs["feature_id"] = feature_id

        kwargs["body"] = body

        return self._update_rum_operation_strong_link_endpoint.call_with_http_info(**kwargs)
