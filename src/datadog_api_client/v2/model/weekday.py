# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class Weekday(ModelSimple):
    """
    A day of the week.

    :param value: Must be one of ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"].
    :type value: str
    """

    allowed_values = {
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    }
    MONDAY: ClassVar["Weekday"]
    TUESDAY: ClassVar["Weekday"]
    WEDNESDAY: ClassVar["Weekday"]
    THURSDAY: ClassVar["Weekday"]
    FRIDAY: ClassVar["Weekday"]
    SATURDAY: ClassVar["Weekday"]
    SUNDAY: ClassVar["Weekday"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


Weekday.MONDAY = Weekday("monday")
Weekday.TUESDAY = Weekday("tuesday")
Weekday.WEDNESDAY = Weekday("wednesday")
Weekday.THURSDAY = Weekday("thursday")
Weekday.FRIDAY = Weekday("friday")
Weekday.SATURDAY = Weekday("saturday")
Weekday.SUNDAY = Weekday("sunday")
