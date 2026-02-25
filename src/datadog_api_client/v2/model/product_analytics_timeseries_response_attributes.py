# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.product_analytics_interval import ProductAnalyticsInterval
    from datadog_api_client.v2.model.product_analytics_serie import ProductAnalyticsSerie


class ProductAnalyticsTimeseriesResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_interval import ProductAnalyticsInterval
        from datadog_api_client.v2.model.product_analytics_serie import ProductAnalyticsSerie

        return {
            "intervals": ([ProductAnalyticsInterval],),
            "series": ([ProductAnalyticsSerie],),
            "times": ([int],),
            "values": ([[float, none_type]],),
        }

    attribute_map = {
        "intervals": "intervals",
        "series": "series",
        "times": "times",
        "values": "values",
    }

    def __init__(
        self_,
        intervals: Union[List[ProductAnalyticsInterval], UnsetType] = unset,
        series: Union[List[ProductAnalyticsSerie], UnsetType] = unset,
        times: Union[List[int], UnsetType] = unset,
        values: Union[List[List[float]], UnsetType] = unset,
        **kwargs,
    ):
        """


        :param intervals:
        :type intervals: [ProductAnalyticsInterval], optional

        :param series:
        :type series: [ProductAnalyticsSerie], optional

        :param times: Timestamps for each data point (epoch milliseconds).
        :type times: [int], optional

        :param values: Values for each series at each time point.
        :type values: [[float, none_type]], optional
        """
        if intervals is not unset:
            kwargs["intervals"] = intervals
        if series is not unset:
            kwargs["series"] = series
        if times is not unset:
            kwargs["times"] = times
        if values is not unset:
            kwargs["values"] = values
        super().__init__(kwargs)
