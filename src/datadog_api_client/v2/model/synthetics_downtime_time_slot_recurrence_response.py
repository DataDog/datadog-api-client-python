# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.synthetics_downtime_frequency import SyntheticsDowntimeFrequency
    from datadog_api_client.v2.model.synthetics_downtime_time_slot_date import SyntheticsDowntimeTimeSlotDate
    from datadog_api_client.v2.model.synthetics_downtime_weekday_position import SyntheticsDowntimeWeekdayPosition
    from datadog_api_client.v2.model.synthetics_downtime_weekday import SyntheticsDowntimeWeekday


class SyntheticsDowntimeTimeSlotRecurrenceResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_downtime_frequency import SyntheticsDowntimeFrequency
        from datadog_api_client.v2.model.synthetics_downtime_time_slot_date import SyntheticsDowntimeTimeSlotDate
        from datadog_api_client.v2.model.synthetics_downtime_weekday_position import SyntheticsDowntimeWeekdayPosition
        from datadog_api_client.v2.model.synthetics_downtime_weekday import SyntheticsDowntimeWeekday

        return {
            "frequency": (SyntheticsDowntimeFrequency,),
            "interval": (int,),
            "until": (SyntheticsDowntimeTimeSlotDate,),
            "weekday_positions": ([SyntheticsDowntimeWeekdayPosition],),
            "weekdays": ([SyntheticsDowntimeWeekday],),
        }

    attribute_map = {
        "frequency": "frequency",
        "interval": "interval",
        "until": "until",
        "weekday_positions": "weekdayPositions",
        "weekdays": "weekdays",
    }

    def __init__(
        self_,
        frequency: SyntheticsDowntimeFrequency,
        interval: int,
        weekdays: List[SyntheticsDowntimeWeekday],
        until: Union[SyntheticsDowntimeTimeSlotDate, UnsetType] = unset,
        weekday_positions: Union[List[SyntheticsDowntimeWeekdayPosition], UnsetType] = unset,
        **kwargs,
    ):
        """
        Recurrence settings returned in a Synthetics downtime time slot response.

        :param frequency: The recurrence frequency of a Synthetics downtime time slot.
        :type frequency: SyntheticsDowntimeFrequency

        :param interval: The interval between recurrences, relative to the frequency.
        :type interval: int

        :param until: A specific date and time used to define the start or end of a Synthetics downtime time slot.
        :type until: SyntheticsDowntimeTimeSlotDate, optional

        :param weekday_positions: Positions of the weekdays within a month for a monthly Synthetics downtime recurrence. Used in combination with ``weekdays`` to schedule occurrences such as "the first Monday of the month".
        :type weekday_positions: [SyntheticsDowntimeWeekdayPosition], optional

        :param weekdays: Days of the week for a Synthetics downtime recurrence schedule.
        :type weekdays: [SyntheticsDowntimeWeekday]
        """
        if until is not unset:
            kwargs["until"] = until
        if weekday_positions is not unset:
            kwargs["weekday_positions"] = weekday_positions
        super().__init__(kwargs)

        self_.frequency = frequency
        self_.interval = interval
        self_.weekdays = weekdays
