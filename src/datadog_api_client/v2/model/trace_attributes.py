# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.apm_trace_span import APMTraceSpan


class TraceAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.apm_trace_span import APMTraceSpan

        return {
            "is_truncated": (bool,),
            "spans": ([APMTraceSpan],),
        }

    attribute_map = {
        "is_truncated": "is_truncated",
        "spans": "spans",
    }

    def __init__(self_, is_truncated: bool, spans: List[APMTraceSpan], **kwargs):
        """
        The attributes of a trace returned by the Get trace by ID endpoint.

        :param is_truncated: Indicates whether the trace was truncated because its size exceeded the maximum response payload.
        :type is_truncated: bool

        :param spans: The list of spans that compose the trace.
        :type spans: [APMTraceSpan]
        """
        super().__init__(kwargs)

        self_.is_truncated = is_truncated
        self_.spans = spans
