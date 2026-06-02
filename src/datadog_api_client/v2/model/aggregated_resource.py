# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.aggregated_resource_timing_breakdown import AggregatedResourceTimingBreakdown


class AggregatedResource(ModelNormal):
    validations = {
        "cached_count": {
            "inclusive_maximum": 2147483647,
        },
        "downloaded_count": {
            "inclusive_maximum": 2147483647,
        },
        "global_view_name_count": {
            "inclusive_maximum": 2147483647,
        },
        "total_requests": {
            "inclusive_maximum": 2147483647,
        },
        "views_with_resource": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aggregated_resource_timing_breakdown import AggregatedResourceTimingBreakdown

        return {
            "avg_duration_ms": (float,),
            "avg_start_time_ms": (float,),
            "cache_hit_rate_pct": (float,),
            "cached_count": (int,),
            "downloaded_count": (int,),
            "global_p75_duration_ms": (float,),
            "global_view_name_count": (int,),
            "global_view_name_pct": (float,),
            "http_method": (str, none_type),
            "load_frequency_pct": (float,),
            "max_duration_ms": (float,),
            "median_duration_ms": (float,),
            "min_duration_ms": (float,),
            "p75_duration_ms": (float,),
            "p95_duration_ms": (float,),
            "resource_type": (str, none_type),
            "resource_url_path_group": (str,),
            "timing_breakdown": (AggregatedResourceTimingBreakdown,),
            "total_requests": (int,),
            "views_with_resource": (int,),
        }

    attribute_map = {
        "avg_duration_ms": "avg_duration_ms",
        "avg_start_time_ms": "avg_start_time_ms",
        "cache_hit_rate_pct": "cache_hit_rate_pct",
        "cached_count": "cached_count",
        "downloaded_count": "downloaded_count",
        "global_p75_duration_ms": "global_p75_duration_ms",
        "global_view_name_count": "global_view_name_count",
        "global_view_name_pct": "global_view_name_pct",
        "http_method": "http_method",
        "load_frequency_pct": "load_frequency_pct",
        "max_duration_ms": "max_duration_ms",
        "median_duration_ms": "median_duration_ms",
        "min_duration_ms": "min_duration_ms",
        "p75_duration_ms": "p75_duration_ms",
        "p95_duration_ms": "p95_duration_ms",
        "resource_type": "resource_type",
        "resource_url_path_group": "resource_url_path_group",
        "timing_breakdown": "timing_breakdown",
        "total_requests": "total_requests",
        "views_with_resource": "views_with_resource",
    }

    def __init__(
        self_,
        avg_duration_ms: float,
        avg_start_time_ms: float,
        cache_hit_rate_pct: float,
        cached_count: int,
        downloaded_count: int,
        http_method: Union[str, none_type],
        load_frequency_pct: float,
        max_duration_ms: float,
        median_duration_ms: float,
        min_duration_ms: float,
        p75_duration_ms: float,
        p95_duration_ms: float,
        resource_type: Union[str, none_type],
        resource_url_path_group: str,
        timing_breakdown: AggregatedResourceTimingBreakdown,
        total_requests: int,
        views_with_resource: int,
        global_p75_duration_ms: Union[float, UnsetType] = unset,
        global_view_name_count: Union[int, UnsetType] = unset,
        global_view_name_pct: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        Aggregated performance statistics for a single network resource across sampled view instances.

        :param avg_duration_ms: Average total duration in milliseconds.
        :type avg_duration_ms: float

        :param avg_start_time_ms: Average start time relative to view start in milliseconds.
        :type avg_start_time_ms: float

        :param cache_hit_rate_pct: Cache hit rate as a percentage.
        :type cache_hit_rate_pct: float

        :param cached_count: Number of requests served from cache.
        :type cached_count: int

        :param downloaded_count: Number of requests downloaded from the network.
        :type downloaded_count: int

        :param global_p75_duration_ms: 75th percentile duration across all view names in the application, present when include_global_appearance is true.
        :type global_p75_duration_ms: float, optional

        :param global_view_name_count: Number of distinct view names in the application that load this resource, present when include_global_appearance is true.
        :type global_view_name_count: int, optional

        :param global_view_name_pct: Percentage of distinct view names in the application that load this resource, present when include_global_appearance is true.
        :type global_view_name_pct: float, optional

        :param http_method: HTTP method for the resource request.
        :type http_method: str, none_type

        :param load_frequency_pct: Percentage of sampled view instances that loaded this resource.
        :type load_frequency_pct: float

        :param max_duration_ms: Maximum duration in milliseconds.
        :type max_duration_ms: float

        :param median_duration_ms: Median duration in milliseconds.
        :type median_duration_ms: float

        :param min_duration_ms: Minimum duration in milliseconds.
        :type min_duration_ms: float

        :param p75_duration_ms: 75th percentile duration in milliseconds.
        :type p75_duration_ms: float

        :param p95_duration_ms: 95th percentile duration in milliseconds.
        :type p95_duration_ms: float

        :param resource_type: Resource type (JS, CSS, image, fetch, XHR, document, and so on).
        :type resource_type: str, none_type

        :param resource_url_path_group: URL path group used to aggregate similar resources.
        :type resource_url_path_group: str

        :param timing_breakdown: Average timing breakdown per network phase for a resource.
        :type timing_breakdown: AggregatedResourceTimingBreakdown

        :param total_requests: Total number of requests for this resource across all sampled views.
        :type total_requests: int

        :param views_with_resource: Number of sampled view instances that loaded this resource.
        :type views_with_resource: int
        """
        if global_p75_duration_ms is not unset:
            kwargs["global_p75_duration_ms"] = global_p75_duration_ms
        if global_view_name_count is not unset:
            kwargs["global_view_name_count"] = global_view_name_count
        if global_view_name_pct is not unset:
            kwargs["global_view_name_pct"] = global_view_name_pct
        super().__init__(kwargs)

        self_.avg_duration_ms = avg_duration_ms
        self_.avg_start_time_ms = avg_start_time_ms
        self_.cache_hit_rate_pct = cache_hit_rate_pct
        self_.cached_count = cached_count
        self_.downloaded_count = downloaded_count
        self_.http_method = http_method
        self_.load_frequency_pct = load_frequency_pct
        self_.max_duration_ms = max_duration_ms
        self_.median_duration_ms = median_duration_ms
        self_.min_duration_ms = min_duration_ms
        self_.p75_duration_ms = p75_duration_ms
        self_.p95_duration_ms = p95_duration_ms
        self_.resource_type = resource_type
        self_.resource_url_path_group = resource_url_path_group
        self_.timing_breakdown = timing_breakdown
        self_.total_requests = total_requests
        self_.views_with_resource = views_with_resource
