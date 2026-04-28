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
    from datadog_api_client.v2.model.synthetics_downtime_time_slot_recurrence_request import (
        SyntheticsDowntimeTimeSlotRecurrenceRequest,
    )
    from datadog_api_client.v2.model.synthetics_downtime_time_slot_date import SyntheticsDowntimeTimeSlotDate


class SyntheticsDowntimeTimeSlotRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_downtime_time_slot_recurrence_request import (
            SyntheticsDowntimeTimeSlotRecurrenceRequest,
        )
        from datadog_api_client.v2.model.synthetics_downtime_time_slot_date import SyntheticsDowntimeTimeSlotDate

        return {
            "duration": (int,),
            "name": (str,),
            "recurrence": (SyntheticsDowntimeTimeSlotRecurrenceRequest,),
            "start": (SyntheticsDowntimeTimeSlotDate,),
            "timezone": (str,),
        }

    attribute_map = {
        "duration": "duration",
        "name": "name",
        "recurrence": "recurrence",
        "start": "start",
        "timezone": "timezone",
    }

    def __init__(
        self_,
        duration: int,
        start: SyntheticsDowntimeTimeSlotDate,
        timezone: str,
        name: Union[str, UnsetType] = unset,
        recurrence: Union[SyntheticsDowntimeTimeSlotRecurrenceRequest, UnsetType] = unset,
        **kwargs,
    ):
        """
        A time slot for a Synthetics downtime create or update request.

        :param duration: The duration of the time slot in seconds, between 60 and 604800.
        :type duration: int

        :param name: An optional label for the time slot.
        :type name: str, optional

        :param recurrence: Recurrence settings for a Synthetics downtime time slot.
        :type recurrence: SyntheticsDowntimeTimeSlotRecurrenceRequest, optional

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
        self_.start = start
        self_.timezone = timezone
