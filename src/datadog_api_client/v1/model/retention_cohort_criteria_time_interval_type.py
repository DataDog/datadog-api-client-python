# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RetentionCohortCriteriaTimeIntervalType(ModelSimple):
    """
    Type of time interval for cohort criteria.

    :param value: If omitted defaults to "calendar". Must be one of ["calendar"].
    :type value: str
    """

    allowed_values = {
        "calendar",
    }
    CALENDAR: ClassVar["RetentionCohortCriteriaTimeIntervalType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RetentionCohortCriteriaTimeIntervalType.CALENDAR = RetentionCohortCriteriaTimeIntervalType("calendar")
