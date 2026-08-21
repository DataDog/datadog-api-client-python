# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsJourneyComputedColumnName(ModelSimple):
    """
    Name of a computed column to add to each row.

    :param value: If omitted defaults to "first_conversion_timestamps". Must be one of ["first_conversion_timestamps"].
    :type value: str
    """

    allowed_values = {
        "first_conversion_timestamps",
    }
    FIRST_CONVERSION_TIMESTAMPS: ClassVar["ProductAnalyticsJourneyComputedColumnName"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsJourneyComputedColumnName.FIRST_CONVERSION_TIMESTAMPS = ProductAnalyticsJourneyComputedColumnName(
    "first_conversion_timestamps"
)
