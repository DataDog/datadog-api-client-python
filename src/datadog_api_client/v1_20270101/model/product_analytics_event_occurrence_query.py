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
    from datadog_api_client.v1_20270101.model.product_analytics_event_occurrence_query_data_source import (
        ProductAnalyticsEventOccurrenceQueryDataSource,
    )
    from datadog_api_client.v1_20270101.model.product_analytics_event_occurrence_query_search import (
        ProductAnalyticsEventOccurrenceQuerySearch,
    )


class ProductAnalyticsEventOccurrenceQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.product_analytics_event_occurrence_query_data_source import (
            ProductAnalyticsEventOccurrenceQueryDataSource,
        )
        from datadog_api_client.v1_20270101.model.product_analytics_event_occurrence_query_search import (
            ProductAnalyticsEventOccurrenceQuerySearch,
        )

        return {
            "data_source": (ProductAnalyticsEventOccurrenceQueryDataSource,),
            "search": (ProductAnalyticsEventOccurrenceQuerySearch,),
        }

    attribute_map = {
        "data_source": "data_source",
        "search": "search",
    }

    def __init__(
        self_,
        data_source: ProductAnalyticsEventOccurrenceQueryDataSource,
        search: ProductAnalyticsEventOccurrenceQuerySearch,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: ProductAnalyticsEventOccurrenceQueryDataSource

        :param search: Test-only generated schema for the dashboard versioning proof of concept.
        :type search: ProductAnalyticsEventOccurrenceQuerySearch
        """
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.search = search
