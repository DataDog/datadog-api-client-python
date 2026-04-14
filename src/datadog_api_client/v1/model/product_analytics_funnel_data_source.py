# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsFunnelDataSource(ModelSimple):
    """
    Data source for user journey funnel queries.

    :param value: If omitted defaults to "product_analytics_journey". Must be one of ["product_analytics_journey"].
    :type value: str
    """

    allowed_values = {
        "product_analytics_journey",
    }
    PRODUCT_ANALYTICS_JOURNEY: ClassVar["ProductAnalyticsFunnelDataSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsFunnelDataSource.PRODUCT_ANALYTICS_JOURNEY = ProductAnalyticsFunnelDataSource(
    "product_analytics_journey"
)
