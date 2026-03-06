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
    from datadog_api_client.v1.model.widget_line_type import WidgetLineType
    from datadog_api_client.v1.model.widget_line_width import WidgetLineWidth
    from datadog_api_client.v1.model.widget_style_order_by import WidgetStyleOrderBy


class TimeseriesRequestStyle(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_line_type import WidgetLineType
        from datadog_api_client.v1.model.widget_line_width import WidgetLineWidth
        from datadog_api_client.v1.model.widget_style_order_by import WidgetStyleOrderBy

        return {
            "has_value_labels": (bool,),
            "line_type": (WidgetLineType,),
            "line_width": (WidgetLineWidth,),
            "order_by": (WidgetStyleOrderBy,),
            "palette": (str,),
        }

    attribute_map = {
        "has_value_labels": "has_value_labels",
        "line_type": "line_type",
        "line_width": "line_width",
        "order_by": "order_by",
        "palette": "palette",
    }

    def __init__(
        self_,
        has_value_labels: Union[bool, UnsetType] = unset,
        line_type: Union[WidgetLineType, UnsetType] = unset,
        line_width: Union[WidgetLineWidth, UnsetType] = unset,
        order_by: Union[WidgetStyleOrderBy, UnsetType] = unset,
        palette: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Define request widget style for timeseries widgets.

        :param has_value_labels: If true, the value is displayed as a label relative to the data point.
        :type has_value_labels: bool, optional

        :param line_type: Type of lines displayed.
        :type line_type: WidgetLineType, optional

        :param line_width: Width of line displayed.
        :type line_width: WidgetLineWidth, optional

        :param order_by: How to order series in timeseries visualizations.

            * ``tags`` : Order series alphabetically by tag name (default behavior)
            * ``values`` : Order series by their current metric values (typically descending)
        :type order_by: WidgetStyleOrderBy, optional

        :param palette: Color palette to apply to the widget.
        :type palette: str, optional
        """
        if has_value_labels is not unset:
            kwargs["has_value_labels"] = has_value_labels
        if line_type is not unset:
            kwargs["line_type"] = line_type
        if line_width is not unset:
            kwargs["line_width"] = line_width
        if order_by is not unset:
            kwargs["order_by"] = order_by
        if palette is not unset:
            kwargs["palette"] = palette
        super().__init__(kwargs)
