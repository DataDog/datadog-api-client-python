# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.base_product_analytics_query import BaseProductAnalyticsQuery
    from datadog_api_client.v1_20270101.model.retention_search_return_criteria_time_interval import (
        RetentionSearchReturnCriteriaTimeInterval,
    )
    from datadog_api_client.v1_20270101.model.product_analytics_event_query import ProductAnalyticsEventQuery
    from datadog_api_client.v1_20270101.model.product_analytics_event_occurrence_query import (
        ProductAnalyticsEventOccurrenceQuery,
    )


class RetentionSearchReturnCriteria(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.base_product_analytics_query import BaseProductAnalyticsQuery
        from datadog_api_client.v1_20270101.model.retention_search_return_criteria_time_interval import (
            RetentionSearchReturnCriteriaTimeInterval,
        )

        return {
            "base_query": (BaseProductAnalyticsQuery,),
            "time_interval": (RetentionSearchReturnCriteriaTimeInterval,),
        }

    attribute_map = {
        "base_query": "base_query",
        "time_interval": "time_interval",
    }

    def __init__(
        self_,
        base_query: Union[BaseProductAnalyticsQuery, ProductAnalyticsEventQuery, ProductAnalyticsEventOccurrenceQuery],
        time_interval: Union[RetentionSearchReturnCriteriaTimeInterval, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param base_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type base_query: BaseProductAnalyticsQuery

        :param time_interval: Test-only generated schema for the dashboard versioning proof of concept.
        :type time_interval: RetentionSearchReturnCriteriaTimeInterval, optional
        """
        if time_interval is not unset:
            kwargs["time_interval"] = time_interval
        super().__init__(kwargs)

        self_.base_query = base_query
