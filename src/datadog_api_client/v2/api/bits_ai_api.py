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
from datadog_api_client.v2.model.list_investigations_response import ListInvestigationsResponse
from datadog_api_client.v2.model.list_investigations_response_data import ListInvestigationsResponseData
from datadog_api_client.v2.model.trigger_investigation_response import TriggerInvestigationResponse
from datadog_api_client.v2.model.trigger_investigation_request import TriggerInvestigationRequest
from datadog_api_client.v2.model.get_investigation_response import GetInvestigationResponse


class BitsAIApi:
    """
    Use the Bits AI endpoints to retrieve AI-powered investigations.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._get_investigation_endpoint = _Endpoint(
            settings={
                "response_type": (GetInvestigationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/bits-ai/investigations/{id}",
                "operation_id": "get_investigation",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_investigations_endpoint = _Endpoint(
            settings={
                "response_type": (ListInvestigationsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/bits-ai/investigations",
                "operation_id": "list_investigations",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_offset": {
                    "openapi_types": (int,),
                    "attribute": "page[offset]",
                    "location": "query",
                },
                "page_limit": {
                    "validation": {
                        "inclusive_maximum": 100,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[limit]",
                    "location": "query",
                },
                "filter_monitor_id": {
                    "openapi_types": (int,),
                    "attribute": "filter[monitor_id]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._trigger_investigation_endpoint = _Endpoint(
            settings={
                "response_type": (TriggerInvestigationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/bits-ai/investigations",
                "operation_id": "trigger_investigation",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (TriggerInvestigationRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def get_investigation(
        self,
        id: str,
    ) -> GetInvestigationResponse:
        """Get a Bits AI investigation.

        Get a specific Bits AI investigation by ID.

        :param id: The ID of the investigation.
        :type id: str
        :rtype: GetInvestigationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._get_investigation_endpoint.call_with_http_info(**kwargs)

    def list_investigations(
        self,
        *,
        page_offset: Union[int, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
        filter_monitor_id: Union[int, UnsetType] = unset,
    ) -> ListInvestigationsResponse:
        """List Bits AI investigations.

        List all Bits AI investigations for the organization.

        :param page_offset: Offset for pagination.
        :type page_offset: int, optional
        :param page_limit: Maximum number of investigations to return.
        :type page_limit: int, optional
        :param filter_monitor_id: Filter investigations by monitor ID.
        :type filter_monitor_id: int, optional
        :rtype: ListInvestigationsResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        if filter_monitor_id is not unset:
            kwargs["filter_monitor_id"] = filter_monitor_id

        return self._list_investigations_endpoint.call_with_http_info(**kwargs)

    def list_investigations_with_pagination(
        self,
        *,
        page_offset: Union[int, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
        filter_monitor_id: Union[int, UnsetType] = unset,
    ) -> collections.abc.Iterable[ListInvestigationsResponseData]:
        """List Bits AI investigations.

        Provide a paginated version of :meth:`list_investigations`, returning all items.

        :param page_offset: Offset for pagination.
        :type page_offset: int, optional
        :param page_limit: Maximum number of investigations to return.
        :type page_limit: int, optional
        :param filter_monitor_id: Filter investigations by monitor ID.
        :type filter_monitor_id: int, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[ListInvestigationsResponseData]
        """
        kwargs: Dict[str, Any] = {}
        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        if filter_monitor_id is not unset:
            kwargs["filter_monitor_id"] = filter_monitor_id

        local_page_size = get_attribute_from_path(kwargs, "page_limit", 25)
        endpoint = self._list_investigations_endpoint
        set_attribute_from_path(kwargs, "page_limit", local_page_size, endpoint.params_map)
        pagination = {
            "limit_value": local_page_size,
            "results_path": "data",
            "page_offset_param": "page_offset",
            "endpoint": endpoint,
            "kwargs": kwargs,
        }
        return endpoint.call_with_http_info_paginated(pagination)

    def trigger_investigation(
        self,
        body: TriggerInvestigationRequest,
    ) -> TriggerInvestigationResponse:
        """Trigger a Bits AI investigation.

        Trigger a new Bits AI investigation based on a monitor alert.

        :param body: Trigger investigation request body.
        :type body: TriggerInvestigationRequest
        :rtype: TriggerInvestigationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._trigger_investigation_endpoint.call_with_http_info(**kwargs)
