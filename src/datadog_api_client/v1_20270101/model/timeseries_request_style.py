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
    from datadog_api_client.v1_20270101.model.widget_line_type import WidgetLineType
    from datadog_api_client.v1_20270101.model.widget_line_width import WidgetLineWidth
    from datadog_api_client.v1_20270101.model.widget_style_order_by import WidgetStyleOrderBy
    from datadog_api_client.v1_20270101.model.value_labels_density import ValueLabelsDensity


class TimeseriesRequestStyle(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.timeseries_color_order import TimeseriesColorOrder
        from datadog_api_client.v1_20270101.model.widget_line_type import WidgetLineType
        from datadog_api_client.v1_20270101.model.widget_line_width import WidgetLineWidth
        from datadog_api_client.v1_20270101.model.widget_style_order_by import WidgetStyleOrderBy
        from datadog_api_client.v1_20270101.model.value_labels_density import ValueLabelsDensity

        return {
            "color_order": (TimeseriesColorOrder,),
            "has_value_labels": (bool,),
            "line_type": (WidgetLineType,),
            "line_width": (WidgetLineWidth,),
            "order_by": (WidgetStyleOrderBy,),
            "order_reverse": (bool,),
            "palette": (str,),
            "value_labels_density": (ValueLabelsDensity,),
        }

    attribute_map = {
        "color_order": "color_order",
        "has_value_labels": "has_value_labels",
        "line_type": "line_type",
        "line_width": "line_width",
        "order_by": "order_by",
        "order_reverse": "order_reverse",
        "palette": "palette",
        "value_labels_density": "value_labels_density",
    }

    def __init__(
        self_,
        color_order: Union[TimeseriesColorOrder, UnsetType] = unset,
        has_value_labels: Union[bool, UnsetType] = unset,
        line_type: Union[WidgetLineType, UnsetType] = unset,
        line_width: Union[WidgetLineWidth, UnsetType] = unset,
        order_by: Union[WidgetStyleOrderBy, UnsetType] = unset,
        order_reverse: Union[bool, UnsetType] = unset,
        palette: Union[str, UnsetType] = unset,
        value_labels_density: Union[ValueLabelsDensity, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param color_order: Test-only generated schema for the dashboard versioning proof of concept.
        :type color_order: TimeseriesColorOrder, optional

        :param has_value_labels: Test-only generated schema for the dashboard versioning proof of concept.
        :type has_value_labels: bool, optional

        :param line_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type line_type: WidgetLineType, optional

        :param line_width: Test-only generated schema for the dashboard versioning proof of concept.
        :type line_width: WidgetLineWidth, optional

        :param order_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type order_by: WidgetStyleOrderBy, optional

        :param order_reverse: Test-only generated schema for the dashboard versioning proof of concept.
        :type order_reverse: bool, optional

        :param palette: Test-only generated schema for the dashboard versioning proof of concept.
        :type palette: str, optional

        :param value_labels_density: Test-only generated schema for the dashboard versioning proof of concept.
        :type value_labels_density: ValueLabelsDensity, optional
        """
        if color_order is not unset:
            kwargs["color_order"] = color_order
        if has_value_labels is not unset:
            kwargs["has_value_labels"] = has_value_labels
        if line_type is not unset:
            kwargs["line_type"] = line_type
        if line_width is not unset:
            kwargs["line_width"] = line_width
        if order_by is not unset:
            kwargs["order_by"] = order_by
        if order_reverse is not unset:
            kwargs["order_reverse"] = order_reverse
        if palette is not unset:
            kwargs["palette"] = palette
        if value_labels_density is not unset:
            kwargs["value_labels_density"] = value_labels_density
        super().__init__(kwargs)
