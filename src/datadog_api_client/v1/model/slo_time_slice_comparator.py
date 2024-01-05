# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SLOTimeSliceComparator(ModelSimple):
    """
    The comparator used to compare the SLI value to the threshold.

    :param value: Must be one of [">", ">=", "<", "<="].
    :type value: str
    """

    allowed_values = {
        ">",
        ">=",
        "<",
        "<=",
    }
    GREATER: ClassVar["SLOTimeSliceComparator"]
    GREATER_EQUAL: ClassVar["SLOTimeSliceComparator"]
    LESS: ClassVar["SLOTimeSliceComparator"]
    LESS_EQUAL: ClassVar["SLOTimeSliceComparator"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SLOTimeSliceComparator.GREATER = SLOTimeSliceComparator(">")
SLOTimeSliceComparator.GREATER_EQUAL = SLOTimeSliceComparator(">=")
SLOTimeSliceComparator.LESS = SLOTimeSliceComparator("<")
SLOTimeSliceComparator.LESS_EQUAL = SLOTimeSliceComparator("<=")
