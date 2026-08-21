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
    from datadog_api_client.v2.model.product_analytics_retention_compute_metric import (
        ProductAnalyticsRetentionComputeMetric,
    )


class ProductAnalyticsRetentionCompute(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_retention_compute_metric import (
            ProductAnalyticsRetentionComputeMetric,
        )

        return {
            "aggregation": (str,),
            "metric": (ProductAnalyticsRetentionComputeMetric,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "metric": "metric",
    }

    def __init__(self_, aggregation: str, metric: ProductAnalyticsRetentionComputeMetric, **kwargs):
        """
        The metric and aggregation applied to a retention query.

        :param aggregation: The aggregation function applied to the metric, such as ``count`` or ``avg``.
        :type aggregation: str

        :param metric: The retention metric to compute, either an absolute count or a rate.
        :type metric: ProductAnalyticsRetentionComputeMetric
        """
        super().__init__(kwargs)

        self_.aggregation = aggregation
        self_.metric = metric
