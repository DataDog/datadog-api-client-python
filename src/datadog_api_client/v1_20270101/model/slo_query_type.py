# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SloQueryType(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["monitor", "metric", "time_slice"].
    :type value: str
    """

    allowed_values = {
        "monitor",
        "metric",
        "time_slice",
    }
    MONITOR: ClassVar["SloQueryType"]
    METRIC: ClassVar["SloQueryType"]
    TIME_SLICE: ClassVar["SloQueryType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SloQueryType.MONITOR = SloQueryType("monitor")
SloQueryType.METRIC = SloQueryType("metric")
SloQueryType.TIME_SLICE = SloQueryType("time_slice")
