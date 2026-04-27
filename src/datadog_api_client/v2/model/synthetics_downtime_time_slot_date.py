# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsDowntimeTimeSlotDate(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "day": (int,),
            "hour": (int,),
            "minute": (int,),
            "month": (int,),
            "year": (int,),
        }

    attribute_map = {
        "day": "day",
        "hour": "hour",
        "minute": "minute",
        "month": "month",
        "year": "year",
    }

    def __init__(self_, day: int, hour: int, minute: int, month: int, year: int, **kwargs):
        """
        A specific date and time used to define the start or end of a Synthetics downtime time slot.

        :param day: The day component of the date (1-31).
        :type day: int

        :param hour: The hour component of the time (0-23).
        :type hour: int

        :param minute: The minute component of the time (0-59).
        :type minute: int

        :param month: The month component of the date (1-12).
        :type month: int

        :param year: The year component of the date.
        :type year: int
        """
        super().__init__(kwargs)

        self_.day = day
        self_.hour = hour
        self_.minute = minute
        self_.month = month
        self_.year = year
