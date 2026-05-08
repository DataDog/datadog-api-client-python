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
    from datadog_api_client.v1.model.point_plot_dimension import PointPlotDimension


class PointPlotProjectionDimension(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.point_plot_dimension import PointPlotDimension

        return {
            "alias": (str,),
            "column": (str,),
            "dimension": (PointPlotDimension,),
        }

    attribute_map = {
        "alias": "alias",
        "column": "column",
        "dimension": "dimension",
    }

    def __init__(self_, column: str, dimension: PointPlotDimension, alias: Union[str, UnsetType] = unset, **kwargs):
        """
        Dimension mapping for the point plot projection.

        :param alias: Alias for the column.
        :type alias: str, optional

        :param column: Source column name from the dataset.
        :type column: str

        :param dimension: Dimension of the point plot.
        :type dimension: PointPlotDimension
        """
        if alias is not unset:
            kwargs["alias"] = alias
        super().__init__(kwargs)

        self_.column = column
        self_.dimension = dimension
