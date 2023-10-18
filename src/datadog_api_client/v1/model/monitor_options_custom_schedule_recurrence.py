# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class MonitorOptionsCustomScheduleRecurrence(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "rrule": (str,),
            "start": (str,),
            "timezone": (str,),
        }

    attribute_map = {
        "rrule": "rrule",
        "start": "start",
        "timezone": "timezone",
    }

    def __init__(
        self_,
        rrule: Union[str, UnsetType] = unset,
        start: Union[str, UnsetType] = unset,
        timezone: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Configuration for a recurrence set on the monitor options for custom schedule.

        :param rrule: Defines the recurrence rule (RRULE) for a given schedule.
        :type rrule: str, optional

        :param start: Defines the start date and time of the recurring schedule.
        :type start: str, optional

        :param timezone: Defines the timezone the schedule runs on.
        :type timezone: str, optional
        """
        if rrule is not unset:
            kwargs["rrule"] = rrule
        if start is not unset:
            kwargs["start"] = start
        if timezone is not unset:
            kwargs["timezone"] = timezone
        super().__init__(kwargs)
