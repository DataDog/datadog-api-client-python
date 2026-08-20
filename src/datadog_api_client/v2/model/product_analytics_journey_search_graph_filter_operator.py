# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsJourneySearchGraphFilterOperator(ModelSimple):
    """
    Comparison operator applied to the graph filter value.

    :param value: Must be one of ["=", "<", ">", "<=", ">="].
    :type value: str
    """

    allowed_values = {
        "=",
        "<",
        ">",
        "<=",
        ">=",
    }
    EQUAL: ClassVar["ProductAnalyticsJourneySearchGraphFilterOperator"]
    LESS_THAN: ClassVar["ProductAnalyticsJourneySearchGraphFilterOperator"]
    GREATER_THAN: ClassVar["ProductAnalyticsJourneySearchGraphFilterOperator"]
    LESS_THAN_OR_EQUAL: ClassVar["ProductAnalyticsJourneySearchGraphFilterOperator"]
    GREATER_THAN_OR_EQUAL: ClassVar["ProductAnalyticsJourneySearchGraphFilterOperator"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsJourneySearchGraphFilterOperator.EQUAL = ProductAnalyticsJourneySearchGraphFilterOperator("=")
ProductAnalyticsJourneySearchGraphFilterOperator.LESS_THAN = ProductAnalyticsJourneySearchGraphFilterOperator("<")
ProductAnalyticsJourneySearchGraphFilterOperator.GREATER_THAN = ProductAnalyticsJourneySearchGraphFilterOperator(">")
ProductAnalyticsJourneySearchGraphFilterOperator.LESS_THAN_OR_EQUAL = ProductAnalyticsJourneySearchGraphFilterOperator(
    "<="
)
ProductAnalyticsJourneySearchGraphFilterOperator.GREATER_THAN_OR_EQUAL = (
    ProductAnalyticsJourneySearchGraphFilterOperator(">=")
)
