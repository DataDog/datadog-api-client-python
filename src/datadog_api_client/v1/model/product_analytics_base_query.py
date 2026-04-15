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
    from datadog_api_client.v1.model.product_analytics_event_data_source import ProductAnalyticsEventDataSource
    from datadog_api_client.v1.model.product_analytics_event_query_search import ProductAnalyticsEventQuerySearch


class ProductAnalyticsBaseQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.product_analytics_event_data_source import ProductAnalyticsEventDataSource
        from datadog_api_client.v1.model.product_analytics_event_query_search import ProductAnalyticsEventQuerySearch

        return {
            "data_source": (ProductAnalyticsEventDataSource,),
            "search": (ProductAnalyticsEventQuerySearch,),
        }

    attribute_map = {
        "data_source": "data_source",
        "search": "search",
    }

    def __init__(
        self_, data_source: ProductAnalyticsEventDataSource, search: ProductAnalyticsEventQuerySearch, **kwargs
    ):
        """
        Product Analytics event query.

        :param data_source: Data source for Product Analytics event queries.
        :type data_source: ProductAnalyticsEventDataSource

        :param search: Search configuration for Product Analytics event query.
        :type search: ProductAnalyticsEventQuerySearch
        """
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.search = search
