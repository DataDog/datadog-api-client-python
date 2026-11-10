# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.device_base_array import DeviceBaseArray
from datadog_api_client.v2.model.device_details import DeviceDetails


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
                "auth": ["apiKeyAuth", "appKeyAuth"],
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
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/eudm/devices",
                "operation_id": "get_eudm_devices",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "bssid": {
                    "openapi_types": ([str],),
                    "attribute": "bssid",
                    "location": "query",
                    "collection_format": "multi",
                },
                "page_limit": {
                    "validation": {
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[limit]",
                    "location": "query",
                },
                "page_cursor": {
                    "openapi_types": (str,),
                    "attribute": "page[cursor]",
                    "location": "query",
                },
            },
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
        *,
        bssid: Union[List[str], UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
        page_cursor: Union[str, UnsetType] = unset,
    ) -> DeviceBaseArray:
        """Get all devices.

        :param bssid: Filter devices to those currently associated with any of the given BSSID values.
            Each value must be a MAC-48 address; repeat the parameter to pass several values.
        :type bssid: [str], optional
        :param page_limit: Maximum number of devices to return in one page. Must be a positive integer.
            If not set, the response contains all matching devices.
        :type page_limit: int, optional
        :param page_cursor: Opaque cursor that selects the next page. Use the ``meta.page.after`` value
            of the previous response. Devices are ordered by ID.
        :type page_cursor: str, optional
        :rtype: DeviceBaseArray
        """
        kwargs: Dict[str, Any] = {}
        if bssid is not unset:
            kwargs["bssid"] = bssid

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        if page_cursor is not unset:
            kwargs["page_cursor"] = page_cursor

        return self._get_eudm_devices_endpoint.call_with_http_info(**kwargs)
