# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsJourneyConversionType(ModelSimple):
    """
    Whether to return the entities that converted at the target step, or those that dropped off.

    :param value: Must be one of ["conversion", "drop-off"].
    :type value: str
    """

    allowed_values = {
        "conversion",
        "drop-off",
    }
    CONVERSION: ClassVar["ProductAnalyticsJourneyConversionType"]
    DROP_OFF: ClassVar["ProductAnalyticsJourneyConversionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsJourneyConversionType.CONVERSION = ProductAnalyticsJourneyConversionType("conversion")
ProductAnalyticsJourneyConversionType.DROP_OFF = ProductAnalyticsJourneyConversionType("drop-off")
