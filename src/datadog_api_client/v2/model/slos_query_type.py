# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SlosQueryType(ModelSimple):
    """
    The type of SLO definition being queried.

    :param value: Must be one of ["metric", "time_slice", "monitor"].
    :type value: str
    """

    allowed_values = {
        "metric",
        "time_slice",
        "monitor",
    }
    METRIC: ClassVar["SlosQueryType"]
    TIME_SLICE: ClassVar["SlosQueryType"]
    MONITOR: ClassVar["SlosQueryType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SlosQueryType.METRIC = SlosQueryType("metric")
SlosQueryType.TIME_SLICE = SlosQueryType("time_slice")
SlosQueryType.MONITOR = SlosQueryType("monitor")
