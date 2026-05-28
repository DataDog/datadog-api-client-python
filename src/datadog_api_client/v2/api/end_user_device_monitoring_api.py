# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.device_base_array import DeviceBaseArray
from datadog_api_client.v2.model.device_details import DeviceDetails
from datadog_api_client.v2.model.graph_item_array import GraphItemArray
from datadog_api_client.v2.model.issue_definition_array import IssueDefinitionArray
from datadog_api_client.v2.model.overview_item_array import OverviewItemArray


class EndUserDeviceMonitoringApi:
    """
    Inspect devices reported by the Datadog Agent on end-user laptops, desktops,
    and mobile devices, including their health, hardware, and connectivity attributes.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._get_eudm_device_endpoint = _Endpoint(
            settings={
                "response_type": (DeviceDetails,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/eudm/devices/{device_id}",
                "operation_id": "get_eudm_device",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "device_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "device_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_eudm_devices_endpoint = _Endpoint(
            settings={
                "response_type": (DeviceBaseArray,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/eudm/devices",
                "operation_id": "get_eudm_devices",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_eudm_graph_endpoint = _Endpoint(
            settings={
                "response_type": (GraphItemArray,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/eudm/graph",
                "operation_id": "get_eudm_graph",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "by": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "by",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_eudm_issues_endpoint = _Endpoint(
            settings={
                "response_type": (IssueDefinitionArray,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/eudm/issues",
                "operation_id": "get_eudm_issues",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_eudm_overview_endpoint = _Endpoint(
            settings={
                "response_type": (OverviewItemArray,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/eudm/overview",
                "operation_id": "get_eudm_overview",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def get_eudm_device(
        self,
        device_id: str,
    ) -> DeviceDetails:
        """Get a device.

        :param device_id: Unique identifier of the device to fetch. Matches the Datadog host identifier.
        :type device_id: str
        :rtype: DeviceDetails
        """
        kwargs: Dict[str, Any] = {}
        kwargs["device_id"] = device_id

        return self._get_eudm_device_endpoint.call_with_http_info(**kwargs)

    def get_eudm_devices(
        self,
    ) -> DeviceBaseArray:
        """Get all devices.

        :rtype: DeviceBaseArray
        """
        kwargs: Dict[str, Any] = {}
        return self._get_eudm_devices_endpoint.call_with_http_info(**kwargs)

    def get_eudm_graph(
        self,
        by: str,
    ) -> GraphItemArray:
        """Get device counts grouped by attribute.

        :param by: Device attribute to group by (for example, ``os`` or ``type`` ).
            Determines which column the response counts are bucketed against.
        :type by: str
        :rtype: GraphItemArray
        """
        kwargs: Dict[str, Any] = {}
        kwargs["by"] = by

        return self._get_eudm_graph_endpoint.call_with_http_info(**kwargs)

    def get_eudm_issues(
        self,
    ) -> IssueDefinitionArray:
        """Get all device issue definitions.

        :rtype: IssueDefinitionArray
        """
        kwargs: Dict[str, Any] = {}
        return self._get_eudm_issues_endpoint.call_with_http_info(**kwargs)

    def get_eudm_overview(
        self,
    ) -> OverviewItemArray:
        """Get overview tiles.

        :rtype: OverviewItemArray
        """
        kwargs: Dict[str, Any] = {}
        return self._get_eudm_overview_endpoint.call_with_http_info(**kwargs)
