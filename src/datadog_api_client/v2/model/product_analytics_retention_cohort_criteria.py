# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.product_analytics_base_query import ProductAnalyticsBaseQuery
    from datadog_api_client.v2.model.product_analytics_retention_time_interval import (
        ProductAnalyticsRetentionTimeInterval,
    )
    from datadog_api_client.v2.model.product_analytics_event_query import ProductAnalyticsEventQuery
    from datadog_api_client.v2.model.product_analytics_occurrence_query import ProductAnalyticsOccurrenceQuery
    from datadog_api_client.v2.model.product_analytics_retention_calendar_time_interval import (
        ProductAnalyticsRetentionCalendarTimeInterval,
    )
    from datadog_api_client.v2.model.product_analytics_retention_fixed_time_interval import (
        ProductAnalyticsRetentionFixedTimeInterval,
    )


class ProductAnalyticsRetentionCohortCriteria(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_base_query import ProductAnalyticsBaseQuery
        from datadog_api_client.v2.model.product_analytics_retention_time_interval import (
            ProductAnalyticsRetentionTimeInterval,
        )

        return {
            "base_query": (ProductAnalyticsBaseQuery,),
            "time_interval": (ProductAnalyticsRetentionTimeInterval,),
        }

    attribute_map = {
        "base_query": "base_query",
        "time_interval": "time_interval",
    }

    def __init__(
        self_,
        base_query: Union[ProductAnalyticsBaseQuery, ProductAnalyticsEventQuery, ProductAnalyticsOccurrenceQuery],
        time_interval: Union[
            ProductAnalyticsRetentionTimeInterval,
            ProductAnalyticsRetentionCalendarTimeInterval,
            ProductAnalyticsRetentionFixedTimeInterval,
        ],
        **kwargs,
    ):
        """
        Defines the event that places an entity into a cohort, and how cohorts are bucketed over time.

        :param base_query: A query definition discriminated by the ``data_source`` field.
            Use ``product_analytics`` for standard event queries, or
            ``product_analytics_occurrence`` for occurrence-filtered queries.
        :type base_query: ProductAnalyticsBaseQuery

        :param time_interval: A retention interval, either aligned to calendar boundaries or of a fixed length.
            Cohort criteria use calendar intervals; return criteria use fixed intervals.
        :type time_interval: ProductAnalyticsRetentionTimeInterval
        """
        super().__init__(kwargs)

        self_.base_query = base_query
        self_.time_interval = time_interval
