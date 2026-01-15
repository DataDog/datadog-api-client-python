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
    from datadog_api_client.v1.model.bar_chart_widget_display import BarChartWidgetDisplay
    from datadog_api_client.v1.model.bar_chart_widget_scaling import BarChartWidgetScaling
    from datadog_api_client.v1.model.bar_chart_widget_stacked import BarChartWidgetStacked
    from datadog_api_client.v1.model.bar_chart_widget_flat import BarChartWidgetFlat


class BarChartWidgetStyle(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.bar_chart_widget_display import BarChartWidgetDisplay
        from datadog_api_client.v1.model.bar_chart_widget_scaling import BarChartWidgetScaling

        return {
            "display": (BarChartWidgetDisplay,),
            "palette": (str,),
            "scaling": (BarChartWidgetScaling,),
        }

    attribute_map = {
        "display": "display",
        "palette": "palette",
        "scaling": "scaling",
    }

    def __init__(
        self_,
        display: Union[BarChartWidgetDisplay, BarChartWidgetStacked, BarChartWidgetFlat, UnsetType] = unset,
        palette: Union[str, UnsetType] = unset,
        scaling: Union[BarChartWidgetScaling, UnsetType] = unset,
        **kwargs,
    ):
        """
        Style customization for a bar chart widget.

        :param display: Bar chart widget display options.
        :type display: BarChartWidgetDisplay, optional

        :param palette: Color palette to apply to the widget.
        :type palette: str, optional

        :param scaling: Bar chart widget scaling definition.
        :type scaling: BarChartWidgetScaling, optional
        """
        if display is not unset:
            kwargs["display"] = display
        if palette is not unset:
            kwargs["palette"] = palette
        if scaling is not unset:
            kwargs["scaling"] = scaling
        super().__init__(kwargs)
