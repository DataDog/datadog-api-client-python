# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class ProductAnalyticsCompute(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "aggregation": (str,),
            "interval": (int,),
            "metric": (str,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "interval": "interval",
        "metric": "metric",
    }

    def __init__(
        self_,
        aggregation: str,
        interval: Union[int, UnsetType] = unset,
        metric: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A compute rule for aggregating data.

        :param aggregation: The aggregation function (count, cardinality, avg, sum, min, max, etc.).
        :type aggregation: str

        :param interval: Time bucket size in milliseconds. Required for timeseries queries.
        :type interval: int, optional

        :param metric: The metric to aggregate on. Required for non-count aggregations.
        :type metric: str, optional
        """
        if interval is not unset:
            kwargs["interval"] = interval
        if metric is not unset:
            kwargs["metric"] = metric
        super().__init__(kwargs)

        self_.aggregation = aggregation
