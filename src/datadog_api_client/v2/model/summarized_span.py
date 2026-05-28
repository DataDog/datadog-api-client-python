# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.apm_span_error_flag import APMSpanErrorFlag


class SummarizedSpan(ModelNormal):
    validations = {
        "hidden_child_spans_count": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.apm_span_error_flag import APMSpanErrorFlag

        return {
            "children": ([SummarizedSpan],),
            "duration_seconds": (float,),
            "end_time": (datetime,),
            "error": (APMSpanErrorFlag,),
            "hidden_child_spans_count": (int,),
            "meta": ({str: (str,)},),
            "metrics": ({str: (float,)},),
            "name": (str,),
            "parent_id": (int,),
            "resource": (str,),
            "service": (str,),
            "span_id": (int,),
            "span_kind": (str,),
            "start_time": (datetime,),
        }

    attribute_map = {
        "children": "children",
        "duration_seconds": "durationSeconds",
        "end_time": "endTime",
        "error": "error",
        "hidden_child_spans_count": "hidden_child_spans_count",
        "meta": "meta",
        "metrics": "metrics",
        "name": "name",
        "parent_id": "parentID",
        "resource": "resource",
        "service": "service",
        "span_id": "spanID",
        "span_kind": "span_kind",
        "start_time": "startTime",
    }

    def __init__(
        self_,
        children: List[SummarizedSpan],
        duration_seconds: float,
        end_time: datetime,
        error: APMSpanErrorFlag,
        hidden_child_spans_count: int,
        meta: Dict[str, str],
        metrics: Dict[str, float],
        name: str,
        parent_id: int,
        resource: str,
        service: str,
        span_id: int,
        span_kind: str,
        start_time: datetime,
        **kwargs,
    ):
        """
        A node in the pruned trace tree.

        :param children: The child spans of this node in the pruned tree.
        :type children: [SummarizedSpan]

        :param duration_seconds: The duration of the span, in seconds.
        :type duration_seconds: float

        :param end_time: The end time of the span, in RFC3339 format.
        :type end_time: datetime

        :param error: Error flag for a span. ``1`` when the span is in error, ``0`` otherwise.
        :type error: APMSpanErrorFlag

        :param hidden_child_spans_count: The number of child spans that were pruned from this node when summarizing the trace.
        :type hidden_child_spans_count: int

        :param meta: String-valued tags attached to the span.
        :type meta: {str: (str,)}

        :param metrics: Numeric metrics attached to the span.
        :type metrics: {str: (float,)}

        :param name: The operation name of the span.
        :type name: str

        :param parent_id: The ID of the parent span, or ``0`` when the span is the trace root.
        :type parent_id: int

        :param resource: The resource that the span describes.
        :type resource: str

        :param service: The name of the service that emitted the span.
        :type service: str

        :param span_id: The span ID, as an unsigned 64-bit integer.
        :type span_id: int

        :param span_kind: The OpenTelemetry span kind, for example ``INTERNAL`` , ``SERVER`` , ``CLIENT`` ,
            ``PRODUCER`` , or ``CONSUMER``.
        :type span_kind: str

        :param start_time: The start time of the span, in RFC3339 format.
        :type start_time: datetime
        """
        super().__init__(kwargs)

        self_.children = children
        self_.duration_seconds = duration_seconds
        self_.end_time = end_time
        self_.error = error
        self_.hidden_child_spans_count = hidden_child_spans_count
        self_.meta = meta
        self_.metrics = metrics
        self_.name = name
        self_.parent_id = parent_id
        self_.resource = resource
        self_.service = service
        self_.span_id = span_id
        self_.span_kind = span_kind
        self_.start_time = start_time
