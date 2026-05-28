# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class PrunedTraceType(ModelSimple):
    """
    The type of the pruned trace resource. The value is always `pruned_trace`.

    :param value: If omitted defaults to "pruned_trace". Must be one of ["pruned_trace"].
    :type value: str
    """

    allowed_values = {
        "pruned_trace",
    }
    PRUNED_TRACE: ClassVar["PrunedTraceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


PrunedTraceType.PRUNED_TRACE = PrunedTraceType("pruned_trace")
