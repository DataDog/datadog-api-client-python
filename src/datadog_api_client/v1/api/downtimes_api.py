# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union
import warnings

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    UnsetType,
    unset,
)
from datadog_api_client.v1.model.downtime import Downtime
from datadog_api_client.v1.model.canceled_downtimes_ids import CanceledDowntimesIds
from datadog_api_client.v1.model.cancel_downtimes_by_scope_request import CancelDowntimesByScopeRequest


class DowntimesApi:
    """
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
                "endpoint_path": "/api/v1/downtime/{downtime_id}",
                "operation_id": "cancel_downtime",
                "http_method": "DELETE",
                "version": "v1",
            },
            params_map={
                "downtime_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "downtime_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._cancel_downtimes_by_scope_endpoint = _Endpoint(
            settings={
                "response_type": (CanceledDowntimesIds,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/downtime/cancel/by_scope",
                "operation_id": "cancel_downtimes_by_scope",
                "http_method": "POST",
                "version": "v1",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CancelDowntimesByScopeRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_downtime_endpoint = _Endpoint(
            settings={
                "response_type": (Downtime,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/downtime",
                "operation_id": "create_downtime",
                "http_method": "POST",
                "version": "v1",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (Downtime,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._get_downtime_endpoint = _Endpoint(
            settings={
                "response_type": (Downtime,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/downtime/{downtime_id}",
                "operation_id": "get_downtime",
                "http_method": "GET",
                "version": "v1",
            },
            params_map={
                "downtime_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "downtime_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_downtimes_endpoint = _Endpoint(
            settings={
                "response_type": ([Downtime],),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/downtime",
                "operation_id": "list_downtimes",
                "http_method": "GET",
                "version": "v1",
            },
            params_map={
                "current_only": {
                    "openapi_types": (bool,),
                    "attribute": "current_only",
                    "location": "query",
                },
                "with_creator": {
                    "openapi_types": (bool,),
                    "attribute": "with_creator",
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
                "response_type": ([Downtime],),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/monitor/{monitor_id}/downtimes",
                "operation_id": "list_monitor_downtimes",
                "http_method": "GET",
                "version": "v1",
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

        self._update_downtime_endpoint = _Endpoint(
            settings={
                "response_type": (Downtime,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/downtime/{downtime_id}",
                "operation_id": "update_downtime",
                "http_method": "PUT",
                "version": "v1",
            },
            params_map={
                "downtime_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "downtime_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (Downtime,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def cancel_downtime(
        self,
        downtime_id: int,
    ) -> None:
        """Cancel a downtime. **Deprecated**.

        Cancel a downtime. **Note:** This endpoint has been deprecated. Please use v2 endpoints.

        :param downtime_id: ID of the downtime to cancel.
        :type downtime_id: int
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["downtime_id"] = downtime_id

        warnings.warn("cancel_downtime is deprecated", DeprecationWarning, stacklevel=2)
        return self._cancel_downtime_endpoint.call_with_http_info(**kwargs)

    def cancel_downtimes_by_scope(
        self,
        body: CancelDowntimesByScopeRequest,
    ) -> CanceledDowntimesIds:
        """Cancel downtimes by scope. **Deprecated**.

        Delete all downtimes that match the scope of ``X``. **Note:** This only interacts with Downtimes created using v1 endpoints. This endpoint has been deprecated and will not be replaced. Please use v2 endpoints to find and cancel downtimes.

        :param body: Scope to cancel downtimes for.
        :type body: CancelDowntimesByScopeRequest
        :rtype: CanceledDowntimesIds
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        warnings.warn("cancel_downtimes_by_scope is deprecated", DeprecationWarning, stacklevel=2)
        return self._cancel_downtimes_by_scope_endpoint.call_with_http_info(**kwargs)

    def create_downtime(
        self,
        body: Downtime,
    ) -> Downtime:
        """Schedule a downtime. **Deprecated**.

        Schedule a downtime. **Note:** This endpoint has been deprecated. Please use v2 endpoints.

        :param body: Schedule a downtime request body.
        :type body: Downtime
        :rtype: Downtime
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        warnings.warn("create_downtime is deprecated", DeprecationWarning, stacklevel=2)
        return self._create_downtime_endpoint.call_with_http_info(**kwargs)

    def get_downtime(
        self,
        downtime_id: int,
    ) -> Downtime:
        """Get a downtime. **Deprecated**.

        Get downtime detail by ``downtime_id``. **Note:** This endpoint has been deprecated. Please use v2 endpoints.

        :param downtime_id: ID of the downtime to fetch.
        :type downtime_id: int
        :rtype: Downtime
        """
        kwargs: Dict[str, Any] = {}
        kwargs["downtime_id"] = downtime_id

        warnings.warn("get_downtime is deprecated", DeprecationWarning, stacklevel=2)
        return self._get_downtime_endpoint.call_with_http_info(**kwargs)

    def list_downtimes(
        self,
        *,
        current_only: Union[bool, UnsetType] = unset,
        with_creator: Union[bool, UnsetType] = unset,
    ) -> List[Downtime]:
        """Get all downtimes. **Deprecated**.

        Get all scheduled downtimes. **Note:** This endpoint has been deprecated. Please use v2 endpoints.

        :param current_only: Only return downtimes that are active when the request is made.
        :type current_only: bool, optional
        :param with_creator: Return creator information.
        :type with_creator: bool, optional
        :rtype: [Downtime]
        """
        kwargs: Dict[str, Any] = {}
        if current_only is not unset:
            kwargs["current_only"] = current_only

        if with_creator is not unset:
            kwargs["with_creator"] = with_creator

        warnings.warn("list_downtimes is deprecated", DeprecationWarning, stacklevel=2)
        return self._list_downtimes_endpoint.call_with_http_info(**kwargs)

    def list_monitor_downtimes(
        self,
        monitor_id: int,
    ) -> List[Downtime]:
        """Get active downtimes for a monitor. **Deprecated**.

        Get all active v1 downtimes for the specified monitor. **Note:** This endpoint has been deprecated. Please use v2 endpoints.

        :param monitor_id: The id of the monitor
        :type monitor_id: int
        :rtype: [Downtime]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["monitor_id"] = monitor_id

        warnings.warn("list_monitor_downtimes is deprecated", DeprecationWarning, stacklevel=2)
        return self._list_monitor_downtimes_endpoint.call_with_http_info(**kwargs)

    def update_downtime(
        self,
        downtime_id: int,
        body: Downtime,
    ) -> Downtime:
        """Update a downtime. **Deprecated**.

        Update a single downtime by ``downtime_id``. **Note:** This endpoint has been deprecated. Please use v2 endpoints.

        :param downtime_id: ID of the downtime to update.
        :type downtime_id: int
        :param body: Update a downtime request body.
        :type body: Downtime
        :rtype: Downtime
        """
        kwargs: Dict[str, Any] = {}
        kwargs["downtime_id"] = downtime_id

        kwargs["body"] = body

        warnings.warn("update_downtime is deprecated", DeprecationWarning, stacklevel=2)
        return self._update_downtime_endpoint.call_with_http_info(**kwargs)
