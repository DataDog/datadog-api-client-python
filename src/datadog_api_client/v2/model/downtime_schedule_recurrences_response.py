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
    from datadog_api_client.v2.model.downtime_schedule_current_downtime_response import (
        DowntimeScheduleCurrentDowntimeResponse,
    )
    from datadog_api_client.v2.model.downtime_schedule_recurrence_response import DowntimeScheduleRecurrenceResponse


class DowntimeScheduleRecurrencesResponse(ModelNormal):
    validations = {
        "recurrences": {
            "max_items": 5,
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.downtime_schedule_current_downtime_response import (
            DowntimeScheduleCurrentDowntimeResponse,
        )
        from datadog_api_client.v2.model.downtime_schedule_recurrence_response import DowntimeScheduleRecurrenceResponse

        return {
            "current_downtime": (DowntimeScheduleCurrentDowntimeResponse,),
            "recurrences": ([DowntimeScheduleRecurrenceResponse],),
            "timezone": (str,),
        }

    attribute_map = {
        "current_downtime": "current_downtime",
        "recurrences": "recurrences",
        "timezone": "timezone",
    }

    def __init__(
        self_,
        recurrences: List[DowntimeScheduleRecurrenceResponse],
        current_downtime: Union[DowntimeScheduleCurrentDowntimeResponse, UnsetType] = unset,
        timezone: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A recurring downtime schedule definition.

        :param current_downtime: The most recent actual start and end dates for a recurring downtime. For a canceled downtime,
            this is the previously occurring downtime. For active downtimes, this is the ongoing downtime, and for scheduled
            downtimes it is the upcoming downtime.
        :type current_downtime: DowntimeScheduleCurrentDowntimeResponse, optional

        :param recurrences: A list of downtime recurrences.
        :type recurrences: [DowntimeScheduleRecurrenceResponse]

        :param timezone: The timezone in which to schedule the downtime. This affects recurring start and end dates.
            Must match ``display_timezone``.
        :type timezone: str, optional
        """
        if current_downtime is not unset:
            kwargs["current_downtime"] = current_downtime
        if timezone is not unset:
            kwargs["timezone"] = timezone
        super().__init__(kwargs)

        self_.recurrences = recurrences
