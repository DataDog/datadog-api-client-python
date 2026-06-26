# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.governance_config_response import GovernanceConfigResponse
from datadog_api_client.v2.model.governance_limits_response import GovernanceLimitsResponse
from datadog_api_client.v2.model.governance_notification_settings_response import GovernanceNotificationSettingsResponse
from datadog_api_client.v2.model.governance_notification_settings_update_request import (
    GovernanceNotificationSettingsUpdateRequest,
)
from datadog_api_client.v2.model.governance_resource_limits_response import GovernanceResourceLimitsResponse


class GovernanceSettingsApi:
    """
    Governance Settings cover organization-wide Governance Console configuration, usage limits and
    resource limits, and notification preferences that determine when and how the Console alerts
    users about governance activity.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._get_governance_config_endpoint = _Endpoint(
            settings={
                "response_type": (GovernanceConfigResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/governance/config",
                "operation_id": "get_governance_config",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_governance_notification_settings_endpoint = _Endpoint(
            settings={
                "response_type": (GovernanceNotificationSettingsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/governance/notification_settings",
                "operation_id": "get_governance_notification_settings",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_governance_limits_endpoint = _Endpoint(
            settings={
                "response_type": (GovernanceLimitsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/governance/limits",
                "operation_id": "list_governance_limits",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_governance_resource_limits_endpoint = _Endpoint(
            settings={
                "response_type": (GovernanceResourceLimitsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/governance/resource-limits",
                "operation_id": "list_governance_resource_limits",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_governance_notification_settings_endpoint = _Endpoint(
            settings={
                "response_type": (GovernanceNotificationSettingsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/governance/notification_settings",
                "operation_id": "update_governance_notification_settings",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (GovernanceNotificationSettingsUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def get_governance_config(
        self,
    ) -> GovernanceConfigResponse:
        """Get the governance console configuration.

        Retrieve the Governance Console configuration for the organization, including whether the
        Console is enabled, whether assignment notifications are enabled, and whether usage
        attribution is configured.

        :rtype: GovernanceConfigResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._get_governance_config_endpoint.call_with_http_info(**kwargs)

    def get_governance_notification_settings(
        self,
    ) -> GovernanceNotificationSettingsResponse:
        """Get governance notification settings.

        Retrieve the organization-wide governance notification settings, including whether users are
        notified when detections are assigned to them.

        :rtype: GovernanceNotificationSettingsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._get_governance_notification_settings_endpoint.call_with_http_info(**kwargs)

    def list_governance_limits(
        self,
    ) -> GovernanceLimitsResponse:
        """List governance limits.

        Retrieve the list of usage limits tracked for the organization in the Governance Console.
        Each limit reports the query used to compute current usage, the unit and time range it is
        measured over, and its current usage status.

        :rtype: GovernanceLimitsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_governance_limits_endpoint.call_with_http_info(**kwargs)

    def list_governance_resource_limits(
        self,
    ) -> GovernanceResourceLimitsResponse:
        """List governance resource limits.

        Retrieve the list of resource limits tracked for the organization in the Governance Console.
        Each resource limit reports its current value and configured limit, the queries used to
        compute them, and its current usage status.

        :rtype: GovernanceResourceLimitsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_governance_resource_limits_endpoint.call_with_http_info(**kwargs)

    def update_governance_notification_settings(
        self,
        body: GovernanceNotificationSettingsUpdateRequest,
    ) -> GovernanceNotificationSettingsResponse:
        """Update governance notification settings.

        Update the organization-wide governance notification settings. Only the attributes present in
        the request are modified.

        :type body: GovernanceNotificationSettingsUpdateRequest
        :rtype: GovernanceNotificationSettingsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._update_governance_notification_settings_endpoint.call_with_http_info(**kwargs)
