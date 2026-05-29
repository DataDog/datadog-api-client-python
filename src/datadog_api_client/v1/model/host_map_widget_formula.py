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
    from datadog_api_client.v1.model.host_map_widget_dimension import HostMapWidgetDimension
    from datadog_api_client.v1.model.widget_number_format import WidgetNumberFormat


class HostMapWidgetFormula(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.host_map_widget_dimension import HostMapWidgetDimension
        from datadog_api_client.v1.model.widget_number_format import WidgetNumberFormat

        return {
            "alias": (str,),
            "dimension": (HostMapWidgetDimension,),
            "formula": (str,),
            "number_format": (WidgetNumberFormat,),
        }

    attribute_map = {
        "alias": "alias",
        "dimension": "dimension",
        "formula": "formula",
        "number_format": "number_format",
    }

    def __init__(
        self_,
        dimension: HostMapWidgetDimension,
        formula: str,
        alias: Union[str, UnsetType] = unset,
        number_format: Union[WidgetNumberFormat, UnsetType] = unset,
        **kwargs,
    ):
        """
        Formula for the infrastructure host map widget that specifies both the expression
        and the visual dimension it populates.

        :param alias: Expression alias.
        :type alias: str, optional

        :param dimension: Visual dimension driven by a formula in the infrastructure host map widget.
        :type dimension: HostMapWidgetDimension

        :param formula: String expression built from queries, formulas, and functions.
        :type formula: str

        :param number_format: Number format options for the widget.
        :type number_format: WidgetNumberFormat, optional
        """
        if alias is not unset:
            kwargs["alias"] = alias
        if number_format is not unset:
            kwargs["number_format"] = number_format
        super().__init__(kwargs)

        self_.dimension = dimension
        self_.formula = formula
