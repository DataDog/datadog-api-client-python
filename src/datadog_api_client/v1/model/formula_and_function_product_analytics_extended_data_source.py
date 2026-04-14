# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FormulaAndFunctionProductAnalyticsExtendedDataSource(ModelSimple):
    """
    Data source for Product Analytics Extended queries.

    :param value: If omitted defaults to "product_analytics_extended". Must be one of ["product_analytics_extended"].
    :type value: str
    """

    allowed_values = {
        "product_analytics_extended",
    }
    PRODUCT_ANALYTICS_EXTENDED: ClassVar["FormulaAndFunctionProductAnalyticsExtendedDataSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FormulaAndFunctionProductAnalyticsExtendedDataSource.PRODUCT_ANALYTICS_EXTENDED = (
    FormulaAndFunctionProductAnalyticsExtendedDataSource("product_analytics_extended")
)
