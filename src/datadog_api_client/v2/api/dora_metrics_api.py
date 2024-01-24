# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.dora_deployment_response import DORADeploymentResponse
from datadog_api_client.v2.model.dora_deployment_request import DORADeploymentRequest
from datadog_api_client.v2.model.dora_incident_response import DORAIncidentResponse
from datadog_api_client.v2.model.dora_incident_request import DORAIncidentRequest


class DORAMetricsApi:
    """
    Send events for DORA Metrics to measure and improve software delivery. See the `DORA Metrics page <https://docs.datadoghq.com/dora_metrics/>`_ for more information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_dora_deployment_endpoint = _Endpoint(
            settings={
                "response_type": (DORADeploymentResponse,),
                "auth": ["apiKeyAuth"],
                "endpoint_path": "/api/v2/dora/deployment",
                "operation_id": "create_dora_deployment",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (DORADeploymentRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_dora_incident_endpoint = _Endpoint(
            settings={
                "response_type": (DORAIncidentResponse,),
                "auth": ["apiKeyAuth"],
                "endpoint_path": "/api/v2/dora/incident",
                "operation_id": "create_dora_incident",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (DORAIncidentRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_dora_deployment(
        self,
        body: DORADeploymentRequest,
    ) -> DORADeploymentResponse:
        """Send a deployment event for DORA Metrics.

        Use this API endpoint to provide data about deployments for DORA metrics.

        This is necessary for:

        * Deployment Frequency
        * Change Lead Time
        * Change Failure Rate

        :type body: DORADeploymentRequest
        :rtype: DORADeploymentResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_dora_deployment_endpoint.call_with_http_info(**kwargs)

    def create_dora_incident(
        self,
        body: DORAIncidentRequest,
    ) -> DORAIncidentResponse:
        """Send an incident event for DORA Metrics.

        Use this API endpoint to provide data about incidents for DORA metrics.

        This is necessary for:

        * Change Failure Rate
        * Time to Restore

        :type body: DORAIncidentRequest
        :rtype: DORAIncidentResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_dora_incident_endpoint.call_with_http_info(**kwargs)
