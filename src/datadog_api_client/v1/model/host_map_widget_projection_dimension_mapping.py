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


class HostMapWidgetProjectionDimensionMapping(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.host_map_widget_dimension import HostMapWidgetDimension
        from datadog_api_client.v1.model.widget_number_format import WidgetNumberFormat

        return {
            "alias": (str,),
            "column": (str,),
            "dimension": (HostMapWidgetDimension,),
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
        dimension: HostMapWidgetDimension,
        alias: Union[str, UnsetType] = unset,
        number_format: Union[WidgetNumberFormat, UnsetType] = unset,
        **kwargs,
    ):
        """
        Maps a dataset column to a host map visual dimension.

        :param alias: Alias used to label the column instead of its name.
        :type alias: str, optional

        :param column: Source column name from the dataset.
        :type column: str

        :param dimension: Visual dimension for the host map widget. Used both by infrastructure-backed formulas and by DDSQL projection columns; ``group`` is only meaningful for DDSQL projection columns, where repeated entries define the grouping hierarchy.
        :type dimension: HostMapWidgetDimension

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
