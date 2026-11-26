# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class Day(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

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
    MONDAY: ClassVar["Day"]
    TUESDAY: ClassVar["Day"]
    WEDNESDAY: ClassVar["Day"]
    THURSDAY: ClassVar["Day"]
    FRIDAY: ClassVar["Day"]
    SATURDAY: ClassVar["Day"]
    SUNDAY: ClassVar["Day"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


Day.MONDAY = Day("monday")
Day.TUESDAY = Day("tuesday")
Day.WEDNESDAY = Day("wednesday")
Day.THURSDAY = Day("thursday")
Day.FRIDAY = Day("friday")
Day.SATURDAY = Day("saturday")
Day.SUNDAY = Day("sunday")
