# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class FleetScheduleV2RecurrenceRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "days_of_week": ([str],),
            "interval": (int,),
            "maintenance_window_duration": (int,),
            "start_maintenance_window": (str,),
            "timezone": (str,),
        }

    attribute_map = {
        "days_of_week": "days_of_week",
        "interval": "interval",
        "maintenance_window_duration": "maintenance_window_duration",
        "start_maintenance_window": "start_maintenance_window",
        "timezone": "timezone",
    }

    def __init__(
        self_,
        days_of_week: Union[List[str], UnsetType] = unset,
        interval: Union[int, UnsetType] = unset,
        maintenance_window_duration: Union[int, UnsetType] = unset,
        start_maintenance_window: Union[str, UnsetType] = unset,
        timezone: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Defines the recurrence pattern for the schedule.

        :param days_of_week: Days of the week when the schedule triggers. Valid values are
            "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun".
        :type days_of_week: [str], optional

        :param interval: Interval between schedule runs in weeks. 1 means the schedule runs every week
            on the specified days. Higher values repeat every N weeks.
        :type interval: int, optional

        :param maintenance_window_duration: Duration of the maintenance window in minutes.
        :type maintenance_window_duration: int, optional

        :param start_maintenance_window: Start time of the maintenance window in 24-hour clock format (HH:MM).
            Deployments are triggered at this time on the specified days.
        :type start_maintenance_window: str, optional

        :param timezone: Timezone in IANA Time Zone Database format.
        :type timezone: str, optional
        """
        if days_of_week is not unset:
            kwargs["days_of_week"] = days_of_week
        if interval is not unset:
            kwargs["interval"] = interval
        if maintenance_window_duration is not unset:
            kwargs["maintenance_window_duration"] = maintenance_window_duration
        if start_maintenance_window is not unset:
            kwargs["start_maintenance_window"] = start_maintenance_window
        if timezone is not unset:
            kwargs["timezone"] = timezone
        super().__init__(kwargs)
