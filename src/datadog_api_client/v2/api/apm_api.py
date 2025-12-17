# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.service_list import ServiceList


class APMApi:
    """
    Observe, troubleshoot, and improve cloud-scale applications with all telemetry in context
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._get_service_list_endpoint = _Endpoint(
            settings={
                "response_type": (ServiceList,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/apm/services",
                "operation_id": "get_service_list",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def get_service_list(
        self,
    ) -> ServiceList:
        """Get service list.

        :rtype: ServiceList
        """
        kwargs: Dict[str, Any] = {}
        return self._get_service_list_endpoint.call_with_http_info(**kwargs)
