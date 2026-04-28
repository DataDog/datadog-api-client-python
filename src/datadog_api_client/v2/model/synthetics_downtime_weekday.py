# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsDowntimeWeekday(ModelSimple):
    """
    A day of the week for a Synthetics downtime recurrence.

    :param value: Must be one of ["MO", "TU", "WE", "TH", "FR", "SA", "SU"].
    :type value: str
    """

    allowed_values = {
        "MO",
        "TU",
        "WE",
        "TH",
        "FR",
        "SA",
        "SU",
    }
    MONDAY: ClassVar["SyntheticsDowntimeWeekday"]
    TUESDAY: ClassVar["SyntheticsDowntimeWeekday"]
    WEDNESDAY: ClassVar["SyntheticsDowntimeWeekday"]
    THURSDAY: ClassVar["SyntheticsDowntimeWeekday"]
    FRIDAY: ClassVar["SyntheticsDowntimeWeekday"]
    SATURDAY: ClassVar["SyntheticsDowntimeWeekday"]
    SUNDAY: ClassVar["SyntheticsDowntimeWeekday"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsDowntimeWeekday.MONDAY = SyntheticsDowntimeWeekday("MO")
SyntheticsDowntimeWeekday.TUESDAY = SyntheticsDowntimeWeekday("TU")
SyntheticsDowntimeWeekday.WEDNESDAY = SyntheticsDowntimeWeekday("WE")
SyntheticsDowntimeWeekday.THURSDAY = SyntheticsDowntimeWeekday("TH")
SyntheticsDowntimeWeekday.FRIDAY = SyntheticsDowntimeWeekday("FR")
SyntheticsDowntimeWeekday.SATURDAY = SyntheticsDowntimeWeekday("SA")
SyntheticsDowntimeWeekday.SUNDAY = SyntheticsDowntimeWeekday("SU")
