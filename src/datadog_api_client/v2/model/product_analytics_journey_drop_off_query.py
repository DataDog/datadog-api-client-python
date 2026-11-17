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
    from datadog_api_client.v2.model.product_analytics_sampling import ProductAnalyticsSampling
    from datadog_api_client.v2.model.product_analytics_journey_search import ProductAnalyticsJourneySearch
    from datadog_api_client.v2.model.product_analytics_journey_node_target import ProductAnalyticsJourneyNodeTarget
    from datadog_api_client.v2.model.product_analytics_journey_node_target import ProductAnalyticsJourneyNodeTarget


class ProductAnalyticsJourneyDropOffQuery(ModelNormal):
    validations = {
        "top_issue_count": {
            "inclusive_maximum": 100,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_sampling import ProductAnalyticsSampling
        from datadog_api_client.v2.model.product_analytics_journey_search import ProductAnalyticsJourneySearch
        from datadog_api_client.v2.model.product_analytics_journey_node_target import ProductAnalyticsJourneyNodeTarget

        return {
            "sampling": (ProductAnalyticsSampling,),
            "search": (ProductAnalyticsJourneySearch,),
            "target": (ProductAnalyticsJourneyNodeTarget,),
            "top_issue_count": (int,),
        }

    attribute_map = {
        "sampling": "sampling",
        "search": "search",
        "target": "target",
        "top_issue_count": "top_issue_count",
    }

    def __init__(
        self_,
        search: ProductAnalyticsJourneySearch,
        sampling: Union[ProductAnalyticsSampling, UnsetType] = unset,
        target: Union[ProductAnalyticsJourneyNodeTarget, UnsetType] = unset,
        top_issue_count: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Query definition for a journey drop-off analysis request.

        :param sampling: Sampling configuration for a query.
        :type sampling: ProductAnalyticsSampling, optional

        :param search: Defines the steps of the journey and the filters applied to it.
        :type search: ProductAnalyticsJourneySearch

        :param target: A reference to a single step of the journey.
        :type target: ProductAnalyticsJourneyNodeTarget, optional

        :param top_issue_count: Maximum number of issues to return.
        :type top_issue_count: int, optional
        """
        if sampling is not unset:
            kwargs["sampling"] = sampling
        if target is not unset:
            kwargs["target"] = target
        if top_issue_count is not unset:
            kwargs["top_issue_count"] = top_issue_count
        super().__init__(kwargs)

        self_.search = search
