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
    from datadog_api_client.v2.model.product_analytics_occurrence_query_data_source import (
        ProductAnalyticsOccurrenceQueryDataSource,
    )
    from datadog_api_client.v2.model.product_analytics_occurrence_search import ProductAnalyticsOccurrenceSearch


class ProductAnalyticsOccurrenceQuery(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_occurrence_query_data_source import (
            ProductAnalyticsOccurrenceQueryDataSource,
        )
        from datadog_api_client.v2.model.product_analytics_occurrence_search import ProductAnalyticsOccurrenceSearch

        return {
            "data_source": (ProductAnalyticsOccurrenceQueryDataSource,),
            "search": (ProductAnalyticsOccurrenceSearch,),
        }

    attribute_map = {
        "data_source": "data_source",
        "search": "search",
    }

    def __init__(
        self_,
        data_source: ProductAnalyticsOccurrenceQueryDataSource,
        search: ProductAnalyticsOccurrenceSearch,
        **kwargs,
    ):
        """
        A Product Analytics occurrence-filtered query.

        :param data_source: The data source identifier for occurrence queries.
        :type data_source: ProductAnalyticsOccurrenceQueryDataSource

        :param search: Search parameters for an occurrence query.
        :type search: ProductAnalyticsOccurrenceSearch
        """
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.search = search
