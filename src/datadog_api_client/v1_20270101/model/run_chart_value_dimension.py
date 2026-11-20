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
    from datadog_api_client.v1_20270101.model.run_chart_value_dimension_dimension import RunChartValueDimensionDimension
    from datadog_api_client.v1_20270101.model.widget_number_format import WidgetNumberFormat
    from datadog_api_client.v1_20270101.model.run_chart_line_style import RunChartLineStyle


class RunChartValueDimension(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.run_chart_value_dimension_dimension import (
            RunChartValueDimensionDimension,
        )
        from datadog_api_client.v1_20270101.model.widget_number_format import WidgetNumberFormat
        from datadog_api_client.v1_20270101.model.run_chart_line_style import RunChartLineStyle

        return {
            "alias": (str,),
            "column": (str,),
            "dimension": (RunChartValueDimensionDimension,),
            "number_format": (WidgetNumberFormat,),
            "style": (RunChartLineStyle,),
        }

    attribute_map = {
        "alias": "alias",
        "column": "column",
        "dimension": "dimension",
        "number_format": "number_format",
        "style": "style",
    }

    def __init__(
        self_,
        column: str,
        dimension: RunChartValueDimensionDimension,
        alias: Union[str, UnsetType] = unset,
        number_format: Union[WidgetNumberFormat, UnsetType] = unset,
        style: Union[RunChartLineStyle, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param alias: Test-only generated schema for the dashboard versioning proof of concept.
        :type alias: str, optional

        :param column: Test-only generated schema for the dashboard versioning proof of concept.
        :type column: str

        :param dimension: Test-only generated schema for the dashboard versioning proof of concept.
        :type dimension: RunChartValueDimensionDimension

        :param number_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type number_format: WidgetNumberFormat, optional

        :param style: Test-only generated schema for the dashboard versioning proof of concept.
        :type style: RunChartLineStyle, optional
        """
        if alias is not unset:
            kwargs["alias"] = alias
        if number_format is not unset:
            kwargs["number_format"] = number_format
        if style is not unset:
            kwargs["style"] = style
        super().__init__(kwargs)

        self_.column = column
        self_.dimension = dimension
