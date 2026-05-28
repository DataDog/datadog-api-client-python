# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.apm_span_error_flag import APMSpanErrorFlag


class APMTraceSpan(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.apm_span_error_flag import APMSpanErrorFlag

        return {
            "duration": (int,),
            "end_time": (int,),
            "error": (APMSpanErrorFlag,),
            "meta": ({str: (str,)},),
            "metrics": ({str: (float,)},),
            "name": (str,),
            "parent_id": (int,),
            "resource": (str,),
            "resource_hash": (str,),
            "restricted": (bool,),
            "self_time": (float,),
            "service": (str,),
            "span_id": (int,),
            "start_time": (int,),
            "trace_id": (int,),
            "trace_id_full": (str,),
            "type": (str,),
        }

    attribute_map = {
        "duration": "duration",
        "end_time": "endTime",
        "error": "error",
        "meta": "meta",
        "metrics": "metrics",
        "name": "name",
        "parent_id": "parentID",
        "resource": "resource",
        "resource_hash": "resourceHash",
        "restricted": "restricted",
        "self_time": "self_time",
        "service": "service",
        "span_id": "spanID",
        "start_time": "startTime",
        "trace_id": "traceID",
        "trace_id_full": "traceIDFull",
        "type": "type",
    }

    def __init__(
        self_,
        duration: int,
        end_time: int,
        error: APMSpanErrorFlag,
        meta: Dict[str, str],
        metrics: Dict[str, float],
        name: str,
        parent_id: int,
        resource: str,
        service: str,
        span_id: int,
        start_time: int,
        trace_id: int,
        trace_id_full: str,
        type: str,
        resource_hash: Union[str, UnsetType] = unset,
        restricted: Union[bool, UnsetType] = unset,
        self_time: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        A single APM span returned as part of a trace.

        :param duration: The duration of the span, in nanoseconds.
        :type duration: int

        :param end_time: The end time of the span, in Unix nanoseconds.
        :type end_time: int

        :param error: Error flag for a span. ``1`` when the span is in error, ``0`` otherwise.
        :type error: APMSpanErrorFlag

        :param meta: String-valued tags attached to the span. Tag keys starting with ``_`` are
            filtered out of the response.
        :type meta: {str: (str,)}

        :param metrics: Numeric metrics attached to the span. Metric keys starting with ``_`` are
            filtered out of the response.
        :type metrics: {str: (float,)}

        :param name: The operation name of the span.
        :type name: str

        :param parent_id: The ID of the parent span, or ``0`` when the span is a trace root.
        :type parent_id: int

        :param resource: The resource that the span describes.
        :type resource: str

        :param resource_hash: A hash of the resource field.
        :type resource_hash: str, optional

        :param restricted: Whether access to the span is restricted by the organization's data access policies.
        :type restricted: bool, optional

        :param self_time: The time spent in the span itself, excluding time spent in child spans, in nanoseconds.
        :type self_time: float, optional

        :param service: The name of the service that emitted the span.
        :type service: str

        :param span_id: The span ID, as an unsigned 64-bit integer.
        :type span_id: int

        :param start_time: The start time of the span, in Unix nanoseconds.
        :type start_time: int

        :param trace_id: The lower 64 bits of the trace ID, as an unsigned 64-bit integer.
        :type trace_id: int

        :param trace_id_full: The full 128-bit trace ID, encoded as a 32-character hexadecimal string.
        :type trace_id_full: str

        :param type: The type of the span (for example, ``web`` , ``db`` , or ``rpc`` ).
        :type type: str
        """
        if resource_hash is not unset:
            kwargs["resource_hash"] = resource_hash
        if restricted is not unset:
            kwargs["restricted"] = restricted
        if self_time is not unset:
            kwargs["self_time"] = self_time
        super().__init__(kwargs)

        self_.duration = duration
        self_.end_time = end_time
        self_.error = error
        self_.meta = meta
        self_.metrics = metrics
        self_.name = name
        self_.parent_id = parent_id
        self_.resource = resource
        self_.service = service
        self_.span_id = span_id
        self_.start_time = start_time
        self_.trace_id = trace_id
        self_.trace_id_full = trace_id_full
        self_.type = type
