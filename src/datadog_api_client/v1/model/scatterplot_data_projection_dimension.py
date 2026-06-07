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
    from datadog_api_client.v1.model.scatterplot_dimension import ScatterplotDimension
    from datadog_api_client.v1.model.widget_number_format import WidgetNumberFormat


class ScatterplotDataProjectionDimension(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.scatterplot_dimension import ScatterplotDimension
        from datadog_api_client.v1.model.widget_number_format import WidgetNumberFormat

        return {
            "alias": (str,),
            "column": (str,),
            "dimension": (ScatterplotDimension,),
            "number_format": (WidgetNumberFormat,),
        }

    attribute_map = {
        "alias": "alias",
        "column": "column",
        "dimension": "dimension",
        "number_format": "number_format",
    }

    def __init__(
        self_,
        column: str,
        dimension: ScatterplotDimension,
        alias: Union[str, UnsetType] = unset,
        number_format: Union[WidgetNumberFormat, UnsetType] = unset,
        **kwargs,
    ):
        """
        A single dimension mapping for a scatterplot data projection.

        :param alias: Display alias for the dimension.
        :type alias: str, optional

        :param column: The column name from the data source.
        :type column: str

        :param dimension: Dimension of the Scatterplot.
        :type dimension: ScatterplotDimension

        :param number_format: Number format options for the widget.
        :type number_format: WidgetNumberFormat, optional
        """
        if alias is not unset:
            kwargs["alias"] = alias
        if number_format is not unset:
            kwargs["number_format"] = number_format
        super().__init__(kwargs)

        self_.column = column
        self_.dimension = dimension
