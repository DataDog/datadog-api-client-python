# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RUMSdkConfigTracingUrlPropagatorType(ModelSimple):
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
    DATADOG: ClassVar["RUMSdkConfigTracingUrlPropagatorType"]
    B3: ClassVar["RUMSdkConfigTracingUrlPropagatorType"]
    B3MULTI: ClassVar["RUMSdkConfigTracingUrlPropagatorType"]
    TRACECONTEXT: ClassVar["RUMSdkConfigTracingUrlPropagatorType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RUMSdkConfigTracingUrlPropagatorType.DATADOG = RUMSdkConfigTracingUrlPropagatorType("datadog")
RUMSdkConfigTracingUrlPropagatorType.B3 = RUMSdkConfigTracingUrlPropagatorType("b3")
RUMSdkConfigTracingUrlPropagatorType.B3MULTI = RUMSdkConfigTracingUrlPropagatorType("b3multi")
RUMSdkConfigTracingUrlPropagatorType.TRACECONTEXT = RUMSdkConfigTracingUrlPropagatorType("tracecontext")
