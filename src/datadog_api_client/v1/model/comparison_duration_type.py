# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ComparisonDurationType(ModelSimple):
    """
    The comparison window type.

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
    PREVIOUS_TIMEFRAME: ClassVar["ComparisonDurationType"]
    CUSTOM_TIMEFRAME: ClassVar["ComparisonDurationType"]
    PREVIOUS_DAY: ClassVar["ComparisonDurationType"]
    PREVIOUS_WEEK: ClassVar["ComparisonDurationType"]
    PREVIOUS_MONTH: ClassVar["ComparisonDurationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ComparisonDurationType.PREVIOUS_TIMEFRAME = ComparisonDurationType("previous_timeframe")
ComparisonDurationType.CUSTOM_TIMEFRAME = ComparisonDurationType("custom_timeframe")
ComparisonDurationType.PREVIOUS_DAY = ComparisonDurationType("previous_day")
ComparisonDurationType.PREVIOUS_WEEK = ComparisonDurationType("previous_week")
ComparisonDurationType.PREVIOUS_MONTH = ComparisonDurationType("previous_month")
