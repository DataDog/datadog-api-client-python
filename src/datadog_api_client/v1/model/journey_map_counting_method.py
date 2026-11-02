# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class JourneyMapCountingMethod(ModelSimple):
    """
    Whether to count unique journeys or all journeys.

    :param value: Must be one of ["uniques", "totals"].
    :type value: str
    """

    allowed_values = {
        "uniques",
        "totals",
    }
    UNIQUES: ClassVar["JourneyMapCountingMethod"]
    TOTALS: ClassVar["JourneyMapCountingMethod"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


JourneyMapCountingMethod.UNIQUES = JourneyMapCountingMethod("uniques")
JourneyMapCountingMethod.TOTALS = JourneyMapCountingMethod("totals")
