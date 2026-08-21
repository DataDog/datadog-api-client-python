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
    from datadog_api_client.v2.model.product_analytics_journey_target import ProductAnalyticsJourneyTarget
    from datadog_api_client.v2.model.product_analytics_journey_node_target import ProductAnalyticsJourneyNodeTarget
    from datadog_api_client.v2.model.product_analytics_journey_path_target import ProductAnalyticsJourneyPathTarget


class ProductAnalyticsGraphQueryCompute(ModelNormal):
    validations = {
        "aggregation": {},
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_journey_target import ProductAnalyticsJourneyTarget

        return {
            "aggregation": (str,),
            "interval": (int,),
            "metric": (str,),
            "target": (ProductAnalyticsJourneyTarget,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "interval": "interval",
        "metric": "metric",
        "target": "target",
    }

    def __init__(
        self_,
        aggregation: str,
        interval: Union[int, UnsetType] = unset,
        metric: Union[str, UnsetType] = unset,
        target: Union[
            ProductAnalyticsJourneyTarget,
            ProductAnalyticsJourneyNodeTarget,
            ProductAnalyticsJourneyPathTarget,
            UnsetType,
        ] = unset,
        **kwargs,
    ):
        """
        Defines the metric computed over the journey.

        :param aggregation: Aggregation function: ``count`` , ``cardinality`` , ``avg`` , ``median`` , ``min`` , ``max`` , ``sum`` ,
            or a percentile of the form ``pc<N>`` such as ``pc95``. Defaults to ``cardinality``.
        :type aggregation: str

        :param interval: Time bucket interval in milliseconds, used by timeseries queries.
        :type interval: int, optional

        :param metric: Metric to aggregate on. Use a facet path such as ``@view.time_spent`` , or one of the
            journey metrics ``__dd.conversion`` , ``__dd.conversion_rate`` , ``__dd.time_to_convert`` ,
            or ``__dd.dropoff_rate``. Defaults to ``__dd.conversion``.
        :type metric: str, optional

        :param target: A reference to a step, or a range of steps, in the journey.
            Use a ``node`` target to name a single step, or a ``path`` target to name the range
            between two steps.
        :type target: ProductAnalyticsJourneyTarget, optional
        """
        if interval is not unset:
            kwargs["interval"] = interval
        if metric is not unset:
            kwargs["metric"] = metric
        if target is not unset:
            kwargs["target"] = target
        super().__init__(kwargs)

        self_.aggregation = aggregation
