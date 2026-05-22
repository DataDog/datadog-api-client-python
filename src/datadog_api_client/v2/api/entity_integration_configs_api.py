# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.entity_integration_config_response import EntityIntegrationConfigResponse
from datadog_api_client.v2.model.entity_integration_config_request import EntityIntegrationConfigRequest


class EntityIntegrationConfigsApi:
    """
    Manage per-integration configurations for the Internal Developer Portal (IDP). These configurations control which external resources (for example, GitHub repositories, Jira projects, or PagerDuty services) are synced as entities into the Software Catalog.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._delete_entity_integration_config_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/idp/entity_integrations/{integration_id}",
                "operation_id": "delete_entity_integration_config",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "integration_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "integration_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_entity_integration_config_endpoint = _Endpoint(
            settings={
                "response_type": (EntityIntegrationConfigResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/idp/entity_integrations/{integration_id}",
                "operation_id": "get_entity_integration_config",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "integration_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "integration_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_entity_integration_config_endpoint = _Endpoint(
            settings={
                "response_type": (EntityIntegrationConfigResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/idp/entity_integrations/{integration_id}",
                "operation_id": "update_entity_integration_config",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "integration_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "integration_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (EntityIntegrationConfigRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def delete_entity_integration_config(
        self,
        integration_id: str,
    ) -> None:
        """Delete an entity integration configuration.

        Delete the configuration stored for a given integration in the caller's organization.

        :param integration_id: The identifier of the integration whose configuration is being managed. Supported values are ``github`` , ``jira`` , and ``pagerduty``.
        :type integration_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["integration_id"] = integration_id

        return self._delete_entity_integration_config_endpoint.call_with_http_info(**kwargs)

    def get_entity_integration_config(
        self,
        integration_id: str,
    ) -> EntityIntegrationConfigResponse:
        """Get an entity integration configuration.

        Retrieve the configuration currently stored for a given integration in the caller's organization.

        :param integration_id: The identifier of the integration whose configuration is being managed. Supported values are ``github`` , ``jira`` , and ``pagerduty``.
        :type integration_id: str
        :rtype: EntityIntegrationConfigResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["integration_id"] = integration_id

        return self._get_entity_integration_config_endpoint.call_with_http_info(**kwargs)

    def update_entity_integration_config(
        self,
        integration_id: str,
        body: EntityIntegrationConfigRequest,
    ) -> EntityIntegrationConfigResponse:
        """Create or update entity integration configuration.

        Create or replace the configuration for a given integration in the caller's organization. The shape of ``data.attributes.config`` depends on the integration:

        * For ``github`` : ``config`` must contain an ``enabled_repos`` array of objects with ``hostname`` , ``github_org_name`` , and ``repo_name``.
        * For ``jira`` : ``config`` must contain an ``enabled_projects`` array of objects with ``hostname`` , ``account_id`` , and ``project_key``.
        * For ``pagerduty`` : ``config`` must contain an ``accounts`` array of objects with a required ``enabled`` boolean and an optional ``subdomain`` string.

        :param integration_id: The identifier of the integration whose configuration is being managed. Supported values are ``github`` , ``jira`` , and ``pagerduty``.
        :type integration_id: str
        :type body: EntityIntegrationConfigRequest
        :rtype: EntityIntegrationConfigResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["integration_id"] = integration_id

        kwargs["body"] = body

        return self._update_entity_integration_config_endpoint.call_with_http_info(**kwargs)
