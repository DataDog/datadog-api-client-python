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


class SecurityMonitoringSchedulingOptions(ModelNormal):
    _nullable = True

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
        Options for scheduled rules. When this field is present, the rule runs based on the schedule. When absent, it runs real-time on ingested logs.

        :param rrule: Schedule for the rule queries, written in RRULE syntax. See `RFC <https://icalendar.org/iCalendar-RFC-5545/3-8-5-3-recurrence-rule.html>`_ for syntax reference.
        :type rrule: str, optional

        :param start: Start date for the schedule, in ISO 8601 format without timezone.
        :type start: str, optional

        :param timezone: Time zone of the start date, in the `tz database <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones>`_ format.
        :type timezone: str, optional
        """
        if rrule is not unset:
            kwargs["rrule"] = rrule
        if start is not unset:
            kwargs["start"] = start
        if timezone is not unset:
            kwargs["timezone"] = timezone
        super().__init__(kwargs)
