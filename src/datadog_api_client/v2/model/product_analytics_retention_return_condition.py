# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsRetentionReturnCondition(ModelSimple):
    """
    When an entity counts as having returned. Use `conversion_on` to count only entities that
        returned during the period itself, or `conversion_on_or_after` to also count later returns.

    :param value: Must be one of ["conversion_on", "conversion_on_or_after"].
    :type value: str
    """

    allowed_values = {
        "conversion_on",
        "conversion_on_or_after",
    }
    CONVERSION_ON: ClassVar["ProductAnalyticsRetentionReturnCondition"]
    CONVERSION_ON_OR_AFTER: ClassVar["ProductAnalyticsRetentionReturnCondition"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsRetentionReturnCondition.CONVERSION_ON = ProductAnalyticsRetentionReturnCondition("conversion_on")
ProductAnalyticsRetentionReturnCondition.CONVERSION_ON_OR_AFTER = ProductAnalyticsRetentionReturnCondition(
    "conversion_on_or_after"
)
