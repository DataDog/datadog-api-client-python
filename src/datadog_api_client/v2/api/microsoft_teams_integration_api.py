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
from datadog_api_client.v2.model.microsoft_teams_get_channel_by_name_response import (
    MicrosoftTeamsGetChannelByNameResponse,
)
from datadog_api_client.v2.model.microsoft_teams_api_handles_response import MicrosoftTeamsApiHandlesResponse
from datadog_api_client.v2.model.microsoft_teams_create_api_handle_response import MicrosoftTeamsCreateApiHandleResponse
from datadog_api_client.v2.model.microsoft_teams_create_api_handle_request import MicrosoftTeamsCreateApiHandleRequest
from datadog_api_client.v2.model.microsoft_teams_api_handle_info_response import MicrosoftTeamsApiHandleInfoResponse
from datadog_api_client.v2.model.microsoft_teams_update_api_handle_request import MicrosoftTeamsUpdateApiHandleRequest


class MicrosoftTeamsIntegrationApi:
    """
    Configure your `Datadog Microsoft Teams integration <https://docs.datadoghq.com/integrations/microsoft_teams/>`_
    directly through the Datadog API. Note: These endpoints do not support legacy connector handles.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_api_handle_endpoint = _Endpoint(
            settings={
                "response_type": (MicrosoftTeamsCreateApiHandleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/ms-teams/configuration/tenant-based-handles",
                "operation_id": "create_api_handle",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (MicrosoftTeamsCreateApiHandleRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_api_handle_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id}",
                "operation_id": "delete_api_handle",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "handle_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "handle_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_api_handle_endpoint = _Endpoint(
            settings={
                "response_type": (MicrosoftTeamsApiHandleInfoResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id}",
                "operation_id": "get_api_handle",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "handle_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "handle_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_api_handle_by_name_endpoint = _Endpoint(
            settings={
                "response_type": (MicrosoftTeamsApiHandleInfoResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/ms-teams/configuration/tenant-based-handles/name/{handle_name}",
                "operation_id": "get_api_handle_by_name",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "handle_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "handle_name",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_channel_by_name_endpoint = _Endpoint(
            settings={
                "response_type": (MicrosoftTeamsGetChannelByNameResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/ms-teams/configuration/channel/{tenant_name}/{team_name}/{channel_name}",
                "operation_id": "get_channel_by_name",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "tenant_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "tenant_name",
                    "location": "path",
                },
                "team_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "team_name",
                    "location": "path",
                },
                "channel_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "channel_name",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_api_handles_endpoint = _Endpoint(
            settings={
                "response_type": (MicrosoftTeamsApiHandlesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/ms-teams/configuration/tenant-based-handles",
                "operation_id": "list_api_handles",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "tenant_id": {
                    "openapi_types": (str,),
                    "attribute": "tenant_id",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_api_handle_endpoint = _Endpoint(
            settings={
                "response_type": (MicrosoftTeamsApiHandleInfoResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id}",
                "operation_id": "update_api_handle",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "handle_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "handle_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (MicrosoftTeamsUpdateApiHandleRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_api_handle(
        self,
        body: MicrosoftTeamsCreateApiHandleRequest,
    ) -> MicrosoftTeamsCreateApiHandleResponse:
        """Create handle.

        Create a handle in the Datadog Microsoft Teams integration.

        :param body: Handle payload.
        :type body: MicrosoftTeamsCreateApiHandleRequest
        :rtype: MicrosoftTeamsCreateApiHandleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_api_handle_endpoint.call_with_http_info(**kwargs)

    def delete_api_handle(
        self,
        handle_id: str,
    ) -> None:
        """Delete handle.

        Delete a handle from the Datadog Microsoft Teams integration.

        :param handle_id: Your handle id.
        :type handle_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["handle_id"] = handle_id

        return self._delete_api_handle_endpoint.call_with_http_info(**kwargs)

    def get_api_handle(
        self,
        handle_id: str,
    ) -> MicrosoftTeamsApiHandleInfoResponse:
        """Get handle information.

        Get the tenant, team, and channel information of a handle from the Datadog Microsoft Teams integration.

        :param handle_id: Your handle id.
        :type handle_id: str
        :rtype: MicrosoftTeamsApiHandleInfoResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["handle_id"] = handle_id

        return self._get_api_handle_endpoint.call_with_http_info(**kwargs)

    def get_api_handle_by_name(
        self,
        handle_name: str,
    ) -> MicrosoftTeamsApiHandleInfoResponse:
        """Get handle information by name.

        Get the tenant, team, and channel information of a handle by name from the Datadog Microsoft Teams integration.

        :param handle_name: Your handle name.
        :type handle_name: str
        :rtype: MicrosoftTeamsApiHandleInfoResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["handle_name"] = handle_name

        return self._get_api_handle_by_name_endpoint.call_with_http_info(**kwargs)

    def get_channel_by_name(
        self,
        tenant_name: str,
        team_name: str,
        channel_name: str,
    ) -> MicrosoftTeamsGetChannelByNameResponse:
        """Get channel information by name.

        Get the tenant, team, and channel ID of a channel in the Datadog Microsoft Teams integration.

        :param tenant_name: Your tenant name.
        :type tenant_name: str
        :param team_name: Your team name.
        :type team_name: str
        :param channel_name: Your channel name.
        :type channel_name: str
        :rtype: MicrosoftTeamsGetChannelByNameResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["tenant_name"] = tenant_name

        kwargs["team_name"] = team_name

        kwargs["channel_name"] = channel_name

        return self._get_channel_by_name_endpoint.call_with_http_info(**kwargs)

    def list_api_handles(
        self,
        *,
        tenant_id: Union[str, UnsetType] = unset,
    ) -> MicrosoftTeamsApiHandlesResponse:
        """Get all handles.

        Get a list of all handles from the Datadog Microsoft Teams integration.

        :param tenant_id: Your tenant id.
        :type tenant_id: str, optional
        :rtype: MicrosoftTeamsApiHandlesResponse
        """
        kwargs: Dict[str, Any] = {}
        if tenant_id is not unset:
            kwargs["tenant_id"] = tenant_id

        return self._list_api_handles_endpoint.call_with_http_info(**kwargs)

    def update_api_handle(
        self,
        handle_id: str,
        body: MicrosoftTeamsUpdateApiHandleRequest,
    ) -> MicrosoftTeamsApiHandleInfoResponse:
        """Update handle.

        Update a handle from the Datadog Microsoft Teams integration.

        :param handle_id: Your handle id.
        :type handle_id: str
        :param body: Opsgenie service payload.
        :type body: MicrosoftTeamsUpdateApiHandleRequest
        :rtype: MicrosoftTeamsApiHandleInfoResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["handle_id"] = handle_id

        kwargs["body"] = body

        return self._update_api_handle_endpoint.call_with_http_info(**kwargs)
