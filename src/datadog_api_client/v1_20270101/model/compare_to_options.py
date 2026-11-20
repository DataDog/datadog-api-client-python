# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CompareToOptions(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["hour_before", "day_before", "week_before", "month_before"].
    :type value: str
    """

    allowed_values = {
        "hour_before",
        "day_before",
        "week_before",
        "month_before",
    }
    HOUR_BEFORE: ClassVar["CompareToOptions"]
    DAY_BEFORE: ClassVar["CompareToOptions"]
    WEEK_BEFORE: ClassVar["CompareToOptions"]
    MONTH_BEFORE: ClassVar["CompareToOptions"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CompareToOptions.HOUR_BEFORE = CompareToOptions("hour_before")
CompareToOptions.DAY_BEFORE = CompareToOptions("day_before")
CompareToOptions.WEEK_BEFORE = CompareToOptions("week_before")
CompareToOptions.MONTH_BEFORE = CompareToOptions("month_before")
