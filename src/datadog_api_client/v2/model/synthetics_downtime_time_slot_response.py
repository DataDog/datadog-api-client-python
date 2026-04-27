# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.synthetics_downtime_time_slot_recurrence_response import (
        SyntheticsDowntimeTimeSlotRecurrenceResponse,
    )
    from datadog_api_client.v2.model.synthetics_downtime_time_slot_date import SyntheticsDowntimeTimeSlotDate


class SyntheticsDowntimeTimeSlotResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_downtime_time_slot_recurrence_response import (
            SyntheticsDowntimeTimeSlotRecurrenceResponse,
        )
        from datadog_api_client.v2.model.synthetics_downtime_time_slot_date import SyntheticsDowntimeTimeSlotDate

        return {
            "duration": (int,),
            "id": (str,),
            "name": (str,),
            "recurrence": (SyntheticsDowntimeTimeSlotRecurrenceResponse,),
            "start": (SyntheticsDowntimeTimeSlotDate,),
            "timezone": (str,),
        }

    attribute_map = {
        "duration": "duration",
        "id": "id",
        "name": "name",
        "recurrence": "recurrence",
        "start": "start",
        "timezone": "timezone",
    }

    def __init__(
        self_,
        duration: int,
        id: str,
        start: SyntheticsDowntimeTimeSlotDate,
        timezone: str,
        name: Union[str, UnsetType] = unset,
        recurrence: Union[SyntheticsDowntimeTimeSlotRecurrenceResponse, UnsetType] = unset,
        **kwargs,
    ):
        """
        A time slot returned in a Synthetics downtime response.

        :param duration: The duration of the time slot in seconds.
        :type duration: int

        :param id: The unique identifier of the time slot.
        :type id: str

        :param name: The label for the time slot.
        :type name: str, optional

        :param recurrence: Recurrence settings returned in a Synthetics downtime time slot response.
        :type recurrence: SyntheticsDowntimeTimeSlotRecurrenceResponse, optional

        :param start: A specific date and time used to define the start or end of a Synthetics downtime time slot.
        :type start: SyntheticsDowntimeTimeSlotDate

        :param timezone: The IANA timezone name for the time slot.
        :type timezone: str
        """
        if name is not unset:
            kwargs["name"] = name
        if recurrence is not unset:
            kwargs["recurrence"] = recurrence
        super().__init__(kwargs)

        self_.duration = duration
        self_.id = id
        self_.start = start
        self_.timezone = timezone
