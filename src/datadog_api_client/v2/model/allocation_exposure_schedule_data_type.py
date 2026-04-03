# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AllocationExposureScheduleDataType(ModelSimple):
    """
    The resource type for progressive rollout schedules.

    :param value: If omitted defaults to "allocation_exposure_schedules". Must be one of ["allocation_exposure_schedules"].
    :type value: str
    """

    allowed_values = {
        "allocation_exposure_schedules",
    }
    ALLOCATION_EXPOSURE_SCHEDULES: ClassVar["AllocationExposureScheduleDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AllocationExposureScheduleDataType.ALLOCATION_EXPOSURE_SCHEDULES = AllocationExposureScheduleDataType(
    "allocation_exposure_schedules"
)
