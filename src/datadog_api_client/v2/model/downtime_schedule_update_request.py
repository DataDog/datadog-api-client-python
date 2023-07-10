# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class DowntimeScheduleUpdateRequest(ModelComposed):
    def __init__(self, **kwargs):
        """
        Schedule for the downtime.

        :param recurrences: A list of downtime recurrences.
        :type recurrences: [DowntimeScheduleRecurrenceCreateUpdateRequest], optional

        :param timezone: The timezone in which to schedule the downtime.
        :type timezone: str, optional

        :param end: ISO-8601 Datetime to end the downtime. Must include a UTC offset of zero. If not provided, the
            downtime continues forever.
        :type end: datetime, none_type, optional

        :param start: ISO-8601 Datetime to start the downtime. Must include a UTC offset of zero. If not provided, the
            downtime starts the moment it is created.
        :type start: datetime, none_type, optional
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
        from datadog_api_client.v2.model.downtime_schedule_recurrences_update_request import (
            DowntimeScheduleRecurrencesUpdateRequest,
        )
        from datadog_api_client.v2.model.downtime_schedule_one_time_create_update_request import (
            DowntimeScheduleOneTimeCreateUpdateRequest,
        )

        return {
            "oneOf": [
                DowntimeScheduleRecurrencesUpdateRequest,
                DowntimeScheduleOneTimeCreateUpdateRequest,
            ],
        }
