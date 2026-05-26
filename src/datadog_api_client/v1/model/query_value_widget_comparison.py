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
    from datadog_api_client.v1.model.query_value_widget_comparison_directionality import (
        QueryValueWidgetComparisonDirectionality,
    )
    from datadog_api_client.v1.model.comparison_duration import ComparisonDuration
    from datadog_api_client.v1.model.query_value_widget_comparison_type import QueryValueWidgetComparisonType


class QueryValueWidgetComparison(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.query_value_widget_comparison_directionality import (
            QueryValueWidgetComparisonDirectionality,
        )
        from datadog_api_client.v1.model.comparison_duration import ComparisonDuration
        from datadog_api_client.v1.model.query_value_widget_comparison_type import QueryValueWidgetComparisonType

        return {
            "directionality": (QueryValueWidgetComparisonDirectionality,),
            "duration": (ComparisonDuration,),
            "type": (QueryValueWidgetComparisonType,),
        }

    attribute_map = {
        "directionality": "directionality",
        "duration": "duration",
        "type": "type",
    }

    def __init__(
        self_,
        duration: ComparisonDuration,
        directionality: Union[QueryValueWidgetComparisonDirectionality, UnsetType] = unset,
        type: Union[QueryValueWidgetComparisonType, UnsetType] = unset,
        **kwargs,
    ):
        """
        A change indicator that compares the current value to a historical period.

        :param directionality: Color-coding direction: ``increase_better`` (green on rise), ``decrease_better`` (green on drop), or ``neutral`` (no color).
        :type directionality: QueryValueWidgetComparisonDirectionality, optional

        :param duration: The comparison period. Use a preset ``type`` value or set ``type`` to ``custom_timeframe`` and provide ``custom_timeframe`` with explicit millisecond epoch bounds.
        :type duration: ComparisonDuration

        :param type: How the delta is expressed: ``absolute`` (raw difference), ``relative`` (percentage), or ``both``.
        :type type: QueryValueWidgetComparisonType, optional
        """
        if directionality is not unset:
            kwargs["directionality"] = directionality
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

        self_.duration = duration
