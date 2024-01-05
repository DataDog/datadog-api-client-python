# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

import collections
from typing import Any, Dict, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    set_attribute_from_path,
    get_attribute_from_path,
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.list_downtimes_response import ListDowntimesResponse
from datadog_api_client.v2.model.downtime_response_data import DowntimeResponseData
from datadog_api_client.v2.model.downtime_response import DowntimeResponse
from datadog_api_client.v2.model.downtime_create_request import DowntimeCreateRequest
from datadog_api_client.v2.model.downtime_update_request import DowntimeUpdateRequest
from datadog_api_client.v2.model.monitor_downtime_match_response import MonitorDowntimeMatchResponse
from datadog_api_client.v2.model.monitor_downtime_match_response_data import MonitorDowntimeMatchResponseData


class DowntimesApi:
    """
    **Note** : Downtime V2 is currently in private beta. To request access, contact `Datadog support <https://docs.datadoghq.com/help/>`_.

    `Downtiming <https://docs.datadoghq.com/monitors/notify/downtimes>`_ gives
    you greater control over monitor notifications by allowing you to globally exclude
    scopes from alerting. Downtime settings, which can be scheduled with start and
    end times, prevent all alerting related to specified Datadog tags.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._cancel_downtime_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/downtime/{downtime_id}",
                "operation_id": "cancel_downtime",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "downtime_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "downtime_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._create_downtime_endpoint = _Endpoint(
            settings={
                "response_type": (DowntimeResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/downtime",
                "operation_id": "create_downtime",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (DowntimeCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._get_downtime_endpoint = _Endpoint(
            settings={
                "response_type": (DowntimeResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/downtime/{downtime_id}",
                "operation_id": "get_downtime",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "downtime_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "downtime_id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_downtimes_endpoint = _Endpoint(
            settings={
                "response_type": (ListDowntimesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/downtime",
                "operation_id": "list_downtimes",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "current_only": {
                    "openapi_types": (bool,),
                    "attribute": "current_only",
                    "location": "query",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
                "page_offset": {
                    "openapi_types": (int,),
                    "attribute": "page[offset]",
                    "location": "query",
                },
                "page_limit": {
                    "openapi_types": (int,),
                    "attribute": "page[limit]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_monitor_downtimes_endpoint = _Endpoint(
            settings={
                "response_type": (MonitorDowntimeMatchResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/monitor/{monitor_id}/downtime_matches",
                "operation_id": "list_monitor_downtimes",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "monitor_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "monitor_id",
                    "location": "path",
                },
                "page_offset": {
                    "openapi_types": (int,),
                    "attribute": "page[offset]",
                    "location": "query",
                },
                "page_limit": {
                    "openapi_types": (int,),
                    "attribute": "page[limit]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_downtime_endpoint = _Endpoint(
            settings={
                "response_type": (DowntimeResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/downtime/{downtime_id}",
                "operation_id": "update_downtime",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "downtime_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "downtime_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (DowntimeUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def cancel_downtime(
        self,
        downtime_id: str,
    ) -> None:
        """Cancel a downtime.

        Cancel a downtime.

        :param downtime_id: ID of the downtime to cancel.
        :type downtime_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["downtime_id"] = downtime_id

        return self._cancel_downtime_endpoint.call_with_http_info(**kwargs)

    def create_downtime(
        self,
        body: DowntimeCreateRequest,
    ) -> DowntimeResponse:
        """Schedule a downtime.

        Schedule a downtime.

        :param body: Schedule a downtime request body.
        :type body: DowntimeCreateRequest
        :rtype: DowntimeResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_downtime_endpoint.call_with_http_info(**kwargs)

    def get_downtime(
        self,
        downtime_id: str,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> DowntimeResponse:
        """Get a downtime.

        Get downtime detail by ``downtime_id``.

        :param downtime_id: ID of the downtime to fetch.
        :type downtime_id: str
        :param include: Comma-separated list of resource paths for related resources to include in the response. Supported resource
            paths are ``created_by`` and ``monitor``.
        :type include: str, optional
        :rtype: DowntimeResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["downtime_id"] = downtime_id

        if include is not unset:
            kwargs["include"] = include

        return self._get_downtime_endpoint.call_with_http_info(**kwargs)

    def list_downtimes(
        self,
        *,
        current_only: Union[bool, UnsetType] = unset,
        include: Union[str, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
    ) -> ListDowntimesResponse:
        """Get all downtimes.

        Get all scheduled downtimes.

        :param current_only: Only return downtimes that are active when the request is made.
        :type current_only: bool, optional
        :param include: Comma-separated list of resource paths for related resources to include in the response. Supported resource
            paths are ``created_by`` and ``monitor``.
        :type include: str, optional
        :param page_offset: Specific offset to use as the beginning of the returned page.
        :type page_offset: int, optional
        :param page_limit: Maximum number of downtimes in the response.
        :type page_limit: int, optional
        :rtype: ListDowntimesResponse
        """
        kwargs: Dict[str, Any] = {}
        if current_only is not unset:
            kwargs["current_only"] = current_only

        if include is not unset:
            kwargs["include"] = include

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        return self._list_downtimes_endpoint.call_with_http_info(**kwargs)

    def list_downtimes_with_pagination(
        self,
        *,
        current_only: Union[bool, UnsetType] = unset,
        include: Union[str, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
    ) -> collections.abc.Iterable[DowntimeResponseData]:
        """Get all downtimes.

        Provide a paginated version of :meth:`list_downtimes`, returning all items.

        :param current_only: Only return downtimes that are active when the request is made.
        :type current_only: bool, optional
        :param include: Comma-separated list of resource paths for related resources to include in the response. Supported resource
            paths are ``created_by`` and ``monitor``.
        :type include: str, optional
        :param page_offset: Specific offset to use as the beginning of the returned page.
        :type page_offset: int, optional
        :param page_limit: Maximum number of downtimes in the response.
        :type page_limit: int, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[DowntimeResponseData]
        """
        kwargs: Dict[str, Any] = {}
        if current_only is not unset:
            kwargs["current_only"] = current_only

        if include is not unset:
            kwargs["include"] = include

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        local_page_size = get_attribute_from_path(kwargs, "page_limit", 30)
        endpoint = self._list_downtimes_endpoint
        set_attribute_from_path(kwargs, "page_limit", local_page_size, endpoint.params_map)
        pagination = {
            "limit_value": local_page_size,
            "results_path": "data",
            "page_offset_param": "page_offset",
            "endpoint": endpoint,
            "kwargs": kwargs,
        }
        return endpoint.call_with_http_info_paginated(pagination)

    def list_monitor_downtimes(
        self,
        monitor_id: int,
        *,
        page_offset: Union[int, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
    ) -> MonitorDowntimeMatchResponse:
        """Get active downtimes for a monitor.

        Get all active downtimes for the specified monitor.

        :param monitor_id: The id of the monitor.
        :type monitor_id: int
        :param page_offset: Specific offset to use as the beginning of the returned page.
        :type page_offset: int, optional
        :param page_limit: Maximum number of downtimes in the response.
        :type page_limit: int, optional
        :rtype: MonitorDowntimeMatchResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["monitor_id"] = monitor_id

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        return self._list_monitor_downtimes_endpoint.call_with_http_info(**kwargs)

    def list_monitor_downtimes_with_pagination(
        self,
        monitor_id: int,
        *,
        page_offset: Union[int, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
    ) -> collections.abc.Iterable[MonitorDowntimeMatchResponseData]:
        """Get active downtimes for a monitor.

        Provide a paginated version of :meth:`list_monitor_downtimes`, returning all items.

        :param monitor_id: The id of the monitor.
        :type monitor_id: int
        :param page_offset: Specific offset to use as the beginning of the returned page.
        :type page_offset: int, optional
        :param page_limit: Maximum number of downtimes in the response.
        :type page_limit: int, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[MonitorDowntimeMatchResponseData]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["monitor_id"] = monitor_id

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        local_page_size = get_attribute_from_path(kwargs, "page_limit", 30)
        endpoint = self._list_monitor_downtimes_endpoint
        set_attribute_from_path(kwargs, "page_limit", local_page_size, endpoint.params_map)
        pagination = {
            "limit_value": local_page_size,
            "results_path": "data",
            "page_offset_param": "page_offset",
            "endpoint": endpoint,
            "kwargs": kwargs,
        }
        return endpoint.call_with_http_info_paginated(pagination)

    def update_downtime(
        self,
        downtime_id: str,
        body: DowntimeUpdateRequest,
    ) -> DowntimeResponse:
        """Update a downtime.

        Update a downtime by ``downtime_id``.

        :param downtime_id: ID of the downtime to update.
        :type downtime_id: str
        :param body: Update a downtime request body.
        :type body: DowntimeUpdateRequest
        :rtype: DowntimeResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["downtime_id"] = downtime_id

        kwargs["body"] = body

        return self._update_downtime_endpoint.call_with_http_info(**kwargs)
