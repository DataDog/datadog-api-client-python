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
    from datadog_api_client.v1.model.product_analytics_funnel_compute_aggregation import (
        ProductAnalyticsFunnelComputeAggregation,
    )
    from datadog_api_client.v1.model.product_analytics_funnel_compute_metric import ProductAnalyticsFunnelComputeMetric


class ProductAnalyticsFunnelCompute(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.product_analytics_funnel_compute_aggregation import (
            ProductAnalyticsFunnelComputeAggregation,
        )
        from datadog_api_client.v1.model.product_analytics_funnel_compute_metric import (
            ProductAnalyticsFunnelComputeMetric,
        )

        return {
            "aggregation": (ProductAnalyticsFunnelComputeAggregation,),
            "metric": (ProductAnalyticsFunnelComputeMetric,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "metric": "metric",
    }

    def __init__(
        self_,
        aggregation: ProductAnalyticsFunnelComputeAggregation,
        metric: ProductAnalyticsFunnelComputeMetric,
        **kwargs,
    ):
        """
        Compute configuration for user journey funnel.

        :param aggregation: Aggregation type for user journey funnel compute.
        :type aggregation: ProductAnalyticsFunnelComputeAggregation

        :param metric: Metric for user journey funnel compute. ``__dd.conversion`` and ``__dd.conversion_rate`` accept ``count`` (unique users/sessions) and ``cardinality`` (total users/sessions) as aggregations.
        :type metric: ProductAnalyticsFunnelComputeMetric
        """
        super().__init__(kwargs)

        self_.aggregation = aggregation
        self_.metric = metric
