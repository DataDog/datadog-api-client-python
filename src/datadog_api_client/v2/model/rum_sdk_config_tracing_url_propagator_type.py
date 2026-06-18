# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RumSdkConfigTracingUrlPropagatorType(ModelSimple):
    """
    A trace propagator type.

    :param value: Must be one of ["datadog", "b3", "b3multi", "tracecontext"].
    :type value: str
    """

    allowed_values = {
        "datadog",
        "b3",
        "b3multi",
        "tracecontext",
    }
    DATADOG: ClassVar["RumSdkConfigTracingUrlPropagatorType"]
    B3: ClassVar["RumSdkConfigTracingUrlPropagatorType"]
    B3MULTI: ClassVar["RumSdkConfigTracingUrlPropagatorType"]
    TRACECONTEXT: ClassVar["RumSdkConfigTracingUrlPropagatorType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RumSdkConfigTracingUrlPropagatorType.DATADOG = RumSdkConfigTracingUrlPropagatorType("datadog")
RumSdkConfigTracingUrlPropagatorType.B3 = RumSdkConfigTracingUrlPropagatorType("b3")
RumSdkConfigTracingUrlPropagatorType.B3MULTI = RumSdkConfigTracingUrlPropagatorType("b3multi")
RumSdkConfigTracingUrlPropagatorType.TRACECONTEXT = RumSdkConfigTracingUrlPropagatorType("tracecontext")
