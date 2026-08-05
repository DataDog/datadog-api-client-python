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
    from datadog_api_client.v2.model.governance_insight_directionality import GovernanceInsightDirectionality


class GovernanceInsightQueryConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.governance_insight_directionality import GovernanceInsightDirectionality

        return {
            "chart_type": (str,),
            "comparison_shift": (str,),
            "default_value": (int,),
            "directionality": (GovernanceInsightDirectionality,),
            "effective_time_window_days": (int,),
        }

    attribute_map = {
        "chart_type": "chart_type",
        "comparison_shift": "comparison_shift",
        "default_value": "default_value",
        "directionality": "directionality",
        "effective_time_window_days": "effective_time_window_days",
    }

    def __init__(
        self_,
        comparison_shift: str,
        effective_time_window_days: int,
        chart_type: Union[str, UnsetType] = unset,
        default_value: Union[int, UnsetType] = unset,
        directionality: Union[GovernanceInsightDirectionality, UnsetType] = unset,
        **kwargs,
    ):
        """
        Query execution context for running insight queries directly.

        :param chart_type: The chart type used to render the insight.
        :type chart_type: str, optional

        :param comparison_shift: The window used for the previous value comparison; for example, ``week`` or ``month``.
        :type comparison_shift: str

        :param default_value: The default value to display when no data is available.
        :type default_value: int, optional

        :param directionality: Whether an increase in the insight's value is good, bad, or neutral.
        :type directionality: GovernanceInsightDirectionality, optional

        :param effective_time_window_days: The number of days the insight value is computed over.
        :type effective_time_window_days: int
        """
        if chart_type is not unset:
            kwargs["chart_type"] = chart_type
        if default_value is not unset:
            kwargs["default_value"] = default_value
        if directionality is not unset:
            kwargs["directionality"] = directionality
        super().__init__(kwargs)

        self_.comparison_shift = comparison_shift
        self_.effective_time_window_days = effective_time_window_days
