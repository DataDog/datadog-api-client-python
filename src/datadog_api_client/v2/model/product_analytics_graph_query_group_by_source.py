# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsGraphQueryGroupBySource(ModelSimple):
    """
    Audience dimension to group by, instead of an event facet.

    :param value: Must be one of ["product_analytics_audience_filters.users", "product_analytics_audience_filters.accounts"].
    :type value: str
    """

    allowed_values = {
        "product_analytics_audience_filters.users",
        "product_analytics_audience_filters.accounts",
    }
    USERS: ClassVar["ProductAnalyticsGraphQueryGroupBySource"]
    ACCOUNTS: ClassVar["ProductAnalyticsGraphQueryGroupBySource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsGraphQueryGroupBySource.USERS = ProductAnalyticsGraphQueryGroupBySource(
    "product_analytics_audience_filters.users"
)
ProductAnalyticsGraphQueryGroupBySource.ACCOUNTS = ProductAnalyticsGraphQueryGroupBySource(
    "product_analytics_audience_filters.accounts"
)
