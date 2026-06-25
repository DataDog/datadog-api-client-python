# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.governance_controls_response import GovernanceControlsResponse
from datadog_api_client.v2.model.governance_control_response import GovernanceControlResponse
from datadog_api_client.v2.model.governance_control_update_request import GovernanceControlUpdateRequest


class GovernanceControlsApi:
    """
    Governance Controls pair a detection definition with an organization's detection, notification,
    and mitigation configuration within the Governance Console. Each control reports how a class of
    governance issue (such as unused API keys or unqueried metrics) is detected and remediated, along
    with counts of active and mitigated detections.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._get_governance_control_endpoint = _Endpoint(
            settings={
                "response_type": (GovernanceControlResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/governance/control/{detection_type}",
                "operation_id": "get_governance_control",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "detection_type": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "detection_type",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_governance_controls_endpoint = _Endpoint(
            settings={
                "response_type": (GovernanceControlsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/governance/control",
                "operation_id": "list_governance_controls",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_governance_control_endpoint = _Endpoint(
            settings={
                "response_type": (GovernanceControlResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/governance/control/{detection_type}",
                "operation_id": "update_governance_control",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "detection_type": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "detection_type",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (GovernanceControlUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def get_governance_control(
        self,
        detection_type: str,
    ) -> GovernanceControlResponse:
        """Get a governance control.

        Retrieve a single governance control by its detection type, including the organization's current
        detection, notification, and mitigation configuration and detection counts.

        :param detection_type: The detection type that identifies the control, for example ``unused_api_keys``.
        :type detection_type: str
        :rtype: GovernanceControlResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["detection_type"] = detection_type

        return self._get_governance_control_endpoint.call_with_http_info(**kwargs)

    def list_governance_controls(
        self,
    ) -> GovernanceControlsResponse:
        """List governance controls.

        Retrieve the list of governance controls configured for the organization. Each control pairs a
        detection definition with the organization's current detection, notification, and mitigation
        configuration, along with counts of active and mitigated detections.

        :rtype: GovernanceControlsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_governance_controls_endpoint.call_with_http_info(**kwargs)

    def update_governance_control(
        self,
        detection_type: str,
        body: GovernanceControlUpdateRequest,
    ) -> GovernanceControlResponse:
        """Update a governance control.

        Update the detection, notification, and mitigation configuration of a governance control. Only
        the attributes present in the request are modified. Changing the mitigation type or its
        parameters may require additional permissions.

        :param detection_type: The detection type that identifies the control, for example ``unused_api_keys``.
        :type detection_type: str
        :type body: GovernanceControlUpdateRequest
        :rtype: GovernanceControlResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["detection_type"] = detection_type

        kwargs["body"] = body

        return self._update_governance_control_endpoint.call_with_http_info(**kwargs)
