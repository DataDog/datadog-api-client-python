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
    from datadog_api_client.v1.model.product_analytics_base_query import ProductAnalyticsBaseQuery
    from datadog_api_client.v1.model.retention_cohort_criteria_time_interval import RetentionCohortCriteriaTimeInterval


class RetentionCohortCriteria(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.product_analytics_base_query import ProductAnalyticsBaseQuery
        from datadog_api_client.v1.model.retention_cohort_criteria_time_interval import (
            RetentionCohortCriteriaTimeInterval,
        )

        return {
            "base_query": (ProductAnalyticsBaseQuery,),
            "time_interval": (RetentionCohortCriteriaTimeInterval,),
        }

    attribute_map = {
        "base_query": "base_query",
        "time_interval": "time_interval",
    }

    def __init__(
        self_, base_query: ProductAnalyticsBaseQuery, time_interval: RetentionCohortCriteriaTimeInterval, **kwargs
    ):
        """
        Cohort criteria for retention queries.

        :param base_query: Product Analytics event query.
        :type base_query: ProductAnalyticsBaseQuery

        :param time_interval: Time interval for cohort criteria.
        :type time_interval: RetentionCohortCriteriaTimeInterval
        """
        super().__init__(kwargs)

        self_.base_query = base_query
        self_.time_interval = time_interval
