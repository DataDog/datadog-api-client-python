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
    from datadog_api_client.v2.model.synthetics_downtime_time_slot_date import SyntheticsDowntimeTimeSlotDate
    from datadog_api_client.v2.model.synthetics_downtime_frequency import SyntheticsDowntimeFrequency
    from datadog_api_client.v2.model.synthetics_downtime_weekday import SyntheticsDowntimeWeekday


class SyntheticsDowntimeTimeSlotRecurrenceRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_downtime_time_slot_date import SyntheticsDowntimeTimeSlotDate
        from datadog_api_client.v2.model.synthetics_downtime_frequency import SyntheticsDowntimeFrequency
        from datadog_api_client.v2.model.synthetics_downtime_weekday import SyntheticsDowntimeWeekday

        return {
            "end": (SyntheticsDowntimeTimeSlotDate,),
            "frequency": (SyntheticsDowntimeFrequency,),
            "interval": (int,),
            "weekdays": ([SyntheticsDowntimeWeekday],),
        }

    attribute_map = {
        "end": "end",
        "frequency": "frequency",
        "interval": "interval",
        "weekdays": "weekdays",
    }

    def __init__(
        self_,
        frequency: SyntheticsDowntimeFrequency,
        end: Union[SyntheticsDowntimeTimeSlotDate, UnsetType] = unset,
        interval: Union[int, UnsetType] = unset,
        weekdays: Union[List[SyntheticsDowntimeWeekday], UnsetType] = unset,
        **kwargs,
    ):
        """
        Recurrence settings for a Synthetics downtime time slot.

        :param end: A specific date and time used to define the start or end of a Synthetics downtime time slot.
        :type end: SyntheticsDowntimeTimeSlotDate, optional

        :param frequency: The recurrence frequency of a Synthetics downtime time slot.
        :type frequency: SyntheticsDowntimeFrequency

        :param interval: The interval between recurrences, relative to the frequency.
        :type interval: int, optional

        :param weekdays: Days of the week for a Synthetics downtime recurrence schedule.
        :type weekdays: [SyntheticsDowntimeWeekday], optional
        """
        if end is not unset:
            kwargs["end"] = end
        if interval is not unset:
            kwargs["interval"] = interval
        if weekdays is not unset:
            kwargs["weekdays"] = weekdays
        super().__init__(kwargs)

        self_.frequency = frequency
