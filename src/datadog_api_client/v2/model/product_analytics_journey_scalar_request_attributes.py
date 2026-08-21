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
    from datadog_api_client.v2.model.product_analytics_journey_scalar_query import ProductAnalyticsJourneyScalarQuery


class ProductAnalyticsJourneyScalarRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_journey_scalar_query import (
            ProductAnalyticsJourneyScalarQuery,
        )

        return {
            "_from": (int,),
            "query": (ProductAnalyticsJourneyScalarQuery,),
            "to": (int,),
        }

    attribute_map = {
        "_from": "from",
        "query": "query",
        "to": "to",
    }

    def __init__(self_, _from: int, query: ProductAnalyticsJourneyScalarQuery, to: int, **kwargs):
        """
        Attributes of a journey scalar request.

        :param _from: Start of the query window, in epoch milliseconds.
        :type _from: int

        :param query: Query definition for a journey scalar request.
        :type query: ProductAnalyticsJourneyScalarQuery

        :param to: End of the query window, in epoch milliseconds.
        :type to: int
        """
        super().__init__(kwargs)

        self_._from = _from
        self_.query = query
        self_.to = to
