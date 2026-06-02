# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.long_task_stats_per_view import LongTaskStatsPerView
    from datadog_api_client.v2.model.top_long_task_invoker import TopLongTaskInvoker


class AggregatedLongTasksByInvokerType(ModelNormal):
    validations = {
        "criteria_view_occurrences": {
            "inclusive_maximum": 2147483647,
        },
        "view_occurrences": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.long_task_stats_per_view import LongTaskStatsPerView
        from datadog_api_client.v2.model.top_long_task_invoker import TopLongTaskInvoker

        return {
            "criteria_view_occurrences": (int,),
            "impact_score": (float,),
            "invoker_type": (str,),
            "stats_per_view": (LongTaskStatsPerView,),
            "top_invokers": ([TopLongTaskInvoker],),
            "view_occurrences": (int,),
        }

    attribute_map = {
        "criteria_view_occurrences": "criteria_view_occurrences",
        "impact_score": "impact_score",
        "invoker_type": "invoker_type",
        "stats_per_view": "stats_per_view",
        "top_invokers": "top_invokers",
        "view_occurrences": "view_occurrences",
    }

    def __init__(
        self_,
        invoker_type: str,
        stats_per_view: LongTaskStatsPerView,
        top_invokers: List[TopLongTaskInvoker],
        view_occurrences: int,
        criteria_view_occurrences: Union[int, UnsetType] = unset,
        impact_score: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        Aggregated long task statistics for a single invoker type.

        :param criteria_view_occurrences: Number of sampled views where this invoker type had long tasks contributing to the criteria metric.
        :type criteria_view_occurrences: int, optional

        :param impact_score: Rank-product impact score combining view frequency and blocking time severity.
        :type impact_score: float, optional

        :param invoker_type: Category of the long task invoker (for example, resolve-promise, user-callback).
        :type invoker_type: str

        :param stats_per_view: Statistical distributions of long task metrics computed per view across sampled views.
        :type stats_per_view: LongTaskStatsPerView

        :param top_invokers: Top invokers within this invoker type, sorted by impact score descending.
        :type top_invokers: [TopLongTaskInvoker]

        :param view_occurrences: Number of sampled views where this invoker type had any long tasks.
        :type view_occurrences: int
        """
        if criteria_view_occurrences is not unset:
            kwargs["criteria_view_occurrences"] = criteria_view_occurrences
        if impact_score is not unset:
            kwargs["impact_score"] = impact_score
        super().__init__(kwargs)

        self_.invoker_type = invoker_type
        self_.stats_per_view = stats_per_view
        self_.top_invokers = top_invokers
        self_.view_occurrences = view_occurrences
