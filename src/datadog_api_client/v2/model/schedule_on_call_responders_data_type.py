# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ScheduleOnCallRespondersDataType(ModelSimple):
    """
    Represents the resource type for a schedule's grouped on-call responders across the previous, current, and next positions.

    :param value: If omitted defaults to "schedule_oncall_responders". Must be one of ["schedule_oncall_responders"].
    :type value: str
    """

    allowed_values = {
        "schedule_oncall_responders",
    }
    SCHEDULE_ONCALL_RESPONDERS: ClassVar["ScheduleOnCallRespondersDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ScheduleOnCallRespondersDataType.SCHEDULE_ONCALL_RESPONDERS = ScheduleOnCallRespondersDataType(
    "schedule_oncall_responders"
)
