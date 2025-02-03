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
from datadog_api_client.v2.model.microsoft_teams_tenant_based_handles_response import (
    MicrosoftTeamsTenantBasedHandlesResponse,
)
from datadog_api_client.v2.model.microsoft_teams_tenant_based_handle_response import (
    MicrosoftTeamsTenantBasedHandleResponse,
)
from datadog_api_client.v2.model.microsoft_teams_create_tenant_based_handle_request import (
    MicrosoftTeamsCreateTenantBasedHandleRequest,
)
from datadog_api_client.v2.model.microsoft_teams_update_tenant_based_handle_request import (
    MicrosoftTeamsUpdateTenantBasedHandleRequest,
)
from datadog_api_client.v2.model.microsoft_teams_workflows_webhook_handles_response import (
    MicrosoftTeamsWorkflowsWebhookHandlesResponse,
)
from datadog_api_client.v2.model.microsoft_teams_workflows_webhook_handle_response import (
    MicrosoftTeamsWorkflowsWebhookHandleResponse,
)
from datadog_api_client.v2.model.microsoft_teams_create_workflows_webhook_handle_request import (
    MicrosoftTeamsCreateWorkflowsWebhookHandleRequest,
)
from datadog_api_client.v2.model.microsoft_teams_update_workflows_webhook_handle_request import (
    MicrosoftTeamsUpdateWorkflowsWebhookHandleRequest,
)


