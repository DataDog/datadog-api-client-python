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
from datadog_api_client.v2.model.org_connection_list_response import OrgConnectionListResponse
from datadog_api_client.v2.model.org_connection_response import OrgConnectionResponse
from datadog_api_client.v2.model.org_connection_create_request import OrgConnectionCreateRequest
from datadog_api_client.v2.model.org_connection_update_request import OrgConnectionUpdateRequest


class OrgConnectionsApi:
    """
    Manage connections between organizations. Org connections allow for controlled sharing of data between different Datadog organizations. See the `Cross-Organization Visibiltiy <https://docs.datadoghq.com/account_management/org_settings/cross_org_visibility/>`_ page for more information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_org_connections_endpoint = _Endpoint(
            settings={
                "response_type": (OrgConnectionResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/org_connections",
                "operation_id": "create_org_connections",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (OrgConnectionCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_org_connections_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/org_connections/{connection_id}",
                "operation_id": "delete_org_connections",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "connection_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "connection_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._list_org_connections_endpoint = _Endpoint(
            settings={
                "response_type": (OrgConnectionListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/org_connections",
                "operation_id": "list_org_connections",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "sink_org_id": {
                    "openapi_types": (str,),
                    "attribute": "sink_org_id",
                    "location": "query",
                },
                "source_org_id": {
                    "openapi_types": (str,),
                    "attribute": "source_org_id",
                    "location": "query",
                },
                "limit": {
                    "openapi_types": (int,),
                    "attribute": "limit",
                    "location": "query",
                },
                "offset": {
                    "openapi_types": (int,),
                    "attribute": "offset",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_org_connections_endpoint = _Endpoint(
            settings={
                "response_type": (OrgConnectionResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/org_connections/{connection_id}",
                "operation_id": "update_org_connections",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "connection_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "connection_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (OrgConnectionUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_org_connections(
        self,
        body: OrgConnectionCreateRequest,
    ) -> OrgConnectionResponse:
        """Create Org Connection.

        Create a new org connection between the current org and a target org.

        :type body: OrgConnectionCreateRequest
        :rtype: OrgConnectionResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_org_connections_endpoint.call_with_http_info(**kwargs)

    def delete_org_connections(
        self,
        connection_id: UUID,
    ) -> None:
        """Delete Org Connection.

        Delete an existing org connection.

        :param connection_id: The unique identifier of the org connection.
        :type connection_id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["connection_id"] = connection_id

        return self._delete_org_connections_endpoint.call_with_http_info(**kwargs)

    def list_org_connections(
        self,
        *,
        sink_org_id: Union[str, UnsetType] = unset,
        source_org_id: Union[str, UnsetType] = unset,
        limit: Union[int, UnsetType] = unset,
        offset: Union[int, UnsetType] = unset,
    ) -> OrgConnectionListResponse:
        """List Org Connections.

        Returns a list of org connections.

        :param sink_org_id: The Org ID of the sink org.
        :type sink_org_id: str, optional
        :param source_org_id: The Org ID of the source org.
        :type source_org_id: str, optional
        :param limit: The limit of number of entries you want to return. Default is 1000.
        :type limit: int, optional
        :param offset: The pagination offset which you want to query from. Default is 0.
        :type offset: int, optional
        :rtype: OrgConnectionListResponse
        """
        kwargs: Dict[str, Any] = {}
        if sink_org_id is not unset:
            kwargs["sink_org_id"] = sink_org_id

        if source_org_id is not unset:
            kwargs["source_org_id"] = source_org_id

        if limit is not unset:
            kwargs["limit"] = limit

        if offset is not unset:
            kwargs["offset"] = offset

        return self._list_org_connections_endpoint.call_with_http_info(**kwargs)

    def update_org_connections(
        self,
        connection_id: UUID,
        body: OrgConnectionUpdateRequest,
    ) -> OrgConnectionResponse:
        """Update Org Connection.

        Update an existing org connection.

        :param connection_id: The unique identifier of the org connection.
        :type connection_id: UUID
        :type body: OrgConnectionUpdateRequest
        :rtype: OrgConnectionResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["connection_id"] = connection_id

        kwargs["body"] = body

        return self._update_org_connections_endpoint.call_with_http_info(**kwargs)
