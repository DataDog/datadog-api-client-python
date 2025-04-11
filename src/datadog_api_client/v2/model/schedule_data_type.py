# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ScheduleDataType(ModelSimple):
    """
    Schedules resource type.

    :param value: If omitted defaults to "schedules". Must be one of ["schedules"].
    :type value: str
    """

    allowed_values = {
        "schedules",
    }
    SCHEDULES: ClassVar["ScheduleDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ScheduleDataType.SCHEDULES = ScheduleDataType("schedules")
