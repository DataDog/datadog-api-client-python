# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ChangeDurationAnyOfAnyOfItemType4444207072(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["previous_timeframe", "previous_day", "previous_week", "previous_month"].
    :type value: str
    """

    allowed_values = {
        "previous_timeframe",
        "previous_day",
        "previous_week",
        "previous_month",
    }
    PREVIOUS_TIMEFRAME: ClassVar["ChangeDurationAnyOfAnyOfItemType4444207072"]
    PREVIOUS_DAY: ClassVar["ChangeDurationAnyOfAnyOfItemType4444207072"]
    PREVIOUS_WEEK: ClassVar["ChangeDurationAnyOfAnyOfItemType4444207072"]
    PREVIOUS_MONTH: ClassVar["ChangeDurationAnyOfAnyOfItemType4444207072"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ChangeDurationAnyOfAnyOfItemType4444207072.PREVIOUS_TIMEFRAME = ChangeDurationAnyOfAnyOfItemType4444207072(
    "previous_timeframe"
)
ChangeDurationAnyOfAnyOfItemType4444207072.PREVIOUS_DAY = ChangeDurationAnyOfAnyOfItemType4444207072("previous_day")
ChangeDurationAnyOfAnyOfItemType4444207072.PREVIOUS_WEEK = ChangeDurationAnyOfAnyOfItemType4444207072("previous_week")
ChangeDurationAnyOfAnyOfItemType4444207072.PREVIOUS_MONTH = ChangeDurationAnyOfAnyOfItemType4444207072("previous_month")
