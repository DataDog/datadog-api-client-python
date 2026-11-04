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
    from datadog_api_client.v2.model.rum_metric_compute_aggregation_type import RumMetricComputeAggregationType


class RumMetricResponseCompute(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_metric_compute_aggregation_type import RumMetricComputeAggregationType

        return {
            "aggregation_type": (RumMetricComputeAggregationType,),
            "include_percentiles": (bool,),
            "path": (str,),
        }

    attribute_map = {
        "aggregation_type": "aggregation_type",
        "include_percentiles": "include_percentiles",
        "path": "path",
    }

    def __init__(
        self_,
        aggregation_type: Union[RumMetricComputeAggregationType, UnsetType] = unset,
        include_percentiles: Union[bool, UnsetType] = unset,
        path: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The compute rule of the RUM-based metric.

        :param aggregation_type: The type of aggregation to use.
            ``count`` counts the matching events. ``distribution`` aggregates the values found at ``path``.
        :type aggregation_type: RumMetricComputeAggregationType, optional

        :param include_percentiles: Toggle to include or exclude percentile aggregations (p50, p75, p90, p95, p99) for distribution metrics.
            Required when ``aggregation_type`` is ``distribution`` , and must be omitted otherwise.
        :type include_percentiles: bool, optional

        :param path: The path of the numeric RUM event attribute the metric aggregates on.
            Only present when ``aggregation_type`` is ``distribution``.
        :type path: str, optional
        """
        if aggregation_type is not unset:
            kwargs["aggregation_type"] = aggregation_type
        if include_percentiles is not unset:
            kwargs["include_percentiles"] = include_percentiles
        if path is not unset:
            kwargs["path"] = path
        super().__init__(kwargs)
