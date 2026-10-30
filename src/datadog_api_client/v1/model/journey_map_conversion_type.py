# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class JourneyMapConversionType(ModelSimple):
    """
    Whether to show the paths that convert to the end step or drop off before it.

    :param value: Must be one of ["conversion", "drop-off"].
    :type value: str
    """

    allowed_values = {
        "conversion",
        "drop-off",
    }
    CONVERSION: ClassVar["JourneyMapConversionType"]
    DROP_OFF: ClassVar["JourneyMapConversionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


JourneyMapConversionType.CONVERSION = JourneyMapConversionType("conversion")
JourneyMapConversionType.DROP_OFF = JourneyMapConversionType("drop-off")
