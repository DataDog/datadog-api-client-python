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
from datadog_api_client.v2.model.schedule import Schedule
from datadog_api_client.v2.model.schedule_create_request import ScheduleCreateRequest
from datadog_api_client.v2.model.schedule_update_request import ScheduleUpdateRequest


class OnCallApi:
    """
    Configure your `Datadog On-Call <https://docs.datadoghq.com/service_management/on-call/>`_
    directly through the Datadog API.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_on_call_schedule_endpoint = _Endpoint(
            settings={
                "response_type": (Schedule,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/on-call/schedules",
                "operation_id": "create_on_call_schedule",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ScheduleCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_on_call_schedule_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/on-call/schedules/{schedule_id}",
                "operation_id": "delete_on_call_schedule",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "schedule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "schedule_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_on_call_schedule_endpoint = _Endpoint(
            settings={
                "response_type": (Schedule,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/on-call/schedules/{schedule_id}",
                "operation_id": "get_on_call_schedule",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
                "schedule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "schedule_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_on_call_schedule_endpoint = _Endpoint(
            settings={
                "response_type": (Schedule,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/on-call/schedules/{schedule_id}",
                "operation_id": "update_on_call_schedule",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
                "schedule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "schedule_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ScheduleUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_on_call_schedule(
        self,
        body: ScheduleCreateRequest,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> Schedule:
        """Create on-call schedule.

        Create a new on-call schedule

        :type body: ScheduleCreateRequest
        :param include: Comma-separated list of included relationships to be returned. Allowed values: ``teams`` , ``layers`` , ``layers.members`` , ``layers.members.user``.
        :type include: str, optional
        :rtype: Schedule
        """
        kwargs: Dict[str, Any] = {}
        if include is not unset:
            kwargs["include"] = include

        kwargs["body"] = body

        return self._create_on_call_schedule_endpoint.call_with_http_info(**kwargs)

    def delete_on_call_schedule(
        self,
        schedule_id: str,
    ) -> None:
        """Delete on-call schedule.

        Delete an on-call schedule

        :param schedule_id: The ID of the schedule
        :type schedule_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["schedule_id"] = schedule_id

        return self._delete_on_call_schedule_endpoint.call_with_http_info(**kwargs)

    def get_on_call_schedule(
        self,
        schedule_id: str,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> Schedule:
        """Get on-call schedule.

        Get an on-call schedule

        :param schedule_id: The ID of the schedule
        :type schedule_id: str
        :param include: Comma-separated list of included relationships to be returned. Allowed values: ``teams`` , ``layers`` , ``layers.members`` , ``layers.members.user``.
        :type include: str, optional
        :rtype: Schedule
        """
        kwargs: Dict[str, Any] = {}
        if include is not unset:
            kwargs["include"] = include

        kwargs["schedule_id"] = schedule_id

        return self._get_on_call_schedule_endpoint.call_with_http_info(**kwargs)

    def update_on_call_schedule(
        self,
        schedule_id: str,
        body: ScheduleUpdateRequest,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> Schedule:
        """Update on-call schedule.

        Update a new on-call schedule

        :param schedule_id: The ID of the schedule
        :type schedule_id: str
        :type body: ScheduleUpdateRequest
        :param include: Comma-separated list of included relationships to be returned. Allowed values: ``teams`` , ``layers`` , ``layers.members`` , ``layers.members.user``.
        :type include: str, optional
        :rtype: Schedule
        """
        kwargs: Dict[str, Any] = {}
        if include is not unset:
            kwargs["include"] = include

        kwargs["schedule_id"] = schedule_id

        kwargs["body"] = body

        return self._update_on_call_schedule_endpoint.call_with_http_info(**kwargs)
