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
    from datadog_api_client.v1.model.funnel_comparison_custom_timeframe import FunnelComparisonCustomTimeframe
    from datadog_api_client.v1.model.funnel_comparison_duration_type import FunnelComparisonDurationType


class FunnelComparisonDuration(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.funnel_comparison_custom_timeframe import FunnelComparisonCustomTimeframe
        from datadog_api_client.v1.model.funnel_comparison_duration_type import FunnelComparisonDurationType

        return {
            "custom_timeframe": (FunnelComparisonCustomTimeframe,),
            "type": (FunnelComparisonDurationType,),
        }

    attribute_map = {
        "custom_timeframe": "custom_timeframe",
        "type": "type",
    }

    def __init__(
        self_,
        type: FunnelComparisonDurationType,
        custom_timeframe: Union[FunnelComparisonCustomTimeframe, UnsetType] = unset,
        **kwargs,
    ):
        """
        Comparison time configuration for funnel widgets.

        :param custom_timeframe: Custom timeframe for funnel comparison.
        :type custom_timeframe: FunnelComparisonCustomTimeframe, optional

        :param type: Type of comparison duration.
        :type type: FunnelComparisonDurationType
        """
        if custom_timeframe is not unset:
            kwargs["custom_timeframe"] = custom_timeframe
        super().__init__(kwargs)

        self_.type = type