class MicrosoftTeamsIntegrationApi:
    """
    Configure your `Datadog Microsoft Teams integration <https://docs.datadoghq.com/integrations/microsoft_teams/>`_
    directly through the Datadog API. Note: These endpoints do not support legacy connector handles.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_tenant_based_handle_endpoint = _Endpoint(
            settings={
                "response_type": (MicrosoftTeamsTenantBasedHandleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/ms-teams/configuration/tenant-based-handles",
                "operation_id": "create_tenant_based_handle",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (MicrosoftTeamsCreateTenantBasedHandleRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_workflows_webhook_handle_endpoint = _Endpoint(
            settings={
                "response_type": (MicrosoftTeamsWorkflowsWebhookHandleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/ms-teams/configuration/workflows-webhook-handles",
                "operation_id": "create_workflows_webhook_handle",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (MicrosoftTeamsCreateWorkflowsWebhookHandleRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_tenant_based_handle_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id}",
                "operation_id": "delete_tenant_based_handle",
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

        self._delete_workflows_webhook_handle_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id}",
                "operation_id": "delete_workflows_webhook_handle",
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

        self._get_tenant_based_handle_endpoint = _Endpoint(
            settings={
                "response_type": (MicrosoftTeamsTenantBasedHandleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id}",
                "operation_id": "get_tenant_based_handle",
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

        self._get_workflows_webhook_handle_endpoint = _Endpoint(
            settings={
                "response_type": (MicrosoftTeamsWorkflowsWebhookHandleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id}",
                "operation_id": "get_workflows_webhook_handle",
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

        self._list_tenant_based_handles_endpoint = _Endpoint(
            settings={
                "response_type": (MicrosoftTeamsTenantBasedHandlesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/ms-teams/configuration/tenant-based-handles",
                "operation_id": "list_tenant_based_handles",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "tenant_id": {
                    "openapi_types": (str,),
                    "attribute": "tenant_id",
                    "location": "query",
                },
                "name": {
                    "openapi_types": (str,),
                    "attribute": "name",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_workflows_webhook_handles_endpoint = _Endpoint(
            settings={
                "response_type": (MicrosoftTeamsWorkflowsWebhookHandlesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/ms-teams/configuration/workflows-webhook-handles",
                "operation_id": "list_workflows_webhook_handles",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "name": {
                    "openapi_types": (str,),
                    "attribute": "name",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_tenant_based_handle_endpoint = _Endpoint(
            settings={
                "response_type": (MicrosoftTeamsTenantBasedHandleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id}",
                "operation_id": "update_tenant_based_handle",
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
                    "openapi_types": (MicrosoftTeamsUpdateTenantBasedHandleRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_workflows_webhook_handle_endpoint = _Endpoint(
            settings={
                "response_type": (MicrosoftTeamsWorkflowsWebhookHandleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id}",
                "operation_id": "update_workflows_webhook_handle",
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
                    "openapi_types": (MicrosoftTeamsUpdateWorkflowsWebhookHandleRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_tenant_based_handle(
        self,
        body: MicrosoftTeamsCreateTenantBasedHandleRequest,
    ) -> MicrosoftTeamsTenantBasedHandleResponse:
        """Create tenant-based handle.

        Create a tenant-based handle in the Datadog Microsoft Teams integration.

        :param body: Tenant-based handle payload.
        :type body: MicrosoftTeamsCreateTenantBasedHandleRequest
        :rtype: MicrosoftTeamsTenantBasedHandleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_tenant_based_handle_endpoint.call_with_http_info(**kwargs)

    def create_workflows_webhook_handle(
        self,
        body: MicrosoftTeamsCreateWorkflowsWebhookHandleRequest,
    ) -> MicrosoftTeamsWorkflowsWebhookHandleResponse:
        """Create Workflows webhook handle.

        Create a Workflows webhook handle in the Datadog Microsoft Teams integration.

        :param body: Workflows Webhook handle payload.
        :type body: MicrosoftTeamsCreateWorkflowsWebhookHandleRequest
        :rtype: MicrosoftTeamsWorkflowsWebhookHandleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_workflows_webhook_handle_endpoint.call_with_http_info(**kwargs)

    def delete_tenant_based_handle(
        self,
        handle_id: str,
    ) -> None:
        """Delete tenant-based handle.

        Delete a tenant-based handle from the Datadog Microsoft Teams integration.

        :param handle_id: Your tenant-based handle id.
        :type handle_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["handle_id"] = handle_id

        return self._delete_tenant_based_handle_endpoint.call_with_http_info(**kwargs)

    def delete_workflows_webhook_handle(
        self,
        handle_id: str,
    ) -> None:
        """Delete Workflows webhook handle.

        Delete a Workflows webhook handle from the Datadog Microsoft Teams integration.

        :param handle_id: Your Workflows webhook handle id.
        :type handle_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["handle_id"] = handle_id

        return self._delete_workflows_webhook_handle_endpoint.call_with_http_info(**kwargs)

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

    def get_tenant_based_handle(
        self,
        handle_id: str,
    ) -> MicrosoftTeamsTenantBasedHandleResponse:
        """Get tenant-based handle information.

        Get the tenant, team, and channel information of a tenant-based handle from the Datadog Microsoft Teams integration.

        :param handle_id: Your tenant-based handle id.
        :type handle_id: str
        :rtype: MicrosoftTeamsTenantBasedHandleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["handle_id"] = handle_id

        return self._get_tenant_based_handle_endpoint.call_with_http_info(**kwargs)

    def get_workflows_webhook_handle(
        self,
        handle_id: str,
    ) -> MicrosoftTeamsWorkflowsWebhookHandleResponse:
        """Get Workflows webhook handle information.

        Get the name of a Workflows webhook handle from the Datadog Microsoft Teams integration.

        :param handle_id: Your Workflows webhook handle id.
        :type handle_id: str
        :rtype: MicrosoftTeamsWorkflowsWebhookHandleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["handle_id"] = handle_id

        return self._get_workflows_webhook_handle_endpoint.call_with_http_info(**kwargs)

    def list_tenant_based_handles(
        self,
        *,
        tenant_id: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
    ) -> MicrosoftTeamsTenantBasedHandlesResponse:
        """Get all tenant-based handles.

        Get a list of all tenant-based handles from the Datadog Microsoft Teams integration.

        :param tenant_id: Your tenant id.
        :type tenant_id: str, optional
        :param name: Your tenant-based handle name.
        :type name: str, optional
        :rtype: MicrosoftTeamsTenantBasedHandlesResponse
        """
        kwargs: Dict[str, Any] = {}
        if tenant_id is not unset:
            kwargs["tenant_id"] = tenant_id

        if name is not unset:
            kwargs["name"] = name

        return self._list_tenant_based_handles_endpoint.call_with_http_info(**kwargs)

    def list_workflows_webhook_handles(
        self,
        *,
        name: Union[str, UnsetType] = unset,
    ) -> MicrosoftTeamsWorkflowsWebhookHandlesResponse:
        """Get all Workflows webhook handles.

        Get a list of all Workflows webhook handles from the Datadog Microsoft Teams integration.

        :param name: Your Workflows webhook handle name.
        :type name: str, optional
        :rtype: MicrosoftTeamsWorkflowsWebhookHandlesResponse
        """
        kwargs: Dict[str, Any] = {}
        if name is not unset:
            kwargs["name"] = name

        return self._list_workflows_webhook_handles_endpoint.call_with_http_info(**kwargs)

    def update_tenant_based_handle(
        self,
        handle_id: str,
        body: MicrosoftTeamsUpdateTenantBasedHandleRequest,
    ) -> MicrosoftTeamsTenantBasedHandleResponse:
        """Update tenant-based handle.

        Update a tenant-based handle from the Datadog Microsoft Teams integration.

        :param handle_id: Your tenant-based handle id.
        :type handle_id: str
        :param body: Tenant-based handle payload.
        :type body: MicrosoftTeamsUpdateTenantBasedHandleRequest
        :rtype: MicrosoftTeamsTenantBasedHandleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["handle_id"] = handle_id

        kwargs["body"] = body

        return self._update_tenant_based_handle_endpoint.call_with_http_info(**kwargs)

    def update_workflows_webhook_handle(
        self,
        handle_id: str,
        body: MicrosoftTeamsUpdateWorkflowsWebhookHandleRequest,
    ) -> MicrosoftTeamsWorkflowsWebhookHandleResponse:
        """Update Workflows webhook handle.

        Update a Workflows webhook handle from the Datadog Microsoft Teams integration.

        :param handle_id: Your Workflows webhook handle id.
        :type handle_id: str
        :param body: Workflows Webhook handle payload.
        :type body: MicrosoftTeamsUpdateWorkflowsWebhookHandleRequest
        :rtype: MicrosoftTeamsWorkflowsWebhookHandleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["handle_id"] = handle_id

        kwargs["body"] = body

        return self._update_workflows_webhook_handle_endpoint.call_with_http_info(**kwargs)
