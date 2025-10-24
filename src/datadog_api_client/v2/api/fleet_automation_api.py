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
from datadog_api_client.v2.model.fleet_deployments_response import FleetDeploymentsResponse
from datadog_api_client.v2.model.fleet_deployment_response import FleetDeploymentResponse
from datadog_api_client.v2.model.fleet_deployment_configure_create_request import FleetDeploymentConfigureCreateRequest


class FleetAutomationApi:
    """
    Manage automated deployments across your fleet of hosts.
    Use these endpoints to create, retrieve, and cancel deployments
    that apply configuration changes to multiple hosts at once.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._cancel_fleet_deployment_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/unstable/fleet/deployments/{deployment_id}/cancel",
                "operation_id": "cancel_fleet_deployment",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "deployment_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "deployment_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._create_fleet_deployment_configure_endpoint = _Endpoint(
            settings={
                "response_type": (FleetDeploymentResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/unstable/fleet/deployments/configure",
                "operation_id": "create_fleet_deployment_configure",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (FleetDeploymentConfigureCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._get_fleet_deployment_endpoint = _Endpoint(
            settings={
                "response_type": (FleetDeploymentResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/unstable/fleet/deployments/{deployment_id}",
                "operation_id": "get_fleet_deployment",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "deployment_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "deployment_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_fleet_deployments_endpoint = _Endpoint(
            settings={
                "response_type": (FleetDeploymentsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/unstable/fleet/deployments",
                "operation_id": "list_fleet_deployments",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_size": {
                    "validation": {
                        "inclusive_maximum": 100,
                    },
                    "openapi_types": (int,),
                    "attribute": "page_size",
                    "location": "query",
                },
                "page_offset": {
                    "openapi_types": (int,),
                    "attribute": "page_offset",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def cancel_fleet_deployment(
        self,
        deployment_id: str,
    ) -> None:
        """Cancel a deployment.

        Cancel this deployment and stop all associated operations.
        If a workflow is currently running for this deployment, it is canceled immediately.
        Changes already applied to hosts are not rolled back.

        :param deployment_id: The unique identifier of the deployment to cancel.
        :type deployment_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["deployment_id"] = deployment_id

        return self._cancel_fleet_deployment_endpoint.call_with_http_info(**kwargs)

    def create_fleet_deployment_configure(
        self,
        body: FleetDeploymentConfigureCreateRequest,
    ) -> FleetDeploymentResponse:
        """Create a deployment.

        Create a new deployment to apply configuration changes
        to a fleet of hosts matching the specified filter query.

        :param body: Request payload containing the deployment details.
        :type body: FleetDeploymentConfigureCreateRequest
        :rtype: FleetDeploymentResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_fleet_deployment_configure_endpoint.call_with_http_info(**kwargs)

    def get_fleet_deployment(
        self,
        deployment_id: str,
    ) -> FleetDeploymentResponse:
        """Get a deployment by ID.

        Retrieve the details of a specific deployment using its unique identifier.

        :param deployment_id: The unique identifier of the deployment to retrieve.
        :type deployment_id: str
        :rtype: FleetDeploymentResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["deployment_id"] = deployment_id

        return self._get_fleet_deployment_endpoint.call_with_http_info(**kwargs)

    def list_fleet_deployments(
        self,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
    ) -> FleetDeploymentsResponse:
        """List all deployments.

        Retrieve a list of all deployments for fleet automation.
        Use the ``page_size`` and ``page_offset`` parameters to paginate results.

        :param page_size: Number of deployments to return per page. Maximum value is 100.
        :type page_size: int, optional
        :param page_offset: Index of the first deployment to return. Use this with ``page_size`` to paginate through results.
        :type page_offset: int, optional
        :rtype: FleetDeploymentsResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        return self._list_fleet_deployments_endpoint.call_with_http_info(**kwargs)
