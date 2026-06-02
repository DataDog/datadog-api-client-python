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
    from datadog_api_client.v2.model.long_task_metric_stats import LongTaskMetricStats


class LongTaskStatsPerView(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.long_task_metric_stats import LongTaskMetricStats

        return {
            "fcp_blocking_time_ms": (LongTaskMetricStats,),
            "fcp_count": (LongTaskMetricStats,),
            "inp_overlap_blocking_time_ms": (LongTaskMetricStats,),
            "inp_overlap_count": (LongTaskMetricStats,),
            "lcp_blocking_time_ms": (LongTaskMetricStats,),
            "lcp_count": (LongTaskMetricStats,),
            "loading_time_blocking_time_ms": (LongTaskMetricStats,),
            "loading_time_count": (LongTaskMetricStats,),
            "total_blocking_time_ms": (LongTaskMetricStats,),
            "total_count": (LongTaskMetricStats,),
        }

    attribute_map = {
        "fcp_blocking_time_ms": "fcp_blocking_time_ms",
        "fcp_count": "fcp_count",
        "inp_overlap_blocking_time_ms": "inp_overlap_blocking_time_ms",
        "inp_overlap_count": "inp_overlap_count",
        "lcp_blocking_time_ms": "lcp_blocking_time_ms",
        "lcp_count": "lcp_count",
        "loading_time_blocking_time_ms": "loading_time_blocking_time_ms",
        "loading_time_count": "loading_time_count",
        "total_blocking_time_ms": "total_blocking_time_ms",
        "total_count": "total_count",
    }

    def __init__(
        self_,
        fcp_blocking_time_ms: Union[LongTaskMetricStats, UnsetType] = unset,
        fcp_count: Union[LongTaskMetricStats, UnsetType] = unset,
        inp_overlap_blocking_time_ms: Union[LongTaskMetricStats, UnsetType] = unset,
        inp_overlap_count: Union[LongTaskMetricStats, UnsetType] = unset,
        lcp_blocking_time_ms: Union[LongTaskMetricStats, UnsetType] = unset,
        lcp_count: Union[LongTaskMetricStats, UnsetType] = unset,
        loading_time_blocking_time_ms: Union[LongTaskMetricStats, UnsetType] = unset,
        loading_time_count: Union[LongTaskMetricStats, UnsetType] = unset,
        total_blocking_time_ms: Union[LongTaskMetricStats, UnsetType] = unset,
        total_count: Union[LongTaskMetricStats, UnsetType] = unset,
        **kwargs,
    ):
        """
        Statistical distributions of long task metrics computed per view across sampled views.

        :param fcp_blocking_time_ms: Statistical distribution (average, min, max) of a long task metric across sampled views.
        :type fcp_blocking_time_ms: LongTaskMetricStats, optional

        :param fcp_count: Statistical distribution (average, min, max) of a long task metric across sampled views.
        :type fcp_count: LongTaskMetricStats, optional

        :param inp_overlap_blocking_time_ms: Statistical distribution (average, min, max) of a long task metric across sampled views.
        :type inp_overlap_blocking_time_ms: LongTaskMetricStats, optional

        :param inp_overlap_count: Statistical distribution (average, min, max) of a long task metric across sampled views.
        :type inp_overlap_count: LongTaskMetricStats, optional

        :param lcp_blocking_time_ms: Statistical distribution (average, min, max) of a long task metric across sampled views.
        :type lcp_blocking_time_ms: LongTaskMetricStats, optional

        :param lcp_count: Statistical distribution (average, min, max) of a long task metric across sampled views.
        :type lcp_count: LongTaskMetricStats, optional

        :param loading_time_blocking_time_ms: Statistical distribution (average, min, max) of a long task metric across sampled views.
        :type loading_time_blocking_time_ms: LongTaskMetricStats, optional

        :param loading_time_count: Statistical distribution (average, min, max) of a long task metric across sampled views.
        :type loading_time_count: LongTaskMetricStats, optional

        :param total_blocking_time_ms: Statistical distribution (average, min, max) of a long task metric across sampled views.
        :type total_blocking_time_ms: LongTaskMetricStats, optional

        :param total_count: Statistical distribution (average, min, max) of a long task metric across sampled views.
        :type total_count: LongTaskMetricStats, optional
        """
        if fcp_blocking_time_ms is not unset:
            kwargs["fcp_blocking_time_ms"] = fcp_blocking_time_ms
        if fcp_count is not unset:
            kwargs["fcp_count"] = fcp_count
        if inp_overlap_blocking_time_ms is not unset:
            kwargs["inp_overlap_blocking_time_ms"] = inp_overlap_blocking_time_ms
        if inp_overlap_count is not unset:
            kwargs["inp_overlap_count"] = inp_overlap_count
        if lcp_blocking_time_ms is not unset:
            kwargs["lcp_blocking_time_ms"] = lcp_blocking_time_ms
        if lcp_count is not unset:
            kwargs["lcp_count"] = lcp_count
        if loading_time_blocking_time_ms is not unset:
            kwargs["loading_time_blocking_time_ms"] = loading_time_blocking_time_ms
        if loading_time_count is not unset:
            kwargs["loading_time_count"] = loading_time_count
        if total_blocking_time_ms is not unset:
            kwargs["total_blocking_time_ms"] = total_blocking_time_ms
        if total_count is not unset:
            kwargs["total_count"] = total_count
        super().__init__(kwargs)
