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


class GovernanceLimitQueryConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "chart_type": (str,),
            "comparison_shift": (str,),
            "default_value": (int,),
            "directionality": (str,),
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
        chart_type: Union[str, UnsetType] = unset,
        comparison_shift: Union[str, UnsetType] = unset,
        default_value: Union[int, UnsetType] = unset,
        directionality: Union[str, UnsetType] = unset,
        effective_time_window_days: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        The query execution context used to visualize a limit and its usage.

        :param chart_type: The chart type used to visualize the limit and its usage.
        :type chart_type: str, optional

        :param comparison_shift: The time shift applied to compare current usage against a prior period.
        :type comparison_shift: str, optional

        :param default_value: The default value used for the limit when no explicit value is configured.
        :type default_value: int, optional

        :param directionality: The direction in which usage approaches the limit, indicating whether higher or lower values are closer to the limit.
        :type directionality: str, optional

        :param effective_time_window_days: The number of days of data the limit query evaluates over.
        :type effective_time_window_days: int, optional
        """
        if chart_type is not unset:
            kwargs["chart_type"] = chart_type
        if comparison_shift is not unset:
            kwargs["comparison_shift"] = comparison_shift
        if default_value is not unset:
            kwargs["default_value"] = default_value
        if directionality is not unset:
            kwargs["directionality"] = directionality
        if effective_time_window_days is not unset:
            kwargs["effective_time_window_days"] = effective_time_window_days
        super().__init__(kwargs)
