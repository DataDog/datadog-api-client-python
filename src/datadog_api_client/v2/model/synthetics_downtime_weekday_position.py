# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsDowntimeWeekdayPosition(ModelSimple):
    """
    The position of a weekday within a month for a monthly Synthetics downtime recurrence. `1` through `4` select the first through fourth occurrence of the weekday in the month, and `-1` selects the last occurrence.

    :param value: Must be one of [1, 2, 3, 4, -1].
    :type value: int
    """

    allowed_values = {
        1,
        2,
        3,
        4,
        -1,
    }
    FIRST: ClassVar["SyntheticsDowntimeWeekdayPosition"]
    SECOND: ClassVar["SyntheticsDowntimeWeekdayPosition"]
    THIRD: ClassVar["SyntheticsDowntimeWeekdayPosition"]
    FOURTH: ClassVar["SyntheticsDowntimeWeekdayPosition"]
    LAST: ClassVar["SyntheticsDowntimeWeekdayPosition"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (int,),
        }


SyntheticsDowntimeWeekdayPosition.FIRST = SyntheticsDowntimeWeekdayPosition(1)
SyntheticsDowntimeWeekdayPosition.SECOND = SyntheticsDowntimeWeekdayPosition(2)
SyntheticsDowntimeWeekdayPosition.THIRD = SyntheticsDowntimeWeekdayPosition(3)
SyntheticsDowntimeWeekdayPosition.FOURTH = SyntheticsDowntimeWeekdayPosition(4)
SyntheticsDowntimeWeekdayPosition.LAST = SyntheticsDowntimeWeekdayPosition(-1)
