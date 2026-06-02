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
    from datadog_api_client.v2.model.long_task_stats_per_view import LongTaskStatsPerView


class TopLongTaskInvoker(ModelNormal):
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

        return {
            "criteria_view_occurrences": (int,),
            "file": (str, none_type),
            "impact_score": (float,),
            "invoker": (str,),
            "stats_per_view": (LongTaskStatsPerView,),
            "view_occurrences": (int,),
        }

    attribute_map = {
        "criteria_view_occurrences": "criteria_view_occurrences",
        "file": "file",
        "impact_score": "impact_score",
        "invoker": "invoker",
        "stats_per_view": "stats_per_view",
        "view_occurrences": "view_occurrences",
    }

    def __init__(
        self_,
        file: Union[str, none_type],
        invoker: str,
        stats_per_view: LongTaskStatsPerView,
        view_occurrences: int,
        criteria_view_occurrences: Union[int, UnsetType] = unset,
        impact_score: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        A top long task invoker within an invoker type.

        :param criteria_view_occurrences: Number of sampled views where this invoker had long tasks contributing to the criteria metric.
        :type criteria_view_occurrences: int, optional

        :param file: Cleaned source file path for the invoker script.
        :type file: str, none_type

        :param impact_score: Rank-product impact score combining view frequency and blocking time severity.
        :type impact_score: float, optional

        :param invoker: Name of the invoker function or script.
        :type invoker: str

        :param stats_per_view: Statistical distributions of long task metrics computed per view across sampled views.
        :type stats_per_view: LongTaskStatsPerView

        :param view_occurrences: Number of sampled views where this invoker had any long tasks.
        :type view_occurrences: int
        """
        if criteria_view_occurrences is not unset:
            kwargs["criteria_view_occurrences"] = criteria_view_occurrences
        if impact_score is not unset:
            kwargs["impact_score"] = impact_score
        super().__init__(kwargs)

        self_.file = file
        self_.invoker = invoker
        self_.stats_per_view = stats_per_view
        self_.view_occurrences = view_occurrences
