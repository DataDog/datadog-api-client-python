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
    from datadog_api_client.v1.model.comparison_custom_timeframe import ComparisonCustomTimeframe
    from datadog_api_client.v1.model.comparison_duration_type import ComparisonDurationType


class ComparisonDuration(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.comparison_custom_timeframe import ComparisonCustomTimeframe
        from datadog_api_client.v1.model.comparison_duration_type import ComparisonDurationType

        return {
            "custom_timeframe": (ComparisonCustomTimeframe,),
            "type": (ComparisonDurationType,),
        }

    attribute_map = {
        "custom_timeframe": "custom_timeframe",
        "type": "type",
    }

    def __init__(
        self_,
        type: ComparisonDurationType,
        custom_timeframe: Union[ComparisonCustomTimeframe, UnsetType] = unset,
        **kwargs,
    ):
        """
        The comparison period. Use a preset ``type`` value or set ``type`` to ``custom_timeframe`` and provide ``custom_timeframe`` with explicit millisecond epoch bounds.

        :param custom_timeframe: Fixed time range for a ``custom_timeframe`` comparison.
        :type custom_timeframe: ComparisonCustomTimeframe, optional

        :param type: The comparison window type.
        :type type: ComparisonDurationType
        """
        if custom_timeframe is not unset:
            kwargs["custom_timeframe"] = custom_timeframe
        super().__init__(kwargs)

        self_.type = type
