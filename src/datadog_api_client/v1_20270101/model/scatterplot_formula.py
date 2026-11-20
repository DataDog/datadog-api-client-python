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
    from datadog_api_client.v1_20270101.model.scatter_plot_dimension import ScatterPlotDimension
    from datadog_api_client.v1_20270101.model.scatterplot_formula_limit import ScatterplotFormulaLimit
    from datadog_api_client.v1_20270101.model.widget_number_format import WidgetNumberFormat
    from datadog_api_client.v1_20270101.model.widget_formula_style import WidgetFormulaStyle


class ScatterplotFormula(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.scatter_plot_dimension import ScatterPlotDimension
        from datadog_api_client.v1_20270101.model.scatterplot_formula_limit import ScatterplotFormulaLimit
        from datadog_api_client.v1_20270101.model.widget_number_format import WidgetNumberFormat
        from datadog_api_client.v1_20270101.model.widget_formula_style import WidgetFormulaStyle

        return {
            "alias": (str,),
            "dimension": (ScatterPlotDimension,),
            "formula": (str,),
            "limit": (ScatterplotFormulaLimit,),
            "number_format": (WidgetNumberFormat,),
            "style": (WidgetFormulaStyle,),
        }

    attribute_map = {
        "alias": "alias",
        "dimension": "dimension",
        "formula": "formula",
        "limit": "limit",
        "number_format": "number_format",
        "style": "style",
    }

    def __init__(
        self_,
        dimension: ScatterPlotDimension,
        formula: str,
        alias: Union[str, UnsetType] = unset,
        limit: Union[ScatterplotFormulaLimit, UnsetType] = unset,
        number_format: Union[WidgetNumberFormat, UnsetType] = unset,
        style: Union[WidgetFormulaStyle, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param alias: Test-only generated schema for the dashboard versioning proof of concept.
        :type alias: str, optional

        :param dimension: Test-only generated schema for the dashboard versioning proof of concept.
        :type dimension: ScatterPlotDimension

        :param formula: Test-only generated schema for the dashboard versioning proof of concept.
        :type formula: str

        :param limit: Test-only generated schema for the dashboard versioning proof of concept.
        :type limit: ScatterplotFormulaLimit, optional

        :param number_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type number_format: WidgetNumberFormat, optional

        :param style: Test-only generated schema for the dashboard versioning proof of concept.
        :type style: WidgetFormulaStyle, optional
        """
        if alias is not unset:
            kwargs["alias"] = alias
        if limit is not unset:
            kwargs["limit"] = limit
        if number_format is not unset:
            kwargs["number_format"] = number_format
        if style is not unset:
            kwargs["style"] = style
        super().__init__(kwargs)

        self_.dimension = dimension
        self_.formula = formula
