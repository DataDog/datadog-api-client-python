# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict
import warnings

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.dora_deployment_response import DORADeploymentResponse
from datadog_api_client.v2.model.dora_deployment_request import DORADeploymentRequest
from datadog_api_client.v2.model.dora_list_response import DORAListResponse
from datadog_api_client.v2.model.dora_list_deployments_request import DORAListDeploymentsRequest
from datadog_api_client.v2.model.dora_fetch_response import DORAFetchResponse
from datadog_api_client.v2.model.dora_failure_response import DORAFailureResponse
from datadog_api_client.v2.model.dora_failure_request import DORAFailureRequest
from datadog_api_client.v2.model.dora_list_failures_request import DORAListFailuresRequest


class DORAMetricsApi:
    """
    Search or send events for DORA Metrics to measure and improve your software delivery performance. See the `DORA Metrics page <https://docs.datadoghq.com/dora_metrics/>`_ for more information.

    **Note** : DORA Metrics are not available in the US1-FED site.
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

        self._create_dora_failure_endpoint = _Endpoint(
            settings={
                "response_type": (DORAFailureResponse,),
                "auth": ["apiKeyAuth"],
                "endpoint_path": "/api/v2/dora/failure",
                "operation_id": "create_dora_failure",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (DORAFailureRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_dora_incident_endpoint = _Endpoint(
            settings={
                "response_type": (DORAFailureResponse,),
                "auth": ["apiKeyAuth"],
                "endpoint_path": "/api/v2/dora/incident",
                "operation_id": "create_dora_incident",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (DORAFailureRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._get_dora_deployment_endpoint = _Endpoint(
            settings={
                "response_type": (DORAFetchResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/dora/deployments/{deployment_id}",
                "operation_id": "get_dora_deployment",
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

        self._get_dora_failure_endpoint = _Endpoint(
            settings={
                "response_type": (DORAFetchResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/dora/failures/{failure_id}",
                "operation_id": "get_dora_failure",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "failure_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "failure_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_dora_deployments_endpoint = _Endpoint(
            settings={
                "response_type": (DORAListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/dora/deployments",
                "operation_id": "list_dora_deployments",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (DORAListDeploymentsRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._list_dora_failures_endpoint = _Endpoint(
            settings={
                "response_type": (DORAListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/dora/failures",
                "operation_id": "list_dora_failures",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (DORAListFailuresRequest,),
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

    def create_dora_failure(
        self,
        body: DORAFailureRequest,
    ) -> DORAFailureResponse:
        """Send a failure event for DORA Metrics.

        Use this API endpoint to provide failure data for DORA metrics.

        This is necessary for:

        * Change Failure Rate
        * Time to Restore

        :type body: DORAFailureRequest
        :rtype: DORAFailureResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_dora_failure_endpoint.call_with_http_info(**kwargs)

    def create_dora_incident(
        self,
        body: DORAFailureRequest,
    ) -> DORAFailureResponse:
        """Send an incident event for DORA Metrics. **Deprecated**.

        **Note** : This endpoint is deprecated. Please use ``/api/v2/dora/failure`` instead.

        Use this API endpoint to provide failure data for DORA metrics.

        This is necessary for:

        * Change Failure Rate
        * Time to Restore

        :type body: DORAFailureRequest
        :rtype: DORAFailureResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        warnings.warn("create_dora_incident is deprecated", DeprecationWarning, stacklevel=2)
        return self._create_dora_incident_endpoint.call_with_http_info(**kwargs)

    def get_dora_deployment(
        self,
        deployment_id: str,
    ) -> DORAFetchResponse:
        """Get a deployment event.

        Use this API endpoint to get a deployment event.

        :param deployment_id: The ID of the deployment event.
        :type deployment_id: str
        :rtype: DORAFetchResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["deployment_id"] = deployment_id

        return self._get_dora_deployment_endpoint.call_with_http_info(**kwargs)

    def get_dora_failure(
        self,
        failure_id: str,
    ) -> DORAFetchResponse:
        """Get a failure event.

        Use this API endpoint to get a failure event.

        :param failure_id: The ID of the failure event.
        :type failure_id: str
        :rtype: DORAFetchResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["failure_id"] = failure_id

        return self._get_dora_failure_endpoint.call_with_http_info(**kwargs)

    def list_dora_deployments(
        self,
        body: DORAListDeploymentsRequest,
    ) -> DORAListResponse:
        """Get a list of deployment events.

        Use this API endpoint to get a list of deployment events.

        :type body: DORAListDeploymentsRequest
        :rtype: DORAListResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._list_dora_deployments_endpoint.call_with_http_info(**kwargs)

    def list_dora_failures(
        self,
        body: DORAListFailuresRequest,
    ) -> DORAListResponse:
        """Get a list of failure events.

        Use this API endpoint to get a list of failure events.

        :type body: DORAListFailuresRequest
        :rtype: DORAListResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._list_dora_failures_endpoint.call_with_http_info(**kwargs)
