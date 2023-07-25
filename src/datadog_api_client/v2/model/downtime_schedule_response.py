# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class DowntimeScheduleResponse(ModelComposed):
    def __init__(self, **kwargs):
        """
        The schedule that defines when the monitor starts, stops, and recurs. There are two types of schedules:
        one-time and recurring. Recurring schedules may have up to five RRULE-based recurrences. If no schedules are
        provided, the downtime will begin immediately and never end.

        :param current_downtime: The most recent actual start and end dates for a recurring downtime. For a canceled downtime,
            this is the previously occurring downtime. For active downtimes, this is the ongoing downtime, and for scheduled
            downtimes it is the upcoming downtime.
        :type current_downtime: DowntimeScheduleCurrentDowntimeResponse, optional

        :param recurrences: A list of downtime recurrences.
        :type recurrences: [DowntimeScheduleRecurrenceResponse]

        :param timezone: The timezone in which to schedule the downtime. This affects recurring start and end dates.
            Must match `display_timezone`.
        :type timezone: str, optional

        :param end: ISO-8601 Datetime to end the downtime.
        :type end: datetime, none_type, optional

        :param start: ISO-8601 Datetime to start the downtime.
        :type start: datetime
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.downtime_schedule_recurrences_response import (
            DowntimeScheduleRecurrencesResponse,
        )
        from datadog_api_client.v2.model.downtime_schedule_one_time_response import DowntimeScheduleOneTimeResponse

        return {
            "oneOf": [
                DowntimeScheduleRecurrencesResponse,
                DowntimeScheduleOneTimeResponse,
            ],
        }
