# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ReportScheduleType(ModelSimple):
    """
    JSON:API resource type for report schedules.

    :param value: If omitted defaults to "schedule". Must be one of ["schedule"].
    :type value: str
    """

    allowed_values = {
        "schedule",
    }
    SCHEDULE: ClassVar["ReportScheduleType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ReportScheduleType.SCHEDULE = ReportScheduleType("schedule")
