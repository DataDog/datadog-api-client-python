# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ConfiguredScheduleTargetType(ModelSimple):
    """
    Indicates that the resource is of type `schedule_target`.

    :param value: If omitted defaults to "schedule_target". Must be one of ["schedule_target"].
    :type value: str
    """

    allowed_values = {
        "schedule_target",
    }
    SCHEDULE_TARGET: ClassVar["ConfiguredScheduleTargetType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ConfiguredScheduleTargetType.SCHEDULE_TARGET = ConfiguredScheduleTargetType("schedule_target")
