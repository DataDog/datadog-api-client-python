# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class FleetScheduleRecurrenceRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "days_of_week": ([str],),
            "maintenance_window_duration": (int,),
            "start_maintenance_window": (str,),
            "timezone": (str,),
        }

    attribute_map = {
        "days_of_week": "days_of_week",
        "maintenance_window_duration": "maintenance_window_duration",
        "start_maintenance_window": "start_maintenance_window",
        "timezone": "timezone",
    }

    def __init__(
        self_,
        days_of_week: List[str],
        maintenance_window_duration: int,
        start_maintenance_window: str,
        timezone: str,
        **kwargs,
    ):
        """
        Defines the recurrence pattern for the schedule. Specifies when deployments should be
        automatically triggered based on maintenance windows.

        :param days_of_week: List of days of the week when the schedule should trigger. Valid values are:
            "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun".
        :type days_of_week: [str]

        :param maintenance_window_duration: Duration of the maintenance window in minutes.
        :type maintenance_window_duration: int

        :param start_maintenance_window: Start time of the maintenance window in 24-hour clock format (HH:MM).
            Deployments will be triggered at this time on the specified days.
        :type start_maintenance_window: str

        :param timezone: Timezone for the schedule in IANA Time Zone Database format (e.g., "America/New_York", "UTC").
        :type timezone: str
        """
        super().__init__(kwargs)

        self_.days_of_week = days_of_week
        self_.maintenance_window_duration = maintenance_window_duration
        self_.start_maintenance_window = start_maintenance_window
        self_.timezone = timezone
