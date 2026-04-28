# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsDowntimeFrequency(ModelSimple):
    """
    The recurrence frequency of a Synthetics downtime time slot.

    :param value: Must be one of ["DAILY", "WEEKLY", "MONTHLY", "YEARLY"].
    :type value: str
    """

    allowed_values = {
        "DAILY",
        "WEEKLY",
        "MONTHLY",
        "YEARLY",
    }
    DAILY: ClassVar["SyntheticsDowntimeFrequency"]
    WEEKLY: ClassVar["SyntheticsDowntimeFrequency"]
    MONTHLY: ClassVar["SyntheticsDowntimeFrequency"]
    YEARLY: ClassVar["SyntheticsDowntimeFrequency"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsDowntimeFrequency.DAILY = SyntheticsDowntimeFrequency("DAILY")
SyntheticsDowntimeFrequency.WEEKLY = SyntheticsDowntimeFrequency("WEEKLY")
SyntheticsDowntimeFrequency.MONTHLY = SyntheticsDowntimeFrequency("MONTHLY")
SyntheticsDowntimeFrequency.YEARLY = SyntheticsDowntimeFrequency("YEARLY")
