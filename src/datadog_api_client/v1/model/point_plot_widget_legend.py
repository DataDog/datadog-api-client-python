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
    from datadog_api_client.v1.model.point_plot_widget_legend_type import PointPlotWidgetLegendType


class PointPlotWidgetLegend(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.point_plot_widget_legend_type import PointPlotWidgetLegendType

        return {
            "type": (PointPlotWidgetLegendType,),
        }

    attribute_map = {
        "type": "type",
    }

    def __init__(self_, type: PointPlotWidgetLegendType, **kwargs):
        """
        Legend configuration for the point plot widget.

        :param type: Type of legend to show for the point plot widget.
        :type type: PointPlotWidgetLegendType
        """
        super().__init__(kwargs)

        self_.type = type
