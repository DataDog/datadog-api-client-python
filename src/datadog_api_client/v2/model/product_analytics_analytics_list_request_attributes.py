# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.product_analytics_analytics_list_query import ProductAnalyticsAnalyticsListQuery


class ProductAnalyticsAnalyticsListRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_analytics_list_query import (
            ProductAnalyticsAnalyticsListQuery,
        )

        return {
            "_from": (int,),
            "query": (ProductAnalyticsAnalyticsListQuery,),
            "to": (int,),
        }

    attribute_map = {
        "_from": "from",
        "query": "query",
        "to": "to",
    }

    def __init__(self_, _from: int, query: ProductAnalyticsAnalyticsListQuery, to: int, **kwargs):
        """
        Attributes for an analytics list request.

        :param _from: Start time in epoch milliseconds. Must be less than ``to``.
        :type _from: int

        :param query: The analytics list query definition. It selects the events to return with ``query`` , then
            chooses the columns on each event row, the sort applied to those rows, and a row limit.
            Unlike the scalar and timeseries queries, a list query returns raw event rows rather than
            aggregates, so it takes no compute or group-by rule.
        :type query: ProductAnalyticsAnalyticsListQuery

        :param to: End time in epoch milliseconds.
        :type to: int
        """
        super().__init__(kwargs)

        self_._from = _from
        self_.query = query
        self_.to = to
