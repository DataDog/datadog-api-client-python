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
from datadog_api_client.v2.model.list_devices_response import ListDevicesResponse
from datadog_api_client.v2.model.get_device_response import GetDeviceResponse
from datadog_api_client.v2.model.get_interfaces_response import GetInterfacesResponse
from datadog_api_client.v2.model.list_tags_response import ListTagsResponse


class NetworkDeviceMonitoringApi:
    """
    The Network Device Monitoring API allows you to fetch devices and interfaces and their attributes. See the `Network Device Monitoring page <https://docs.datadoghq.com/network_monitoring/>`_ for more information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._get_device_endpoint = _Endpoint(
            settings={
                "response_type": (GetDeviceResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/ndm/devices/{device_id}",
                "operation_id": "get_device",
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

        self._get_interfaces_endpoint = _Endpoint(
            settings={
                "response_type": (GetInterfacesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/ndm/interfaces",
                "operation_id": "get_interfaces",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "device_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "device_id",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_devices_endpoint = _Endpoint(
            settings={
                "response_type": (ListDevicesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/ndm/devices",
                "operation_id": "list_devices",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_number": {
                    "openapi_types": (int,),
                    "attribute": "page[number]",
                    "location": "query",
                },
                "page_size": {
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (str,),
                    "attribute": "sort",
                    "location": "query",
                },
                "filter_tag": {
                    "openapi_types": (str,),
                    "attribute": "filter[tag]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_device_user_tags_endpoint = _Endpoint(
            settings={
                "response_type": (ListTagsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/ndm/tags/devices/{device_id}",
                "operation_id": "list_device_user_tags",
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

        self._update_device_user_tags_endpoint = _Endpoint(
            settings={
                "response_type": (ListTagsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/ndm/tags/devices/{device_id}",
                "operation_id": "update_device_user_tags",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "device_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "device_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ListTagsResponse,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def get_device(
        self,
        device_id: str,
    ) -> GetDeviceResponse:
        """Get the device details.

        Get the device details.

        :param device_id: The id of the device to fetch.
        :type device_id: str
        :rtype: GetDeviceResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["device_id"] = device_id

        return self._get_device_endpoint.call_with_http_info(**kwargs)

    def get_interfaces(
        self,
        device_id: str,
    ) -> GetInterfacesResponse:
        """Get the list of interfaces of the device.

        Get the list of interfaces of the device.

        :param device_id: The ID of the device to get interfaces from.
        :type device_id: str
        :rtype: GetInterfacesResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["device_id"] = device_id

        return self._get_interfaces_endpoint.call_with_http_info(**kwargs)

    def list_devices(
        self,
        *,
        page_number: Union[int, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        sort: Union[str, UnsetType] = unset,
        filter_tag: Union[str, UnsetType] = unset,
    ) -> ListDevicesResponse:
        """Get the list of devices.

        Get the list of devices.

        :param page_number: The page number to fetch.
        :type page_number: int, optional
        :param page_size: The number of devices to return per page.
        :type page_size: int, optional
        :param sort: The field to sort the devices by.
        :type sort: str, optional
        :param filter_tag: Filter devices by tag.
        :type filter_tag: str, optional
        :rtype: ListDevicesResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_number is not unset:
            kwargs["page_number"] = page_number

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if sort is not unset:
            kwargs["sort"] = sort

        if filter_tag is not unset:
            kwargs["filter_tag"] = filter_tag

        return self._list_devices_endpoint.call_with_http_info(**kwargs)

    def list_device_user_tags(
        self,
        device_id: str,
    ) -> ListTagsResponse:
        """Get the list of tags for a device.

        Get the list of tags for a device.

        :param device_id: The id of the device to fetch tags for.
        :type device_id: str
        :rtype: ListTagsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["device_id"] = device_id

        return self._list_device_user_tags_endpoint.call_with_http_info(**kwargs)

    def update_device_user_tags(
        self,
        device_id: str,
        body: ListTagsResponse,
    ) -> ListTagsResponse:
        """Update the tags for a device.

        Update the tags for a device.

        :param device_id: The id of the device to update tags for.
        :type device_id: str
        :type body: ListTagsResponse
        :rtype: ListTagsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["device_id"] = device_id

        kwargs["body"] = body

        return self._update_device_user_tags_endpoint.call_with_http_info(**kwargs)
