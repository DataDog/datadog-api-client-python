# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.dashboard_live_timeframe_type import DashboardLiveTimeframeType
    from datadog_api_client.v1.model.widget_live_span_unit import WidgetLiveSpanUnit


class DashboardLiveTimeframe(ModelNormal):
    validations = {
        "value": {
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.dashboard_live_timeframe_type import DashboardLiveTimeframeType
        from datadog_api_client.v1.model.widget_live_span_unit import WidgetLiveSpanUnit

        return {
            "type": (DashboardLiveTimeframeType,),
            "unit": (WidgetLiveSpanUnit,),
            "value": (int,),
        }

    attribute_map = {
        "type": "type",
        "unit": "unit",
        "value": "value",
    }

    def __init__(self_, type: DashboardLiveTimeframeType, unit: WidgetLiveSpanUnit, value: int, **kwargs):
        """
        A live dashboard timeframe.

        :param type: Type of live timeframe.
        :type type: DashboardLiveTimeframeType

        :param unit: Unit of the time span.
        :type unit: WidgetLiveSpanUnit

        :param value: Value of the live timeframe span.
        :type value: int
        """
        super().__init__(kwargs)

        self_.type = type
        self_.unit = unit
        self_.value = value
