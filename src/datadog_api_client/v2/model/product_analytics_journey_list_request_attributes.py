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
    from datadog_api_client.v2.model.product_analytics_journey_list_query import ProductAnalyticsJourneyListQuery


class ProductAnalyticsJourneyListRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_journey_list_query import ProductAnalyticsJourneyListQuery

        return {
            "_from": (int,),
            "query": (ProductAnalyticsJourneyListQuery,),
            "to": (int,),
        }

    attribute_map = {
        "_from": "from",
        "query": "query",
        "to": "to",
    }

    def __init__(self_, _from: int, query: ProductAnalyticsJourneyListQuery, to: int, **kwargs):
        """
        Attributes of a journey list request.

        :param _from: Start of the query window, in epoch milliseconds.
        :type _from: int

        :param query: Query definition for a journey list request.
        :type query: ProductAnalyticsJourneyListQuery

        :param to: End of the query window, in epoch milliseconds.
        :type to: int
        """
        super().__init__(kwargs)

        self_._from = _from
        self_.query = query
        self_.to = to
