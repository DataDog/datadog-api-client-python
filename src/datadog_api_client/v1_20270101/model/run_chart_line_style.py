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
    from datadog_api_client.v1_20270101.model.timeseries_color_order import TimeseriesColorOrder
    from datadog_api_client.v1_20270101.model.widget_line_width import WidgetLineWidth


class RunChartLineStyle(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.timeseries_color_order import TimeseriesColorOrder
        from datadog_api_client.v1_20270101.model.widget_line_width import WidgetLineWidth

        return {
            "color_order": (TimeseriesColorOrder,),
            "line_width": (WidgetLineWidth,),
            "palette": (str,),
        }

    attribute_map = {
        "color_order": "color_order",
        "line_width": "line_width",
        "palette": "palette",
    }

    def __init__(
        self_,
        color_order: Union[TimeseriesColorOrder, UnsetType] = unset,
        line_width: Union[WidgetLineWidth, UnsetType] = unset,
        palette: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param color_order: Test-only generated schema for the dashboard versioning proof of concept.
        :type color_order: TimeseriesColorOrder, optional

        :param line_width: Test-only generated schema for the dashboard versioning proof of concept.
        :type line_width: WidgetLineWidth, optional

        :param palette: Test-only generated schema for the dashboard versioning proof of concept.
        :type palette: str, optional
        """
        if color_order is not unset:
            kwargs["color_order"] = color_order
        if line_width is not unset:
            kwargs["line_width"] = line_width
        if palette is not unset:
            kwargs["palette"] = palette
        super().__init__(kwargs)
