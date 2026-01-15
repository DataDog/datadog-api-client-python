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
    from datadog_api_client.v1.model.bar_chart_widget_legend import BarChartWidgetLegend
    from datadog_api_client.v1.model.bar_chart_widget_stacked_type import BarChartWidgetStackedType


class BarChartWidgetStacked(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.bar_chart_widget_legend import BarChartWidgetLegend
        from datadog_api_client.v1.model.bar_chart_widget_stacked_type import BarChartWidgetStackedType

        return {
            "legend": (BarChartWidgetLegend,),
            "type": (BarChartWidgetStackedType,),
        }

    attribute_map = {
        "legend": "legend",
        "type": "type",
    }

    def __init__(
        self_, type: BarChartWidgetStackedType, legend: Union[BarChartWidgetLegend, UnsetType] = unset, **kwargs
    ):
        """
        Bar chart widget stacked display options.

        :param legend: Bar chart widget stacked legend behavior.
        :type legend: BarChartWidgetLegend, optional

        :param type: Bar chart widget stacked display type.
        :type type: BarChartWidgetStackedType
        """
        if legend is not unset:
            kwargs["legend"] = legend
        super().__init__(kwargs)

        self_.type = type
