# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.get_data_observability_monitor_run_status_response import (
    GetDataObservabilityMonitorRunStatusResponse,
)
from datadog_api_client.v2.model.run_data_observability_monitor_response import RunDataObservabilityMonitorResponse


class DataObservabilityApi:
    """
    Manage and run data observability monitors.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._get_data_observability_monitor_run_status_endpoint = _Endpoint(
            settings={
                "response_type": (GetDataObservabilityMonitorRunStatusResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/data-observability/monitors/runs/{run_id}/status",
                "operation_id": "get_data_observability_monitor_run_status",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "run_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "run_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._run_data_observability_monitor_endpoint = _Endpoint(
            settings={
                "response_type": (RunDataObservabilityMonitorResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/data-observability/monitors/{monitor_id}/run",
                "operation_id": "run_data_observability_monitor",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "monitor_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "monitor_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def get_data_observability_monitor_run_status(
        self,
        run_id: str,
    ) -> GetDataObservabilityMonitorRunStatusResponse:
        """Get data observability monitor run status.

        Retrieves the current status of a data observability monitor run. Poll this endpoint after triggering a run to determine when evaluation is complete.

        :param run_id: The ID of the monitor run to retrieve status for.
        :type run_id: str
        :rtype: GetDataObservabilityMonitorRunStatusResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["run_id"] = run_id

        return self._get_data_observability_monitor_run_status_endpoint.call_with_http_info(**kwargs)

    def run_data_observability_monitor(
        self,
        monitor_id: int,
    ) -> RunDataObservabilityMonitorResponse:
        """Run a data observability monitor.

        Manually triggers a run for a data observability monitor. Only monitors that are not scheduled (manually-runnable) can be triggered this way.

        :param monitor_id: The ID of the data observability monitor to run.
        :type monitor_id: int
        :rtype: RunDataObservabilityMonitorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["monitor_id"] = monitor_id

        return self._run_data_observability_monitor_endpoint.call_with_http_info(**kwargs)
