# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.point_plot_projection_dimension import PointPlotProjectionDimension
    from datadog_api_client.v1.model.point_plot_projection_type import PointPlotProjectionType


class PointPlotProjection(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.point_plot_projection_dimension import PointPlotProjectionDimension
        from datadog_api_client.v1.model.point_plot_projection_type import PointPlotProjectionType

        return {
            "dimensions": ([PointPlotProjectionDimension],),
            "extra_columns": ([str],),
            "type": (PointPlotProjectionType,),
        }

    attribute_map = {
        "dimensions": "dimensions",
        "extra_columns": "extra_columns",
        "type": "type",
    }

    def __init__(
        self_,
        dimensions: List[PointPlotProjectionDimension],
        type: PointPlotProjectionType,
        extra_columns: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Projection configuration for the point plot widget.

        :param dimensions: List of dimension mappings for the projection.
        :type dimensions: [PointPlotProjectionDimension]

        :param extra_columns: Additional columns to include in the projection.
        :type extra_columns: [str], optional

        :param type: Type of the projection.
        :type type: PointPlotProjectionType
        """
        if extra_columns is not unset:
            kwargs["extra_columns"] = extra_columns
        super().__init__(kwargs)

        self_.dimensions = dimensions
        self_.type = type
