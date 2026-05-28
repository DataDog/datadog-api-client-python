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
from datadog_api_client.v2.model.pruned_trace_response import PrunedTraceResponse
from datadog_api_client.v2.model.trace_response import TraceResponse


class APMTraceApi:
    """
    Retrieve full or pruned APM traces by trace ID.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._get_pruned_trace_by_id_endpoint = _Endpoint(
            settings={
                "response_type": (PrunedTraceResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/pruned_trace/{trace_id}",
                "operation_id": "get_pruned_trace_by_id",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "trace_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "trace_id",
                    "location": "path",
                },
                "expand_span_id": {
                    "openapi_types": (int,),
                    "attribute": "expand_span_id",
                    "location": "query",
                },
                "time_hint": {
                    "validation": {
                        "inclusive_maximum": 2147483647,
                    },
                    "openapi_types": (int,),
                    "attribute": "time_hint",
                    "location": "query",
                },
                "force_source": {
                    "openapi_types": (str,),
                    "attribute": "force_source",
                    "location": "query",
                },
                "include_path": {
                    "openapi_types": ([str],),
                    "attribute": "include_path",
                    "location": "query",
                    "collection_format": "multi",
                },
                "tag_include": {
                    "openapi_types": ([str],),
                    "attribute": "tag_include",
                    "location": "query",
                    "collection_format": "multi",
                },
                "tag_exclude": {
                    "openapi_types": ([str],),
                    "attribute": "tag_exclude",
                    "location": "query",
                    "collection_format": "multi",
                },
                "only_service_entry_spans": {
                    "openapi_types": (bool,),
                    "attribute": "only_service_entry_spans",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_trace_by_id_endpoint = _Endpoint(
            settings={
                "response_type": (TraceResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/trace/{trace_id}",
                "operation_id": "get_trace_by_id",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "trace_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "trace_id",
                    "location": "path",
                },
                "include_fields": {
                    "openapi_types": ([str],),
                    "attribute": "include_fields",
                    "location": "query",
                    "collection_format": "multi",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def get_pruned_trace_by_id(
        self,
        trace_id: str,
        *,
        expand_span_id: Union[int, UnsetType] = unset,
        time_hint: Union[int, UnsetType] = unset,
        force_source: Union[str, UnsetType] = unset,
        include_path: Union[List[str], UnsetType] = unset,
        tag_include: Union[List[str], UnsetType] = unset,
        tag_exclude: Union[List[str], UnsetType] = unset,
        only_service_entry_spans: Union[bool, UnsetType] = unset,
    ) -> PrunedTraceResponse:
        """Get a pruned trace by ID.

        Retrieve a pruned, hierarchical view of an APM trace by its trace ID.
        The trace is summarized as a tree of spans rooted at the trace root and reduced in size
        to keep rendering large traces in the UI practical.
        This endpoint is rate limited to ``60`` requests per minute per organization.

        :param trace_id: The trace ID. Accepts either a 32-character hexadecimal string (128-bit trace ID)
            or a decimal string of up to 39 digits.
        :type trace_id: str
        :param expand_span_id: Span ID to expand and preserve in the pruned tree even when its branch would
            normally be summarized.
        :type expand_span_id: int, optional
        :param time_hint: Optional Unix time hint, in seconds, used to optimize the lookup of the trace
            in long-term storage.
        :type time_hint: int, optional
        :param force_source: Force the trace to be loaded from a specific source. When unset, the API picks
            the source automatically.
        :type force_source: str, optional
        :param include_path: Restrict the pruned tree to spans matching the given ``key:value`` pairs.
            Values may be passed as repeated query parameters.
        :type include_path: [str], optional
        :param tag_include: Regex patterns of tag keys whose values must be included in the pruned spans.
            Values may be passed as repeated query parameters.
        :type tag_include: [str], optional
        :param tag_exclude: Regex patterns of tag keys whose values must be excluded from the pruned spans.
            Values may be passed as repeated query parameters.
        :type tag_exclude: [str], optional
        :param only_service_entry_spans: When set to ``true`` , only service entry spans are included in the pruned tree.
        :type only_service_entry_spans: bool, optional
        :rtype: PrunedTraceResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["trace_id"] = trace_id

        if expand_span_id is not unset:
            kwargs["expand_span_id"] = expand_span_id

        if time_hint is not unset:
            kwargs["time_hint"] = time_hint

        if force_source is not unset:
            kwargs["force_source"] = force_source

        if include_path is not unset:
            kwargs["include_path"] = include_path

        if tag_include is not unset:
            kwargs["tag_include"] = tag_include

        if tag_exclude is not unset:
            kwargs["tag_exclude"] = tag_exclude

        if only_service_entry_spans is not unset:
            kwargs["only_service_entry_spans"] = only_service_entry_spans

        return self._get_pruned_trace_by_id_endpoint.call_with_http_info(**kwargs)

    def get_trace_by_id(
        self,
        trace_id: str,
        *,
        include_fields: Union[List[str], UnsetType] = unset,
    ) -> TraceResponse:
        """Get a trace by ID.

        Retrieve a full APM trace by its trace ID, including every span in the trace.
        Traces are returned from live storage when available and fall back to longer-term storage.
        This endpoint is rate limited to ``60`` requests per minute per organization.

        :param trace_id: The trace ID. Accepts either a 32-character hexadecimal string (128-bit trace ID)
            or a decimal string of up to 39 digits.
        :type trace_id: str
        :param include_fields: List of span fields to include in the response. When omitted, every available field is returned.
            Values may be passed as repeated query parameters or as a single comma-separated value.
        :type include_fields: [str], optional
        :rtype: TraceResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["trace_id"] = trace_id

        if include_fields is not unset:
            kwargs["include_fields"] = include_fields

        return self._get_trace_by_id_endpoint.call_with_http_info(**kwargs)
