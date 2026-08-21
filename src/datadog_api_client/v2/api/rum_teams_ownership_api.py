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
    UUID,
)
from datadog_api_client.v2.model.teams_ownership_mappings_response import TeamsOwnershipMappingsResponse
from datadog_api_client.v2.model.teams_ownership_mapping_response import TeamsOwnershipMappingResponse
from datadog_api_client.v2.model.teams_ownership_mapping_create_request import TeamsOwnershipMappingCreateRequest
from datadog_api_client.v2.model.teams_ownership_mapping_batch_response import TeamsOwnershipMappingBatchResponse
from datadog_api_client.v2.model.teams_ownership_mapping_batch_request import TeamsOwnershipMappingBatchRequest
from datadog_api_client.v2.model.teams_ownership_rules_response import TeamsOwnershipRulesResponse


class RumTeamsOwnershipApi:
    """
    Manage teams ownership mappings between RUM views and the teams that own them.
    See https://docs.datadoghq.com/real_user_monitoring/ownership_of_views/.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_teams_ownership_mapping_endpoint = _Endpoint(
            settings={
                "response_type": (TeamsOwnershipMappingResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/config/teams-ownership/mappings",
                "operation_id": "create_teams_ownership_mapping",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (TeamsOwnershipMappingCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_teams_ownership_mappings_batch_endpoint = _Endpoint(
            settings={
                "response_type": (TeamsOwnershipMappingBatchResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/config/teams-ownership/mappings/operations",
                "operation_id": "create_teams_ownership_mappings_batch",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (TeamsOwnershipMappingBatchRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_teams_ownership_mapping_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/config/teams-ownership/mappings/{id}",
                "operation_id": "delete_teams_ownership_mapping",
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
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_teams_ownership_mapping_endpoint = _Endpoint(
            settings={
                "response_type": (TeamsOwnershipMappingResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/config/teams-ownership/mappings/{id}",
                "operation_id": "get_teams_ownership_mapping",
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

        self._list_teams_ownership_mappings_endpoint = _Endpoint(
            settings={
                "response_type": (TeamsOwnershipMappingsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/config/teams-ownership/mappings",
                "operation_id": "list_teams_ownership_mappings",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_view_name": {
                    "openapi_types": ([str],),
                    "attribute": "filter[view_name]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_team_handle": {
                    "openapi_types": ([str],),
                    "attribute": "filter[team_handle]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_application_id": {
                    "openapi_types": ([UUID],),
                    "attribute": "filter[application_id]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_service": {
                    "openapi_types": ([str],),
                    "attribute": "filter[service]",
                    "location": "query",
                    "collection_format": "multi",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_teams_ownership_rules_endpoint = _Endpoint(
            settings={
                "response_type": (TeamsOwnershipRulesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/config/teams-ownership/rules",
                "operation_id": "list_teams_ownership_rules",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_view_name": {
                    "openapi_types": ([str],),
                    "attribute": "filter[view_name]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_team_handle": {
                    "openapi_types": ([str],),
                    "attribute": "filter[team_handle]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_application_id": {
                    "openapi_types": ([UUID],),
                    "attribute": "filter[application_id]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_service": {
                    "openapi_types": ([str],),
                    "attribute": "filter[service]",
                    "location": "query",
                    "collection_format": "multi",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def create_teams_ownership_mapping(
        self,
        body: TeamsOwnershipMappingCreateRequest,
    ) -> TeamsOwnershipMappingResponse:
        """Create a teams ownership mapping.

        Create a teams ownership mapping for your organization.
        Returns the teams ownership mapping object from the request body when the request is successful.

        :param body: The definition of the teams ownership mapping to create.
        :type body: TeamsOwnershipMappingCreateRequest
        :rtype: TeamsOwnershipMappingResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_teams_ownership_mapping_endpoint.call_with_http_info(**kwargs)

    def create_teams_ownership_mappings_batch(
        self,
        body: TeamsOwnershipMappingBatchRequest,
    ) -> TeamsOwnershipMappingBatchResponse:
        """Bulk create and remove teams ownership mappings.

        Add and remove teams ownership mappings for your organization in a single atomic request, following
        the JSON:API `atomic operations extension <https://jsonapi.org/ext/atomic/>`_.
        Operations are applied together: if any operation is invalid, none of the operations are applied.
        Add operations are processed before remove operations, so results may not appear in the same
        order as the request.

        :param body: The list of add and remove operations to apply atomically.
        :type body: TeamsOwnershipMappingBatchRequest
        :rtype: TeamsOwnershipMappingBatchResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_teams_ownership_mappings_batch_endpoint.call_with_http_info(**kwargs)

    def delete_teams_ownership_mapping(
        self,
        id: str,
    ) -> None:
        """Delete a teams ownership mapping.

        Delete a specific teams ownership mapping from your organization.

        :param id: The ID of the teams ownership mapping.
        :type id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._delete_teams_ownership_mapping_endpoint.call_with_http_info(**kwargs)

    def get_teams_ownership_mapping(
        self,
        id: str,
    ) -> TeamsOwnershipMappingResponse:
        """Get a teams ownership mapping.

        Get a specific teams ownership mapping from your organization.

        :param id: The ID of the teams ownership mapping.
        :type id: str
        :rtype: TeamsOwnershipMappingResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._get_teams_ownership_mapping_endpoint.call_with_http_info(**kwargs)

    def list_teams_ownership_mappings(
        self,
        *,
        filter_view_name: Union[List[str], UnsetType] = unset,
        filter_team_handle: Union[List[str], UnsetType] = unset,
        filter_application_id: Union[List[UUID], UnsetType] = unset,
        filter_service: Union[List[str], UnsetType] = unset,
    ) -> TeamsOwnershipMappingsResponse:
        """List teams ownership mappings.

        Get the list of teams ownership mappings for your organization, optionally filtered.

        :param filter_view_name: Filter mappings by RUM view name.
        :type filter_view_name: [str], optional
        :param filter_team_handle: Filter mappings by owning team handle.
        :type filter_team_handle: [str], optional
        :param filter_application_id: Filter mappings by RUM application ID. Each value must be a valid UUID.
        :type filter_application_id: [UUID], optional
        :param filter_service: Filter mappings by RUM application service name.
        :type filter_service: [str], optional
        :rtype: TeamsOwnershipMappingsResponse
        """
        kwargs: Dict[str, Any] = {}
        if filter_view_name is not unset:
            kwargs["filter_view_name"] = filter_view_name

        if filter_team_handle is not unset:
            kwargs["filter_team_handle"] = filter_team_handle

        if filter_application_id is not unset:
            kwargs["filter_application_id"] = filter_application_id

        if filter_service is not unset:
            kwargs["filter_service"] = filter_service

        return self._list_teams_ownership_mappings_endpoint.call_with_http_info(**kwargs)

    def list_teams_ownership_rules(
        self,
        *,
        filter_view_name: Union[List[str], UnsetType] = unset,
        filter_team_handle: Union[List[str], UnsetType] = unset,
        filter_application_id: Union[List[UUID], UnsetType] = unset,
        filter_service: Union[List[str], UnsetType] = unset,
    ) -> TeamsOwnershipRulesResponse:
        """List teams ownership rules.

        Get the list of teams ownership rules for your organization, optionally filtered.
        Rules group the underlying mappings by ``view_name`` , ``application_id`` , ``service`` , and ``match_type`` ,
        collapsing every team that owns the same view into a single entry.

        :param filter_view_name: Filter mappings by RUM view name.
        :type filter_view_name: [str], optional
        :param filter_team_handle: Filter mappings by owning team handle.
        :type filter_team_handle: [str], optional
        :param filter_application_id: Filter mappings by RUM application ID. Each value must be a valid UUID.
        :type filter_application_id: [UUID], optional
        :param filter_service: Filter mappings by RUM application service name.
        :type filter_service: [str], optional
        :rtype: TeamsOwnershipRulesResponse
        """
        kwargs: Dict[str, Any] = {}
        if filter_view_name is not unset:
            kwargs["filter_view_name"] = filter_view_name

        if filter_team_handle is not unset:
            kwargs["filter_team_handle"] = filter_team_handle

        if filter_application_id is not unset:
            kwargs["filter_application_id"] = filter_application_id

        if filter_service is not unset:
            kwargs["filter_service"] = filter_service

        return self._list_teams_ownership_rules_endpoint.call_with_http_info(**kwargs)
