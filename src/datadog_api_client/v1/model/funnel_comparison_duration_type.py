# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FunnelComparisonDurationType(ModelSimple):
    """
    Type of comparison duration.

    :param value: Must be one of ["previous_timeframe", "custom_timeframe", "previous_day", "previous_week", "previous_month"].
    :type value: str
    """

    allowed_values = {
        "previous_timeframe",
        "custom_timeframe",
        "previous_day",
        "previous_week",
        "previous_month",
    }
    PREVIOUS_TIMEFRAME: ClassVar["FunnelComparisonDurationType"]
    CUSTOM_TIMEFRAME: ClassVar["FunnelComparisonDurationType"]
    PREVIOUS_DAY: ClassVar["FunnelComparisonDurationType"]
    PREVIOUS_WEEK: ClassVar["FunnelComparisonDurationType"]
    PREVIOUS_MONTH: ClassVar["FunnelComparisonDurationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FunnelComparisonDurationType.PREVIOUS_TIMEFRAME = FunnelComparisonDurationType("previous_timeframe")
FunnelComparisonDurationType.CUSTOM_TIMEFRAME = FunnelComparisonDurationType("custom_timeframe")
FunnelComparisonDurationType.PREVIOUS_DAY = FunnelComparisonDurationType("previous_day")
FunnelComparisonDurationType.PREVIOUS_WEEK = FunnelComparisonDurationType("previous_week")
FunnelComparisonDurationType.PREVIOUS_MONTH = FunnelComparisonDurationType("previous_month")
