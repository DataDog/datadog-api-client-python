# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class LLMObsSpanFilter(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "_from": (str,),
            "ml_app": (str,),
            "query": (str,),
            "span_id": (str,),
            "span_kind": (str,),
            "span_name": (str,),
            "tags": ({str: (str,)},),
            "to": (str,),
            "trace_id": (str,),
        }

    attribute_map = {
        "_from": "from",
        "ml_app": "ml_app",
        "query": "query",
        "span_id": "span_id",
        "span_kind": "span_kind",
        "span_name": "span_name",
        "tags": "tags",
        "to": "to",
        "trace_id": "trace_id",
    }

    def __init__(
        self_,
        _from: Union[str, UnsetType] = unset,
        ml_app: Union[str, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        span_id: Union[str, UnsetType] = unset,
        span_kind: Union[str, UnsetType] = unset,
        span_name: Union[str, UnsetType] = unset,
        tags: Union[Dict[str, str], UnsetType] = unset,
        to: Union[str, UnsetType] = unset,
        trace_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Filter criteria for an LLM Observability span search.

        :param _from: Start of the time range. Accepts ISO 8601 or relative format (e.g., ``now-15m`` ). Defaults to ``now-15m``.
        :type _from: str, optional

        :param ml_app: Filter by ML application name.
        :type ml_app: str, optional

        :param query: Search query using LLM Observability query syntax. Supports attribute filters using the field:value syntax (e.g. session_id, trace_id, ml_app, meta.span.kind). When provided, structured field filters ( ``span_id`` , ``trace_id`` , etc.) are ignored.
        :type query: str, optional

        :param span_id: Filter by exact span ID.
        :type span_id: str, optional

        :param span_kind: Filter by span kind (e.g., llm, agent, tool, task, workflow).
        :type span_kind: str, optional

        :param span_name: Filter by span name.
        :type span_name: str, optional

        :param tags: Filter by tag key-value pairs.
        :type tags: {str: (str,)}, optional

        :param to: End of the time range. Accepts ISO 8601 or relative format (e.g., ``now`` ). Defaults to ``now``.
        :type to: str, optional

        :param trace_id: Filter by exact trace ID.
        :type trace_id: str, optional
        """
        if _from is not unset:
            kwargs["_from"] = _from
        if ml_app is not unset:
            kwargs["ml_app"] = ml_app
        if query is not unset:
            kwargs["query"] = query
        if span_id is not unset:
            kwargs["span_id"] = span_id
        if span_kind is not unset:
            kwargs["span_kind"] = span_kind
        if span_name is not unset:
            kwargs["span_name"] = span_name
        if tags is not unset:
            kwargs["tags"] = tags
        if to is not unset:
            kwargs["to"] = to
        if trace_id is not unset:
            kwargs["trace_id"] = trace_id
        super().__init__(kwargs)
